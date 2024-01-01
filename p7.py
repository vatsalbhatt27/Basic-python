#Enter 3 sub marks and total, per print it
sub1 =int(input("Enter 1 st sub Marks :"))
sub2 =int(input("Enter 2 nd sub Marks :"))
sub3 =int(input("Enter 3 rd sub Marks :"))
sub4 =int(input("Enter 4 th sub Marks :"))
sub5 =int(input("Enter 5 th sub Marks :"))

total = sub1   + sub2 + sub3 + sub4 + sub5
per = total/5

if per >=70:
	print("Distination")
elif per >=60:
	print("1 st Class ")
elif per >=50:
	print("2 nd Class ")
elif per >=40:
	print("3 rd Class ")
else:
	print("Fail")