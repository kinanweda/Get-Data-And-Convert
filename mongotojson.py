import pymongo
import json

x = pymongo.MongoClient('mongodb://localhost:27017')
db = x['marvel']
col = db['avengers']

data = list(col.find())
print(data)

listkey=[]
for loop in range(len(data)):
    for key in data[loop].keys():
        if key == '_id':
            listkey.append(key)
            listkey.pop(-1)
        else:
            listkey.append(key)
print(listkey)
keys = sorted(list(set(listkey)))
print(keys)

a = [tuple(item.values()) for item in data]
vals = []
for item in range(len(a)):
    vals.append(a[item][1:])
print(vals)

dicts = [{key:val for key,val in zip(keys,vals[item])} for item in range(len(vals))]
print(dicts)

with open("mongotojson.json","w") as x :
    json.dumps(dicts,indent=2)
