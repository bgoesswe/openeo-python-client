import openeo
import logging
import time
from openeo.auth.auth_bearer import BearerAuth
from openeo.rest.job import RESTJob

logging.basicConfig(level=logging.INFO)



stats = testcases = [
#{"testcase": 1, "west": 10.5833333, "south": 46.383333, "east": 10.733333, "north": 46.483333, "crs": "EPSG:4326", "begin": "2017-09-01", "end": "2017-09-30"}, # https://doi.org/10.1109/JSTARS.2016.2587819
#{"testcase": 2, "west": 26.330109, "south": -16.023376, "east": 28.171692, "north": -15.253714, "crs": "EPSG:4326", "begin": "2017-03-24", "end": "2017-03-31"}, # http:// dx.doi.org/ 10.3390/ rs8050402 1
#{"testcase": 3, "west": 26.830673, "south": -15.307366, "east": 27.052460, "north": -15.113227, "crs": "EPSG:4326", "begin": "2017-03-24", "end": "2017-03-31"}, # http:// dx.doi.org/ 10.3390/ rs8050402 2
#{"testcase": 4, "west": 25.563812, "south": -14.429360, "east": 26.092529, "north": -13.980713, "crs": "EPSG:4326", "begin": "2017-03-29", "end": "2017-03-31"}, # http:// dx.doi.org/ 10.3390/ rs8050402 3
#{"testcase": 5, "west": -2.449951, "south": 51.771239, "east": -2.239838, "north": 51.890901, "crs": "EPSG:4326", "begin": "2017-07-16", "end": "2017-07-23"}, # http:// dx.doi.org/ 10.1016/ j.jag.2014.12.001 1
#{"testcase": 6, "west": -2.449951, "south": 51.771239, "east": -2.239838, "north": 51.890901, "crs": "EPSG:4326", "begin": "2017-08-22", "end": "2017-08-23"}, # http:// dx.doi.org/ 10.1016/ j.jag.2014.12.001 2
#{"testcase": 7, "west": -2.449951, "south": 51.771239, "east": -2.239838, "north": 51.890901, "crs": "EPSG:4326", "begin": "2017-07-23", "end": "2017-07-24"}, # http:// dx.doi.org/ 10.1016/j.jag.2016.12.003 1
#{"testcase": 8, "west": 16.506958, "south": 47.529257, "east": 17.188110, "north": 48.022998, "crs": "EPSG:4326", "begin": "2017-07-16", "end": "2017-07-24"}, # 10.3390/rs8110938
{"testcase": 9, "west": 104.076733, "south": 8.423470, "east": 108.809082, "north": 12.156845, "crs": "EPSG:4326", "begin": "2016-03-02", "end": "2018-03-02"}, # 10.1080/2150704X.2016.1225172
{"testcase": 10, "west": 17.078934, "south": 47.691739, "east": 18.022385, "north": 48.039070, "crs": "EPSG:4326",
     "begin": "2016-05-18", "end": "2016-05-25"}, # Digital Object Identifier 10.1109/TGRS.2018.2858004 1
{"testcase": 11, "west": 5.229492, "south": 36.261992, "east": 19.555664, "north": 46.830134, "crs": "EPSG:4326",
     "begin": "2017-10-01", "end": "2017-10-31"}, # Digital Object Identifier 10.1109/TGRS.2018.2858004 2
{"testcase": 12, "west": 10.074463, "south": 44.425934, "east": 13.842773, "north": 46.065608, "crs": "EPSG:4326",
     "begin": "2017-05-07", "end": "2017-05-08"}, # Digital Object Identifier 10.1109/TGRS.2018.2858004 3
{"testcase": 13, "west": 10.994568, "south": 43.661911, "east": 13.059998, "north": 44.820812, "crs": "EPSG:4326",
     "begin": "2017-09-01", "end": "2017-09-30"}, # Digital Object Identifier 10.1109/TGRS.2018.2858004 4
{"testcase": 14, "west": 15.062256, "south": 47.197178, "east": 18.347168, "north": 49.594636, "crs": "EPSG:4326",
     "begin": "2016-01-31", "end": "2017-06-01"}, #  https://doi.org/10.1080/01431161.2018.1479788 1
{"testcase": 15, "west": 10.994568, "south": 43.661911, "east": 13.059998, "north": 44.820812, "crs": "EPSG:4326",
     "begin": "2016-05-18", "end": "2016-05-25"}, #  doi:10.3390/rs10071030 1
{"testcase": 16, "west": 6.855469, "south": 36.279707, "east": 19.291992, "north": 49.296472, "crs": "EPSG:4326",
     "begin": "2017-10-01", "end": "2017-10-31"}, #  doi:10.3390/rs10071030 2
{"testcase": 17, "west": 9.063721, "south": 44.190082, "east": 17.973633, "north": 49.253465, "crs": "EPSG:4326",
     "begin": "2017-07-24", "end": "2017-07-25"}, #  doi:10.3390/rs10071030 3
{"testcase": 18, "west": 6.350098, "south": 36.120128, "east": 18.830566, "north": 47.025206, "crs": "EPSG:4326",
     "begin": "2017-07-23", "end": "2017-07-24"} #  doi:10.3390/rs10071030 4
]
GEE_DRIVER_URL = "http://giv-openeo.uni-muenster.de:8080/v0.3"

OUTPUT_FILE = "/tmp/openeo_gee_output.png"

user = "group1"
password = "test123"

#connect with GEE backend
#session = openeo.session("nobody", GEE_DRIVER_URL)


con = openeo.connect(GEE_DRIVER_URL, auth_type=BearerAuth, auth_options={"username": user, "password": password})

#Test Connection
print(con.list_processes())
print(con.list_collections())
print(con.describe_collection("COPERNICUS/S2"))


# # Test Capabilities
# cap = con.capabilities
#
# print(cap.version())
# print(cap.list_features())
# print(cap.currency())
# print(cap.list_plans())
#
# # Test Processes
# #for stats in testcases:
# processes = con.get_processes()
# pg = processes.get_collection(name="COPERNICUS/S2")
# print(pg.graph)
# pg = processes.filter_bbox(pg, west=stats["west"], south=stats["south"], east=stats["east"], north=stats["north"],
#                            crs="EPSG:4326")
# print(pg.graph)
# pg = processes.filter_daterange(pg, extent=[stats["begin"] + "T00:00:00Z", stats["end"] + "T23:59:59Z"])
# print(pg.graph)
# pg = processes.ndvi(pg, nir="B4", red="B8A")
# print(pg.graph)
# pg = processes.min_time(pg)
# print(pg.graph)

# Test Job

#job = con.create_job(pg.graph)
#print("Test Case {}: {}".format(stats["testcase"], str(job.job_id)))
#print(job.start_job())
# print(job.describe_job)
job = RESTJob(job_id="egZeQzJBRUSyD7M3", connection=con)
#job.start_job()
#time.sleep(20)
test = job.download_results("/tmp/testcase_9")
#test = job.download_results("/tmp/testcase_{}".format(stats["testcase"]))
print("Finished TestCase 9 : {}".format(str(test)))

# 10.228271,45.537137,12.425537,46.860191
# west, south, east, north

# PoC JSON:
# {
#     "process_graph":{
#         "process_id":"stretch_colors",
#         "args":{
#             "imagery":{
#                 "process_id":"min_time",
#                 "args":{
#                     "imagery":{
#                         "process_id":"NDVI",
#                         "args":{
#                             "imagery":{
#                                 "process_id":"filter_daterange",
#                                 "args":{
#                                     "imagery":{
#                                         "process_id":"filter_bbox",
#                                         "args":{
#                                             "imagery":{
#                                                 "product_id":"COPERNICUS/S2"
#                                             },
#                                             "left":9.0,
#                                             "right":9.1,
#                                             "top":12.1,
#                                             "bottom":12.0,
#                                             "srs":"EPSG:4326"
#                                         }
#                                     },
#                                     "from":"2017-01-01",
#                                     "to":"2017-01-31"
#                                 }
#                             },
#                             "red":"B4",
#                             "nir":"B8"
#                         }
#                     }
#                 }
#             },
#             "min": -1,
#             "max": 1
#         }
#     },
#     "output":{
#         "format":"png"
#     }
# }
