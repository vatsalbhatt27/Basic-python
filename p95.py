# method Overloading using if else

class a1:
    def add(self,a=0,b=0,c=0):
        if a!=0 and b!=0 and c!=0:
            return a+b+c
        elif a!=0 and b!=0:
            return a+b
        else:
            return 0
o1=a1()
print("Sum is :",o1.add())
print("Sum is :",o1.add(10,20))
print("Sum is :",o1.add(10,20,30))