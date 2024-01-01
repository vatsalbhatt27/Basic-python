#All Arithmetic Calculation
no1 = int(input("Enter 1 st Number :"))
no2 = int(input("Enter 2 nd Number :"))
ch = int(input("Enter  Your Choise :"))

if ch == 1:
	c = no1 + no2
	print("Sum of  Two Number is :",c)
elif ch == 2:
	c = no1 - no2
	print("Sub of Two Number is :",c)
elif ch == 3:
	c = no1 * no2
	print("Multi of Two Number is :",c)
elif ch == 4:
	c = no1 /  no2
	print("Division  of Two Number is :",c)
else :
	print("Wrong Choise ")
