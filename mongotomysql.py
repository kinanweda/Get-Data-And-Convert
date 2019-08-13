import pymongo
import mysql.connector

dbku = mysql.connector.connect(
    host =  '127.0.0.1',
    port = 3306,
    user = 'kinanweda',
    passwd = '12345',
    database = 'marvel'
)

# kursor = dbku.cursor()
# # kursor.execute('create database marvel')

x = pymongo.MongoClient('mongodb://localhost:27017')
db = x['marvel']
col = db['avengers']

data = list(col.find())

keys = []
for loop in range(len(data)):
    for key in data[loop].keys():
        keys.append(key)
keyx = sorted(list(set(keys)))

kursor.execute('create table avengers1( {} varchar(50))'.format(keyx[0]))

for item in range(len(keyx)-1):
    kursor.execute('alter table avengers1 add column {} varchar(50)'.format(keyx[item+1]))
    dbku.commit()

keys = []
vals = []
for key in data:
    keys.append(tuple(key.keys()))
for val in data:
    vals.append(tuple(val.values()))
for key,val in zip(keys,vals):
    querydb = f''' insert into avengers1 {str(key).replace("'",'')} values{str(val)[9:].replace(')','')}) '''
    kursor.execute(querydb)
    dbku.commit()
    print(kursor.rowcount, 'data terupdate!')
