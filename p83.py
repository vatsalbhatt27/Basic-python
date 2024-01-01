# Multiple Exception and File Open mode

try :
    f=open("f:/a2.txt")
except(ArithmeticError):
    print("Airthmetic Exception")
except(IOError):
    print("File Not Found Exception")
else:
    print("Successfully Done")