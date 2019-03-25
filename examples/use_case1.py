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

''' 2. Researcher A retrieves the used input data of job A.  '''

pidA_url = jobA.get_data_pid_url()
print(pidA_url)

pidA = jobA.get_data_pid()
# retrieve information about the pidA e.g. executed query and description about the dataset.
desc = con.describe_collection(pidA)

query = desc["query"]
# re-execute query and get the resulting file list from the back end
file_list = con.get_filelist(pidA)

''' 3. Researcher A cites the input data in a publication  '''

''' 4. Researcher B uses the same input data of job A for job B  '''

# Take input data of job A by using the input data pid A of job A
pgB = processes.get_collection(data_pid=pidA)

# Choose processes
pgB = processes.ndvi(pgB, nir="B08", red="B04")
pgB = processes.max_time(pgB)

# Create job B out of the process graph B (pgB)

jobB = con.create_job(pgB.graph)
jobB.start_job()

