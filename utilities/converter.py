# converter.py
# description: using csv and json modules, can convert csv to json 
# objects by reading in any csv file, appending the data array with 
# everyone Dictionary pair creating the empty  json file, writing each 
# array item to a set of json key:value pairs.

import csv
import json

data = []
with open('1k-new.csv', 'r', newline='') as infile:
    for row in csv.DictReader(infile):
        data.append(row)

with open('GeneralMotors_OEM.json','w') as outfile:
    for d in data:
        json.dump(d, outfile)

