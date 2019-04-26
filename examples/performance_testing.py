import datetime
from hashlib import sha256

max_files = 10000

def create_result_hash(result_files):
    # Remove all characters from the result files list that are not relevant and create a hash.
    result_list = str(result_files).split("]")[0]
    result_list += "]"
    result_list = result_list.replace(" ", "")
    result_list = result_list.replace("\t", "")
    result_list = result_list.replace("\n", "")
    # Mockup for Evaluation TESTCASE1
    # result_list = result_list.replace("S2A_MSIL1C_20170104T101402_N0204_R022_T32TPR_20170104T101405",
    #                                  "S2A_MSIL1C_20170104T101402_N0204_R022_T32TPR_20170104T101405_NEW")
    result_list = result_list.encode('utf-8')
    result_list = result_list.strip()

    result_hash = sha256(result_list).hexdigest()

    return result_hash


entry = {'date': '2017-05-04', 'name': 'S2A_MSIL1C_20170504T101031_N0205_R022_T32TPR_20170504T101349_new',
         'timestamp': '2017-05-08',
         'path': '/eodc/products/copernicus.eu/s2a_prd_msil1c/2017/05/04/S2A_MSIL1C_20170504T101031_N0205_R022_T32TPR_20170504T101349.zip_new'}

file_list = []

max_iteration = 500
steps = 1000
for j in range(0, max_files, steps):
    milliseconds = 0
    count = 0
    for k in range(0, steps, 1):
        file_list.append(entry)

    for i in range(0, max_iteration, 1):

        start = datetime.datetime.utcnow()
        create_result_hash(file_list)
        end = datetime.datetime.utcnow()
        delta = end - start
        milliseconds += delta.microseconds
        count += 1
    message = "{} ; {}".format(len(file_list), str(milliseconds/max_iteration))
    print(message)