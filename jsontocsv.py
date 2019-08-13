import json
import csv

with open("data.json") as x:
    data = json.load(x)

print(data)
print(type(data))

with open('writetocsv.csv',"w", newline = "") as x :
    writer = csv.DictWriter(x, fieldnames =["nama","usia"])
    writer.writeheader()
    writer.writerows(data)

arr = []
with open("writetocsv.csv","r",newline = "") as x:
    reader = csv.DictReader(x)
    for i in reader:
        arr.append(dict(i))
    for item in arr:
        for key,val in item.items():
            try:
                item[key] = int(val)
            except ValueError:
                item[key] = val
print(arr)
