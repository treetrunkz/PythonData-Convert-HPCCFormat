# 1k-test-builder.py
# description: this file reads in two csv's, creating a rowlist array
# granularly assigning each CSV value iteratively to a new row
# producing a final CSV product ready to ingest.

import os
import csv
import json
import dUnder

rowlist = []
# pre
csv1 = 'OCK_INP.csv'
# q
csv2 = '1k.csv'
# r

root, ext = os.path.splitext(csv2)
output = root + '-new.csv'

with open(csv1) as r1, open(csv2) as r2, open(output, 'w', newline = '') as w:
    writer = csv.writer(w)
    merge_from = csv.reader(r1)
    merge_to = csv.reader(r2)
    for _ in range(0):
        next(merge_from)
    for q, r in zip(merge_from, merge_to):
        line = q[0], r[0], r[1], r[2], r[3], q[4], q[5], q[6], q[7], q[8], q[9], q[10], q[11], q[12], q[13], q[14], q[15], q[16]
        writer.writerow(line)


