#Dict Reader Method
import csv
with open("F:/f1.csv",'r') as file:
    r = csv.DictReader(file)
    for i in r:
        print(dict(i))
