import csv
import json
import sys

with open('test.csv', 'r') as csv_file:
    csv_content = csv.DictReader(csv_file)   
    with open('new.json', 'w') as new_file:
        new_file.write('[\n')
        for row in csv_content:
            json.dump(row, new_file)
            new_file.write(',\n')
        new_file.write(']')