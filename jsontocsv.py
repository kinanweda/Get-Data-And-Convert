import csv
import json

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

with open('writetojson.json', "w") as x:
    x.write(json.dumps(arr, indent = 2))
