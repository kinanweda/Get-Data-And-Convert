import pymongo
import mysql.connector

dbku = mysql.connector.connect(
    host =  '127.0.0.1',
    port = 3306,
    user = 'kinanweda',
    passwd = '12345',
    database = 'doraemon' 
)

x = pymongo.MongoClient('mongodb://localhost:27017')
database = input('Masukkan nama Database : ')
db = x[database]
collection = input('Masukkan nama Collection : ')
col = db[collection]

kursor = dbku.cursor()

describe = ' describe avengers '
kursor.execute(describe)
listsdc = kursor.fetchall()

querydb = ''' select * from avengers'''
kursor.execute(querydb)
listquery = kursor.fetchall()
keys = []
vals = []
for item in range(1,len(listsdc)):
    keys.append(listsdc[item][0])
for item1 in range(len(listquery)):
    vals.append(listquery[item1][1:])
dicts = [{key:val for key,val in zip(keys,vals[item])} for item in range(len(vals))]
print(dicts)

y = col.insert(dicts)
print(len(y), 'udah terupdate!')
