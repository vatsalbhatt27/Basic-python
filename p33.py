#udf with arg no return value

def sum(a,b):
    c = a+b
    print("Sum of Two Number is :",c)

a = int(input("Enter First Number :"))
b = int(input("Enter Second Number :"))

sum(a,b)