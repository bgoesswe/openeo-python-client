import json
import csv
# Read storage result of the impact evaluation
# Format: [job, query, jobquery]
storage_data = None
with open('storage_file.json') as json_file:
    storage_data = json.load(json_file)

# Read performance result of the impact evaluation
# Format: [preparation, processing, query_handler, context_model]
performance_data = None
with open('performance_file_new.json') as json_file:
    performance_data = json.load(json_file)

storage_mean = {}
performance_mean = {}

with open('results_new.csv', mode='w') as results:
    results_file = csv.writer(results, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#    results_file.writerow(['Storage Results'])
#    results_file.writerow(['Context Model', 'Query Table', 'QueryJob Table'])
#    for key, value in storage_data.items():
#        results_file.writerow(['Testcase {}'.format(str(key))])

        #count = [0,0,0]
#        for entry in value:
#            row = [0, 0, 0]
#            for i in range(3):
#                if entry[i][0]:
#                    row[i] = entry[i][0]
#            if row[1] > 0:
#                results_file.writerow(row)

        # mean_job = None
        # mean_query = None
        # mean_queryjob = None
        # if count[0] > 0:
        #     mean_job = sum[0]/count[0]
        # if count[1] > 0:
        #     mean_query = sum[1]/count[1]
        # if count[2] > 0:
        #     mean_queryjob = sum[2]/count[2]
        #
        # storage_mean[key] = [mean_job, mean_query, mean_queryjob]

 #   print(storage_mean)
    results_file.writerow(['Performance Results'])
    results_file.writerow(['Preparation time', 'Execution time', 'QueryHandler time', 'Context Model time', 'DATA', 'normalized', 'norm_hash', 'result_hash', 'check_existing', 'dataset_pid', 'orig_query', 'file_number', 'query persistence', 'Context Model', 'load_job_query', 'result hash', 'static_stuff', 'pip_freeze', 'interpreter_start_end'])
    for key, value in performance_data.items():
        results_file.writerow(['Testcase {}'.format(str(key))])
        # count = [0,0,0,0]
        for entry in value:
            row = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            for i in range(len(row)):
                if entry[i]:
                    if not ("data" in entry[i] or "cm" in entry[i]):
                        row[i] = int(entry[i])
            results_file.writerow(row)


        # mean_prep = None
        # mean_exec = None
        # mean_query = None
        # mean_context = None
        #
        # if count[0] > 0:
        #     mean_prep = sum[0]/count[0]
        # if count[1] > 0:
        #     mean_exec = sum[1]/count[1]
        # if count[2] > 0:
        #     mean_query = sum[2]/count[2]
        # if count[3] > 0:
        #     mean_context = sum[2]/count[2]
        #
        # performance_mean[key] = [mean_prep, mean_exec, mean_query, mean_context]

   # print(performance_mean)




