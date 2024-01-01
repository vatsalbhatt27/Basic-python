# csv File Using delimater

import csv
with open("F:/f1.csv",'r') as file:
    reader = csv.reader(file,delimiter="\t")
    for i in reader:
        print(i)
