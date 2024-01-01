# method Overloading

class a1:
    def add(self,a,b):
        return a+b
    def add(self,a,b,c):
        return a+b+c
o1=a1()
print("Sum is :",o1.add(10,20,30))
#print("Sum is :",o1.add(20,30)) #error