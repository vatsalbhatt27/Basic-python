#udf with arg with return value

def sum():
    c = a+b
    return c
a=int(input("Enter First Number :"))
b=int(input("Enter Second Number :"))

ans=sum()
print("Sum of Two Number is :",ans)