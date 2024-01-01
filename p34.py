#udf no arg with return value

def sum():
    a=int(input("Enter First Number :"))
    b=int(input("Enter Second Number :"))

    c = a+b
    return c
ans=sum()
print("Sum of Two Number is :",ans)