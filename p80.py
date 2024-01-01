# Exception HAndling
try:
    a = int(input("Enter First No :"))
    b = int(input("Enter Secong No:"))

    c = a / b

except Exception as E:
    print(E)
else:
    print("Ans is :", c)