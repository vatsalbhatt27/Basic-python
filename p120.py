# Regular Expression

import re
t1 = "The rain in Spain"
a1 = 'rupareleducation@gmail.com'
a1 = 'rupareleducation'
emails = re.findall(r'[\w\.-]+@[\w\.-]+',a1)
for i in emails:
    print(i)
print("\'")
print("\"")
print("\f")
print("\a")
print("A\nB")
print("A\tB")
print("\\")
x = re.findall("Spain\Z", t1)
print(x)

txt = "201, Punit Shopping Center 7600044051"
x = re.findall("[a-zA-Z]",txt)
print(x)
