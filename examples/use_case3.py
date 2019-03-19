import openeo
import logging

logging.basicConfig(level=logging.INFO)

''' 1. Researcher A runs an experiment (job A) at the EODC back end  '''
EODC_DRIVER_URL = "http://openeo.local.127.0.0.1.nip.io"

OUTPUT_FILE = "/tmp/openeo_eodc_output.tif"

con = openeo.connect(EODC_DRIVER_URL)

# Choose dataset
processes = con.get_processes()
pgA = processes.get_collection(name="s2a_prd_msil1c")
pgA = processes.filter_daterange(pgA, extent=["2017-05-01", "2017-05-31"])
pgA = processes.filter_bbox(pgA, west=10.288696, south=45.935871, east=12.189331, north=46.905246, crs="EPSG:4326")

# Choose processes
pgA = processes.ndvi(pgA, nir="B08", red="B04")
pgA = processes.min_time(pgA)



# Create job A out of the process graph A (pgA)

jobA = con.create_job(pgA.graph)
jobA.start_job()

# Wait until the job execution was finished
desc = jobA.describe_job
while desc["status"] == "submitted":
    desc = jobA.describe_job

''' 2. Researcher B re-runs the same experiment (job B).  '''

# Get the already executed job A by Id
from openeo.rest.job import RESTJob

jobA_new = RESTJob(jobA.job_id, con)

# Get process graph of job A and create new job B with it
pgA = jobA_new.describe_job["process_graph"]

jobB = con.create_job(pgA)

jobB.start_job()


''' 3. Researcher runs a different experiment (job C).  '''

# Choose dataset
processes = con.get_processes()
pgC = processes.get_collection(name="s2a_prd_msil1c")
pgC = processes.filter_daterange(pgC, extent=["2017-05-01", "2017-05-31"])
pgC = processes.filter_bbox(pgC, west=10.288696, south=45.935871, east=12.189331, north=46.905246, crs="EPSG:4326")

# Choose processes
pgC = processes.ndvi(pgC, nir="B08", red="B04")
pgC = processes.max_time(pgC)

# Create job C out of the process graph C (pgC)

jobC = con.create_job(pgC.graph)
jobC.start_job()

# Wait until the job execution was finished
desc = jobC.describe_job
while desc["status"] == "submitted":
    desc = jobC.describe_job

''' 4. Researcher wants to compare the jobs by their environment and outcome. '''

diffAB = jobA.diff(jobB)
diffAC = jobA.diff(jobC)
print("finished")