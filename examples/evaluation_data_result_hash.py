from hashlib import sha256
import datetime
entry = {'date': '2017-05-04', 'name': 'S2A_MSIL1C_20170504T101031_N0205_R022_T32TPR_20170504T101349_new', 'timestamp': '2017-05-08', 'path': '/eodc/products/copernicus.eu/s2a_prd_msil1c/2017/05/04/S2A_MSIL1C_20170504T101031_N0205_R022_T32TPR_20170504T101349.zip_new'}

def create_result_hash(result_files):
    # Remove all characters from the result files list that are not relevant and create a hash.
    result_list = str(result_files)
    #result_list += "]"
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

MAX_FILELIST = 1000000

file_list = []

for i in range(0, MAX_FILELIST, 100):
    file_list.append(entry)
    start = datetime.datetime.utcnow()
    create_result_hash(file_list)
    end = datetime.datetime.utcnow()
    delta = end - start
    message = "{} ; {}".format(i, str(int(delta.total_seconds() * 1000)))
    print(message)