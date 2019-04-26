import openeo
import logging
import time
import psycopg2
import json
# west, south, east, north
testcases = [
#{"testcase": 1, "west": 10.5833333, "south": 46.383333, "east": 10.733333, "north": 46.483333, "crs": "EPSG:4326", "begin": "2017-09-01", "end": "2017-09-30"}, # https://doi.org/10.1109/JSTARS.2016.2587819
#{"testcase": 2, "west": 26.330109, "south": -16.023376, "east": 28.171692, "north": -15.253714, "crs": "EPSG:4326", "begin": "2017-03-24", "end": "2017-03-31"}, # http:// dx.doi.org/ 10.3390/ rs8050402 1
#{"testcase": 3, "west": 26.830673, "south": -15.307366, "east": 27.052460, "north": -15.113227, "crs": "EPSG:4326", "begin": "2017-03-24", "end": "2017-03-31"}, # http:// dx.doi.org/ 10.3390/ rs8050402 2
#{"testcase": 4, "west": 25.563812, "south": -14.429360, "east": 26.092529, "north": -13.980713, "crs": "EPSG:4326", "begin": "2017-03-29", "end": "2017-03-31"}, # http:// dx.doi.org/ 10.3390/ rs8050402 3
#{"testcase": 5, "west": -2.449951, "south": 51.771239, "east": -2.239838, "north": 51.890901, "crs": "EPSG:4326", "begin": "2017-07-16", "end": "2017-07-23"}, # http:// dx.doi.org/ 10.1016/ j.jag.2014.12.001 1
#{"testcase": 6, "west": -2.449951, "south": 51.771239, "east": -2.239838, "north": 51.890901, "crs": "EPSG:4326", "begin": "2017-08-22", "end": "2017-08-23"}, # http:// dx.doi.org/ 10.1016/ j.jag.2014.12.001 2
#{"testcase": 7, "west": -2.449951, "south": 51.771239, "east": -2.239838, "north": 51.890901, "crs": "EPSG:4326", "begin": "2017-07-23", "end": "2017-07-24"}, # http:// dx.doi.org/ 10.1016/j.jag.2016.12.003 1
#{"testcase": 8, "west": 16.506958, "south": 47.529257, "east": 17.188110, "north": 48.022998, "crs": "EPSG:4326", "begin": "2017-07-16", "end": "2017-07-24"}, # 10.3390/rs8110938
{"testcase": 9, "west": 104.076733, "south": 8.423470, "east": 108.809082, "north": 12.156845, "crs": "EPSG:4326", "begin": "2017-03-02", "end": "2018-03-02"}, # 10.1080/2150704X.2016.1225172
##{"testcase": 10, "west": 17.078934, "south": 47.691739, "east": 18.022385, "north": 48.039070, "crs": "EPSG:4326",
##     "begin": "2017-05-18", "end": "2017-05-25"}, # Digital Object Identifier 10.1109/TGRS.2018.2858004 1
##{"testcase": 11, "west": 10.229492, "south": 36.261992, "east": 19.555664, "north": 46.830134, "crs": "EPSG:4326",
##     "begin": "2017-10-01", "end": "2017-10-31"}, # Digital Object Identifier 10.1109/TGRS.2018.2858004 2
#{"testcase": 12, "west": 10.074463, "south": 44.425934, "east": 13.842773, "north": 46.065608, "crs": "EPSG:4326",
#     "begin": "2017-05-07", "end": "2017-05-08"}, # Digital Object Identifier 10.1109/TGRS.2018.2858004 3
#{"testcase": 13, "west": 10.994568, "south": 43.661911, "east": 13.059998, "north": 44.820812, "crs": "EPSG:4326",
#     "begin": "2017-09-01", "end": "2017-09-30"}, # Digital Object Identifier 10.1109/TGRS.2018.2858004 4
##{"testcase": 14, "west": 15.062256, "south": 47.197178, "east": 18.347168, "north": 49.594636, "crs": "EPSG:4326",
##     "begin": "2017-01-31", "end": "2017-06-01"}, #  https://doi.org/10.1080/01431161.2018.1479788 1
##{"testcase": 15, "west": 10.994568, "south": 43.661911, "east": 13.059998, "north": 44.820812, "crs": "EPSG:4326",
##     "begin": "2017-05-18", "end": "2017-05-25"}, #  doi:10.3390/rs10071030 1
##{"testcase": 16, "west": 10.855469, "south": 38.279707, "east": 19.291992, "north": 49.296472, "crs": "EPSG:4326",
##     "begin": "2017-10-01", "end": "2017-10-31"}, #  doi:10.3390/rs10071030 2
##{"testcase": 17, "west": 9.063721, "south": 44.190082, "east": 17.973633, "north": 49.253465, "crs": "EPSG:4326",
##     "begin": "2017-07-24", "end": "2017-07-25"}, #  doi:10.3390/rs10071030 3
##{"testcase": 18, "west": 11.350098, "south": 40.120128, "east": 18.830566, "north": 47.025206, "crs": "EPSG:4326",
##     "begin": "2017-07-23", "end": "2017-07-24"} #  doi:10.3390/rs10071030 4
]


LOCAL_EODC_DRIVER_URL = "http://openeo.local.127.0.0.1.nip.io"

# These have to be adapted to the local instance of the back end (in OpenShift web interface under "Services")
LOCAL_PSQL_USER = "bg"
LOCAL_PSQL_PWD = "bg12345"
LOCAL_PSQL_URL = "172.30.120.58"#172.30.161.214"

JOB_COLUMN_QUERY = "SELECT sum(pg_column_size(metrics)) as filesize, count(*) as filerow FROM jobs as t WHERE id = '{}'"
QUERY_TABLE_QUERY = "SELECT sum(pg_column_size(t)) as filesize, count(*) as filerow FROM query as t WHERE query_pid = '{}'"
QUERYJOB_TABLE_QUERY = "SELECT sum(pg_column_size(t)) as filesize, count(*) as filerow FROM queryjob as t WHERE job_id = '{}'"


logging.basicConfig(level=logging.INFO)
logging.info("--- Impact Evaluation ---")
logging.info("Connecting to the local back end {}...".format(LOCAL_EODC_DRIVER_URL))

# Connect to back end
con = openeo.connect(LOCAL_EODC_DRIVER_URL)
processes = con.get_processes()
# Reset back end database


storage_dict = {}
performance_dict = {}

NUMBER_OF_ITERATIONS = 50
MAX_TRY = 5

counter = 1
number_of_testcases = len(testcases)
for testcase in testcases:


    # Choose dataset
    pgA = processes.get_collection(name="s2a_prd_msil1c")
    pgA = processes.filter_daterange(pgA, extent=[testcase["begin"], testcase["end"]])
    pgA = processes.filter_bbox(pgA, west=testcase["west"], south=testcase["south"], east=testcase["east"], north=testcase["north"], crs=testcase["crs"])

    # Choose processes
    pgA = processes.ndvi(pgA, nir="B08", red="B04")
    pgA = processes.min_time(pgA)
    #logging.info("Creating testcase {}/{}...".format(counter, number_of_testcases))

    storage_dict[counter] = []
    performance_dict[testcase["testcase"]] = []

    logging.info("Start testcase {} --> {}/{}...".format(str(testcase["testcase"]), str(counter), str(number_of_testcases)))
    #time.sleep(2)
    jobA = con.create_job(pgA.graph)
    if jobA:
        jobA.start_job()
    time.sleep(10)
    for i in range(NUMBER_OF_ITERATIONS):

        logging.info("Reset back end database {}...".format(LOCAL_EODC_DRIVER_URL))
        con.resetdb()
        logging.info("Execution testcase {} --> {}/{}...".format(str(testcase["testcase"]), str(i), str(NUMBER_OF_ITERATIONS-1)))
        #try:
        jobA = con.create_job(pgA.graph)
        if jobA:
            jobA.start_job()

            desc = jobA.describe_job
            tries = 0
            while desc["status"] == "submitted":
                time.sleep(2)
                desc = jobA.describe_job
                if tries >= MAX_TRY:
                    break
                tries += 1
            pidA = jobA.get_data_pid()
            # try:
            #     connection = psycopg2.connect(user=LOCAL_PSQL_USER,
            #                               password=LOCAL_PSQL_PWD,
            #                               host=LOCAL_PSQL_URL,
            #                               port="5432",
            #                               database="jobs")
            #     cursor = connection.cursor()
            #     storage_entry = []
            #     cursor.execute(JOB_COLUMN_QUERY.format(jobA.job_id))
            #     job_size = cursor.fetchall()
            #     storage_entry.append(job_size[0])
            #     cursor.execute(QUERY_TABLE_QUERY.format(pidA))
            #     query_size = cursor.fetchall()
            #     storage_entry.append(query_size[0])
            #     cursor.execute(QUERYJOB_TABLE_QUERY.format(jobA.job_id))
            #     queryjob_size = cursor.fetchall()
            #     storage_entry.append(queryjob_size[0])
            #     storage_dict[counter].append(storage_entry)
            #     #print(job_size)
            #
            # except (Exception, psycopg2.Error) as error:
            #     print("Error while fetching from PostgreSQL", error)
            # finally:
            #     # closing database connection.
            #     if (connection):
            #         cursor.close()
            #         connection.close()
            #         #print("PostgreSQL connection is closed")

            logging.info("Status of testcase {}: {}".format(testcase["testcase"], desc["status"]))
            if desc["status"] != "submitted":
                performance_dict[testcase["testcase"]].append(desc["status"].split(";"))
        else:
            time.sleep(5)
        #except Exception:
        #    logging.info("Status of testcase {}: exception".format(counter))

    logging.info("Finished testcase {} --> {}/{}...".format(testcase["testcase"], counter, number_of_testcases))
    counter += 1
#with open('storage_file_new.json', 'w') as file:
#    file.write(json.dumps(storage_dict))
with open('performance_file_new.json', 'w') as file:
    file.write(json.dumps(performance_dict))

# Get Size of job table:
# SELECT sum(pg_column_size(metrics)) as filesize, count(*) as filerow FROM jobs as t WHERE id = ;
# Get Size of Query table:
# SELECT sum(pg_column_size(t)) as filesize, count(*) as filerow FROM query as t WHERE id = ;
# Get Size of QueryJob table:
# SELECT sum(pg_column_size(t)) as filesize, count(*) as filerow FROM queryjob as t WHERE job_id = ;