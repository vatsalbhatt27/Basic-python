
import html
from prettytable import PrettyTable
a = open("F:/s1.csv",'r')
a = a.readlines()
l1 = a[0]
l1 = l1.split(',')
t = PrettyTable([l1[0],l1[1]])
for i in range(1,len(a)):
    t.add_row(a[i].split(','))
c=t.get_html_string()
h1=open('table.html','w')
h1=h1.write(c)