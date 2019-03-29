import openeo
import logging

logging.basicConfig(level=logging.INFO)

''' 1. Researcher A runs an experiment (job A) at the EODC back end  '''
logging.info("1. Researcher A runs an experiment (job A) at the EODC back end")
LOCAL_EODC_DRIVER_URL = "http://openeo.local.127.0.0.1.nip.io"
logging.info("Connecting to the local back end {}...".format(LOCAL_EODC_DRIVER_URL))

import openeo
#connect to back end
con = openeo.connect(LOCAL_EODC_DRIVER_URL)
# Choose dataset
processes = con.get_processes()
pgA = processes.get_collection(name="s2a_prd_msil1c")
pgA = processes.filter_daterange(pgA, extent=["2017-05-01", "2017-05-31"])
pgA = processes.filter_bbox(pgA, west=10.288696, south=45.935871, east=12.189331, north=46.905246, crs="EPSG:4326")
# Choose processes
pgA = processes.ndvi(pgA, nir="B08", red="B04")
pgA = processes.min_time(pgA)
# Create and start job at the back end
# This generates the job context model and the input data (query) PID
jobA = con.create_job(pgA.graph)
jobA.start_job()
# Returns resolveable Query PID e.g. EODC_DRIVER_URL/collections/qu-d1701f4e-e7c5-4a83-92e0-9facbd401a06
pidA = jobA.get_data_pid_url()
# Re-executes the query and returns the resulting file list.
file_list = con.get_filelist(pidA)
# Reusing the data PID with a different workflow
pgB = processes.get_collection(data_pid=pidA)
# Choose processes for the new workflow
pgB = processes.ndvi(pgB, nir="B08", red="B04")
pgB = processes.max_time(pgB)
# ...

''' 2. Researcher A retrieves the used input data of job A.  '''

pidA_url = jobA.get_data_pid_url()
logging.info("Data PID: {}".format(pidA_url))

pidA = jobA.get_data_pid()
# retrieve information about the pidA e.g. executed query and description about the dataset.
desc = con.describe_collection(pidA)
logging.info("Data PID description: {}".format(desc))

query = desc["query"]
# re-execute query and get the resulting file list from the back end
file_list = con.get_filelist(pidA)
logging.info("Query re-execution filelist: {}".format(file_list))

''' 3. Researcher A cites the input data in a publication  '''
logging.info("3. Researcher A cites the input data in a publication")
''' 4. Researcher B uses the same input data of job A for job B  '''
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
