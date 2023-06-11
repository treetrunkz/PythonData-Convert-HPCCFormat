# column-builder
# description: between two csv's replace one row from a csv with another 
# returned as a "-new" ouput file.

import os
import csv
import json
import pandas as pd
import re

rowlist = []
# pre
csv1 = 'assets/GeneralMotors_OEM.csv'
csv2 = 'assets/BuildOutput.csv'


root, ext = os.path.splitext(csv2)
output = root + '-new.csv'

with open(csv1) as r1, open(csv2) as r2, open(output, 'w', newline = '') as w:
    writer = csv.writer(w)
    merge_from = csv.reader(r1)
    merge_to = csv.reader(r2)

    for _ in range(0):
        next(merge_from)
    for merge_from_row, merge_to_row in zip(merge_from, merge_to):
        merge_to_row[3] = merge_from_row[1]
        writer.writerow(merge_to_row)
    print('complete')
        # merge_to_row.insert(1, merge_from_row[3]) -- inserts in row 1 all of row 3
        # del merge_to_row[5:8] -- deletes a range of rows