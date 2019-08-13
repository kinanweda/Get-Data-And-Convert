import json
import csv

with open("data.json") as x:
    data = json.load(x)

print(data)
print(type(data))

keys=[]
for item in range(len(data)):
    for i in data[item].keys():
        keys.append(i)

kolom= sorted(list(set(keys)))

with open('writetocsv.csv',"w", newline = "") as x :
    writer = csv.DictWriter(x, fieldnames = kolom)
    writer.writeheader()
    writer.writerows(data)
