# csv File

import csv
with open("F:/f1.csv",'r') as file:
    reader = csv.reader(file)
    for i in reader:
        print(i)
