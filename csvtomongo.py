import pymongo
import csv

x = pymongo.MongoClient('mongodb://localhost:27017')
database = input('Masukkan nama Database : ')
db = x[database]
collection = input('Masukkan nama Collection : ')
col = db[collection]

data = []
with open('mongotocsv.csv',"r", newline= "") as x :
    reader = csv.DictReader(x)
    for i in reader:
        data.append(dict(i))
keys = []
for loop in range(len(data)):
    for key in data[loop].keys():
        keys.append(key)
kolom = sorted(list(set(keys)))

y = col.insert(data)
print(len(y), 'udah terupdate!')
