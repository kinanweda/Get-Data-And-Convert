import json
import pymongo

x = pymongo.MongoClient('mongodb://localhost:27017')
database = input('Masukkan nama Database : ')
db = x[database]
collection = input('Masukkan nama Collection : ')
col = db[collection]

with open("mongotojson.json") as x:
    data = json.load(x)

y = col.insert_many(data)
