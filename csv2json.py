import csv
import json
import sys

with open(sys.argv[1], encoding='utf-8', mode='r') as csv_file:
    csv_content = csv.DictReader(csv_file)   
    with open(sys.argv[2], encoding='utf-8', mode='w') as new_file:
        new_file.write('[\n')
        for row in csv_content:
        	json.dump(row, new_file, ensure_ascii=False)
        	new_file.write(',\n')
        new_file.write(']')