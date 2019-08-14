import mysql.connector
import csv

table = input('Masukkan nama table : ')

data = []
with open('sqltocsv.csv',"r", newline= "") as x :
    reader = csv.DictReader(x)
    for i in reader:
        data.append(dict(i))
print(data)

keys = []
for loop in range(len(data)):
    for key in data[loop].keys():
        keys.append(key)
keyx = sorted(list(set(keys)))

kursor.execute('create table {}( {} varchar(50))'.format(table,keyx[0]))

for item in range(len(keyx)-1):
    kursor.execute('alter table {} add column {} varchar(50)'.format(table,keyx[item+1]))
    dbku.commit()

keys = []
vals = []
for key in data:
    keys.append(tuple(key.keys()))
for val in data:
    vals.append(tuple(val.values()))
for key,val in zip(keys,vals):
    querydb = f''' insert into {table} {str(key).replace("'",'')} values{str(val)[9:].replace(')','')}) '''
    kursor.execute(querydb)
    dbku.commit()
    print(kursor.rowcount, 'data terupdate!')
