
import csv
csv.register_dialect("bca5",delimiter="|",quoting=csv.QUOTE_NONE)
with open("F:/bca5.csv",'r') as file:
    r1 = csv.reader(file,dialect="bca5")
    for i in r1:
        print(i)