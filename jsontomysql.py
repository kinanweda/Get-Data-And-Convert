import json
import mysql.connector

with open("sqltojson.json") as x:
    data = json.load(x)

table = input('Masukkan nama table : ')
kursor = dbku.cursor()
data = []
with open('sqltocsv.csv',"r", newline= "") as x :
    reader = csv.DictReader(x)
    for i in reader:
        data.append(dict(i))
print(data)

key = []
for loop in range(len(data)):
    for keya in data[loop].keys():
        key.append(keya)
keyx = sorted(list(set(key)))
print(keyx)

kursor.execute('create table {}( {} varchar(50))'.format(table,keyx[0]))

for item in range(len(keyx)-1):
    kursor.execute('alter table {} add column {} varchar(50)'.format(table,keyx[item+1]))
    dbku.commit()

keys = []
vals = []
for key in data:
    print(key)
    keys.append(tuple(key.keys()))
for val in data:
    vals.append(tuple(val.values()))
for key,val in zip(keys,vals):
    querydb = f''' insert into {table} {str(key).replace("'",'')} values {val} '''
    kursor.execute(querydb)
    dbku.commit()
    print(kursor.rowcount, 'data terupdate!')
