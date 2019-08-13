import pymongo
import csv

x = pymongo.MongoClient('mongodb://localhost:27017')
db = x['marvel']
col = db['avengers']

data = list(col.find())

keys = []
for loop in range(len(data)):
    for key in data[loop].keys():
        keys.append(key)
kolom = sorted(list(set(keys)))

with open('mongotocsv.csv','w', newline = '') as x :
    writer = csv.DictWriter(x, fieldnames = kolom)
    writer.writeheader()
    writer.writerows(data)
