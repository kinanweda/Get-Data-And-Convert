import mysql.connector
import json

dbku = mysql.connector.connect(
    host =  '127.0.0.1',
    port = 3306,
    user = 'kinanweda',
    passwd = '12345',
    database = 'doraemon' 
)

kursor = dbku.cursor()
describe = ' describe karakter '
kursor.execute(describe)
listsdc = kursor.fetchall()

kursor = dbku.cursor()
querydb = ''' select * from karakter'''

kursor.execute(querydb)
lists = kursor.fetchall()

keys = []
vals = []
for item in range(1,len(listsdc)):
    keys.append(listsdc[item][0])
for item1 in range(len(lists)):
    vals.append(lists[item1][1:])
dicts = [{key:val for key,val in zip(keys,vals[item])} for item in range(len(vals))]
print(dicts)

with open("sqltojson.json","w") as x :
  x.write(str(dicts).replace("'",'"'))
