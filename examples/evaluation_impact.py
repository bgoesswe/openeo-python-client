import openeo
import logging
import time
# west, south, east, north
datasets = [
{"west": 10.288696, "south": 45.935871, "east": 12.189331, "north": 46.905246, "crs": "EPSG:4326", "begin": "2017-05-01", "end": "2017-05-31"}, # running example
{"west": 26.330109, "south": -16.023376, "east": 28.171692, "north": -15.253714, "crs": "EPSG:4326", "begin": "2006-03-30", "end": "2006-03-30"}, # http:// dx.doi.org/ 10.3390/ rs8050402 1
{"west": 26.830673, "south": -15.307366, "east": 27.052460, "north": -15.113227, "crs": "EPSG:4326", "begin": "2007-03-30", "end": "2007-03-30"}, # http:// dx.doi.org/ 10.3390/ rs8050402 2
{"west": 25.563812, "south": -14.429360, "east": 26.092529, "north": -13.980713, "crs": "EPSG:4326", "begin": "2006-03-29", "end": "2006-03-31"}, # http:// dx.doi.org/ 10.3390/ rs8050402 3
{"west": -2.449951, "south": 51.771239, "east": -2.239838, "north": 51.890901, "crs": "EPSG:4326", "begin": "2007-07-23", "end": "2007-07-23"}, # http:// dx.doi.org/ 10.1016/ j.jag.2014.12.001 1
{"west": -2.449951, "south": 51.771239, "east": -2.239838, "north": 51.890901, "crs": "EPSG:4326", "begin": "2005-08-22", "end": "2005-08-22"}, # http:// dx.doi.org/ 10.1016/ j.jag.2014.12.001 2
{"west": -2.449951, "south": 51.771239, "east": -2.239838, "north": 51.890901, "crs": "EPSG:4326", "begin": "2007-07-23", "end": "2007-07-24"}, # http:// dx.doi.org/ 10.1016/j.jag.2016.12.003 1
{"west": 16.506958, "south": 47.529257, "east": 17.188110, "north": 48.022998, "crs": "EPSG:4326", "begin": "2007-07-23", "end": "2007-07-24"}, # Big Data Infrastructures for Processing Sentinel Data, Wolfgang Wagner
{"west": 104.276733, "south": 8.423470, "east": 106.809082, "north": 11.156845, "crs": "EPSG:4326", "begin": "2007-01-01", "end": "2011-01-01"}, # THE USE OF SAR BACKSCATTER TIME SERIES FOR CHARACTERISING RICE PHENOLOGY, DUY NGUYEN
{"west": 17.078934, "south": 47.691739, "east": 18.022385, "north": 48.039070, "crs": "EPSG:4326",
     "begin": "2016-05-24", "end": "2016-05-24"}, # Digital Object Identifier 10.1109/TGRS.2018.2858004 1
{"west": 5.229492, "south": 36.261992, "east": 19.555664, "north": 46.830134, "crs": "EPSG:4326",
     "begin": "2017-10-01", "end": "2017-10-31"}, # Digital Object Identifier 10.1109/TGRS.2018.2858004 2
{"west": 10.074463, "south": 44.425934, "east": 13.842773, "north": 46.065608, "crs": "EPSG:4326",
     "begin": "2017-05-07", "end": "2017-05-07"}, # Digital Object Identifier 10.1109/TGRS.2018.2858004 3
{"west": 10.994568, "south": 43.661911, "east": 13.059998, "north": 44.820812, "crs": "EPSG:4326",
     "begin": "2017-04-01", "end": "2017-09-30"}, # Digital Object Identifier 10.1109/TGRS.2018.2858004 3
{"west": 15.062256, "south": 47.197178, "east": 18.347168, "north": 48.994636, "crs": "EPSG:4326",
     "begin": "2016-12-01", "end": "2016-12-31"}, #  https://doi.org/10.1080/01431161.2018.1479788 1
{"west": 10.994568, "south": 43.661911, "east": 13.059998, "north": 44.820812, "crs": "EPSG:4326",
     "begin": "2016-05-24", "end": "2016-05-24"}, #  doi:10.3390/rs10071030 1
{"west": 6.855469, "south": 36.279707, "east": 19.291992, "north": 49.296472, "crs": "EPSG:4326",
     "begin": "2017-10-01", "end": "2017-10-31"}, #  doi:10.3390/rs10071030 2
{"west": 9.063721, "south": 44.190082, "east": 17.973633, "north": 49.253465, "crs": "EPSG:4326",
     "begin": "2017-07-24", "end": "2017-07-24"}, #  doi:10.3390/rs10071030 3
{"west": 6.350098, "south": 36.120128, "east": 18.830566, "north": 47.025206, "crs": "EPSG:4326",
     "begin": "2017-07-23", "end": "2017-07-23"} #  doi:10.3390/rs10071030 4
]

LOCAL_EODC_DRIVER_URL = "http://openeo.local.127.0.0.1.nip.io"

logging.basicConfig(level=logging.INFO)
logging.info("--- Impact Evaluation ---")
logging.info("Connecting to the local back end {}...".format(LOCAL_EODC_DRIVER_URL))

# Connect to database
con = openeo.connect(LOCAL_EODC_DRIVER_URL)
processes = con.get_processes()
# Reset back end database
logging.info("Reset back end database {}...".format(LOCAL_EODC_DRIVER_URL))
con.resetdb()

NUMBER_OF_ITERATIONS = 10

counter = 1
number_of_testcases = len(datasets)
for testcase in datasets:

    # Choose dataset
    pgA = processes.get_collection(name="s2a_prd_msil1c")
    pgA = processes.filter_daterange(pgA, extent=[testcase["begin"], testcase["end"]])
    pgA = processes.filter_bbox(pgA, west=testcase["west"], south=testcase["south"], east=testcase["east"], north=testcase["north"], crs=testcase["crs"])

    # Choose processes
    pgA = processes.ndvi(pgA, nir="B08", red="B04")
    pgA = processes.min_time(pgA)
    #logging.info("Creating testcase {}/{}...".format(counter, number_of_testcases))
    logging.info("Start testcase {}/{}...".format(counter, number_of_testcases))
    #time.sleep(2)
    for i in range(NUMBER_OF_ITERATIONS):
        jobA = con.create_job(pgA.graph)
        jobA.start_job()

        desc = jobA.describe_job
        while desc["status"] == "submitted":
            desc = jobA.describe_job
        logging.info("Status of testcase {}: {}".format(counter, desc["status"]))

    logging.info("Finished testcase {}/{}...".format(counter, number_of_testcases))

    counter += 1



''' 1. Run Job A, which creates query PID-A. Get file list of PID-A '''

''' 1. Run Job A, which creates query PID-A. Get file list of PID-A '''
logging.info("1. Run Job A, which creates query PID-A. Get file list of PID-A")


con = openeo.connect(LOCAL_EODC_DRIVER_URL)


logging.info("Preparing Porcess graph for Job A...")
# Create job A out of the process graph A (pgA)
logging.info("Creating Job A and retrieving Job A ID...")
jobA = con.create_job(pgA.graph)
logging.info("Job A with ID {} created...".format(jobA.job_id))
logging.info("Starting Job A...")
jobA.start_job()

# Wait until the job execution was finished
logging.info("Job A Processing...")
desc = jobA.describe_job
while desc["status"] == "submitted":
    desc = jobA.describe_job

# re-execute query and get the resulting file list from the back end
pidA = jobA.get_data_pid()
file_list = con.get_filelist(pidA)
logging.info("Query re-execution filelist: {}".format(file_list))

''' 2. Update one of the resulting files of the PID-A query  '''
# Use flag on the back end to switch to the simulation CSW back end.
logging.info("Update one of the resulting files of the PID-A query")
con.set_mockupstate(deleted=True)
file2_list = con.get_filelist(pidA)

''' 3. Researcher A cites the input data in a publication  '''
logging.info("3. Researcher A cites the input data in a publication")
''' 4. Researcher B uses the same input data of job A for job B  '''
logging.info(str(file_list["input_files"] == file2_list["input_files"]))
logging.info("4. Researcher B uses the same input data of job A for job B")
# Take input data of job A by using the input data pid A of job A
pgB = processes.get_collection(data_pid=pidA)

# Choose processes
pgB = processes.ndvi(pgB, nir="B08", red="B04")
pgB = processes.max_time(pgB)
logging.info("Preparing Porcess graph for Job B using data PID from job A {}...".format(pidA))
# Create job B out of the process graph B (pgB)
logging.info("Preparing Porcess graph for Job B using data PID from job A {}...")
jobB = con.create_job(pgB.graph)
logging.info("Creating and starting job B with id {}".format(jobB.job_id))
jobB.start_job()

logging.info("Job A Processing...")
desc = jobB.describe_job
while desc["status"] == "submitted":
    desc = jobB.describe_job
logging.info("Finished processing job B")

logging.info("JobB data pid: {}".format(jobB.get_data_pid_url()))

logging.info("Finished Use Case 1")

