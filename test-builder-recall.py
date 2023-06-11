# 10k-test-builder.py
# Ellie S. Carl 
# 9/10/2022
# Description: AccurInt Python Batch Ingestion Creator

import csv
import json
import os
import xmltodict
import pandas as pd
from csv import reader
from csv import writer
import sys
import csv
import ctypes as ct
import datetime
import os

# Increase the maximum field limit(191704310)
maxInt = sys.maxsize
while True:
    # decrease the maxInt value by factor 10 
    # when the OverflowError occurs.
    try:
        csv.field_size_limit(maxInt)
        break
    except OverflowError:
        maxInt = int(maxInt/2)
"v{:d}.{:d}.{:d}".format(*sys.version_info[:3]), sys.platform, sys.maxsize, ct.sizeof(ct.c_void_p) * 8, ct.sizeof(ct.c_long) * 8
('v3.8.10', 'linux', 9223372036854775807, 64, 64)
csv.field_size_limit(int(ct.c_ulong(-1).value // 2))


# "FIXED-PREDATA"
# Creates two separate files one CSV the other JSON
# From the XML Conversion process we create enumerated object properties
# Replaces un-normalized data with our OCK Account Data from svc
# ==================================
xmldata = fidget = rowlist = []


x = datetime.datetime.now()

yr = x.strftime("%Y")
mt = x.strftime("%m")
dy = x.strftime("%d")
tm = x.strftime("%f")

account_time = yr + mt + dy + tm
account_number = input("Enter Customer Number: (6 digits only)")

if(len(account_number) != 6):
    print("\n**** ERROR: Customer Number must be 6 digits.******\n")
    sys.exit()

amount = input("Enter desired testfile size: (input as text: 1k, 10k, 100k, 1m, 10m, 40m)")
file_name = account_number + "ABC" + "_" + account_number + "_SFTP_ID_TD_Recall_" + account_time + ".csv"
csv1 = 'assets/utilities/csv/' + amount + '-fixed.csv'
# vin is 3
# q
csv2 = 'assets/utilities/csv/' + amount + 'fixed.csv'
# vin is 0
    # r

# print("pulling data from: " + csv1)
rowcount = 0
number = 0
for row in open(csv1):
    rowcount+=1
# print("Row Count: ", rowcount)
loopcount = rowcount/10000

# print("Number of iterations of Vehicle Specific Data: ", loopcount)

if(loopcount == 0.1):
    csv2 = 'assets/utilities/csv/1kfixed.csv'
csv1 = csv1    

f_data = open('assets/utilities/csv/1kfixed.csv','r').read()
counter = 0
with open('assets/utilities/csv/fixed.csv', 'w') as g:
    for x in range((int(loopcount))):
        counter+=1
        g.write(f_data)
if(loopcount == 0.1):
    with open('assets/utilities/csv/fixed.csv', 'w') as g:
        print("TESTED")
        g.write(f_data)

fixed_data = open('assets/utilities/csv/fixed.csv','r')

root, ext = os.path.splitext(csv2)
output = root + '-predata-recall.csv'

with open(csv1) as r1, open(csv2) as r2, open(output, 'w', newline = '') as w:
    writer = csv.writer(w)
    merge_from = csv.reader(r1, delimiter="|")
    merge_to = csv.reader(r2)
    for _ in range(0):
        next(merge_from)
    for q, r in zip(merge_from, merge_to):
        # line = q[0] + "||||", q[1] + "|", q[3] + "|", r[1] + "|", r[3]+ "|", q[5]+ "|", q[6]+ "|", q[7]+ "|", q[8]+ "|", q[9]+ "|", q[10]+ "|", q[11]+ "|", q[12]+ "|", q[13]+ "|", q[14]+ "||" + q[16] + '|' + '|'
        #        rt             vin         make        model       year       first      last       middle     suffix     address     city       state       zipcode     zipcode2    phone         email             then buildsheet
        #      rt              vin        first       last        middle     suffix     street      city        state       zipcode1    zipcode2    phone1      phone2      email >>EOL      
        line = q[0] + "||||", q[1] + "|", q[5] + "|", q[6] + "|", q[7]+ "|", q[8]+ "|", q[10]+ "|", q[10]+ "|", q[11]+ "|", q[12]+ "|", q[13]+ "|", q[14]+ "|", q[15]+ "||", q[16]
        line = ''.join([i for i in line]).replace(',', '')
        recall = line[1:-1]
        writer.writerow(recall)


gf = csv.reader(fixed_data)
testnum = 0
for row in gf:
    xmldata.append(row)
    testnum+=1

fixed_data.close()

def convert_row(xmldata):
    return """  <buildsheet>
        <manufacturer>%s</manufacturer>
        <vin>%s</vin>
        <make>%s</make>
        <model>%s</model>
        <year>%s</year>
        <odometer>%s</odometer>
        <trim>%s</trim>
        <interiorColor>%s</interiorColor>
        <exteriorColor>%s</exteriorColor>
        <warranty>%s</warranty>
        <vehicleLease>%s</vehicleLease>
        <vehicleFleet>%s</vehicleFleet>
        <vehicleCpo>%s</vehicleCpo>
        <connectedServices>%s</connectedServices>
        <activeRecall>%s</activeRecall>
        <serviceHistory>%s</serviceHistory>
        <type>FuelType</type>
        <items>
            <type>String</type>
                <enum>%s</enum>
        </items>
    </buildsheet>""" % (xmldata[1], xmldata[0], xmldata[1], xmldata[2], xmldata[3], xmldata[4], xmldata[5], xmldata[6], xmldata[6], xmldata[7], xmldata[8], xmldata[8], xmldata[8], xmldata[9], xmldata[10], xmldata[11], xmldata[13])



# FIXED-POSTDATA
# ==============================


# Removing Header and Footer Data from XML File for Dictionary Parsing
with open('assets/utilities/xml/test.xml', 'w') as xml:
    xml.write('<root>\n')
    xml.write('\n'.join([convert_row(row) for row in xmldata[0:]]))
    xml.write('\n</root>')

# XML to Dictionary (JSON structuring) using xmltodict Import
with open('assets/utilities/xml/test.xml') as xml_file:
    data_dict = xmltodict.parse(xml_file.read())
xml_file.close()
json_data = json.dumps(data_dict)
# print(json_data)
# CSV Data parse to XML
# Synthetically Adding Enumerator
# Translating XML Output to JSON Objects...
with open('assets/utilities/json/data.json', 'w', newline='') as json_file:
    json_file.write(json_data)
json_file.close()
with open('assets/utilities/csv/data_composition.csv', 'w') as csv_file:
    csv_file.write(json_data[25:][:-3].replace("}, {", "},\n{", 5000000))
csv_file.close()

csv3 = 'assets/utilities/csv/data_composition.csv'
csv4 = 'assets/utilities/csv/' + amount + 'fixed-predata.csv'

root, ext = os.path.splitext(csv4)
output = root + '-recall.csv'

# Zipping Newly Structured Data By Line
with open(csv3) as r1, open(csv4) as r2, open(output, 'w', newline='') as w:
    writer = csv.writer(w)
    merge_from = csv.reader(r1, delimiter  = '\n')
    merge_to = csv.reader(r2, delimiter= '\n')
    for _ in range(0):
        next(merge_from)
    for q, r in zip(merge_from, merge_to):
        r = [item.replace(',','').replace('"','').replace('|',',').replace('"','') for item in r]
        line = r
        writer.writerow(line)

r1.close(), r2.close()

# Inserting New Line At Every New Object
# JSON Object Saved As CSV, Now Parsable Row-wise
with open('assets/utilities/csv/data_composition.csv', 'w') as csv_file:
    csv_file.write(json_data[25:][:-3].replace("}, {", "}, \n{", 500000))
csv_file.close()

# Remove all junk from text
text = open(output, 'r')
text = ''.join([i for i in text]).replace('"""', '"')
text = ''.join([i for i in text]).replace('""', '"')
text = ''.join([i for i in text]).replace('"{', '{')
text = ''.join([i for i in text]).replace('},"', '}').replace('|,{','| {').replace('}}"','}}')
text = text.replace('""', '"')
# Writelines into Output
x = open("output.csv", "w")
x.writelines("001,"+ account_number + ",,generated\n")
x.writelines(text.replace('"',''))
x.writelines("003,"+ str(len(text)))
# print(output)
write_file = open(file_name, "w")
write_file.writelines("001,"+ account_number + ",,generated\n")
write_file.writelines(text.replace('"',''))
write_file.writelines("003,"+ amount.rstrip(amount[-1]) + "000")
x.close()
print(file_name)

write_file.close()