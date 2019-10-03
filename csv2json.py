import csv
import json
import sys


try:
    csv_filename = sys.argv[1]
    json_file = sys.argv[2]

    csv_file = open(csv_filename, "r")
    csv_content = csv.DictReader(csv_file)
    json_out = json.dumps([row for row in csv_content], indent=2)

    new_file = open(json_file, "w")
    new_file.write(json_out)
    new_file.close()

    print("Sucess!!!")
except IOError as io_error:
    print(io_error)
