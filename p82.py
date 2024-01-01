# Define User Exception
try:
    a=10/0
except(ArithmeticError,IOError):
    print("Airthmetic Exception")
else:
    print("Succefully Done")