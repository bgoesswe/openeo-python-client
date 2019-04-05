import csv

try:

    with open('/home/bgoesswe/results_timesheets.csv', mode='w') as results:
        results_file = csv.writer(results, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        fp = open('/home/bgoesswe/errors_in_timesheets', 'r')

        line = fp.readline()
        cnt = 1
        while line:
            line_parts = line.split(" Added ")
            if len(line_parts) >= 2:
                username = line_parts[1].split(": ")[0]
                date = line_parts[1].split(": ")[1]
                results_file.writerow([username, date])
                print("Write {}: {}".format(username, date))
            line = fp.readline()
            cnt += 1

finally:
    fp.close()