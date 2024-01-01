# method Overloading using if else

class Computer:
    def area(self,x=None,y=None):
        if x!=None and y!=None:
            return x+y
        elif x!=None:
            return x*x
        else:
            return 0
o1=Computer()
print("Area Value :",o1.area())
print("Area Value :",o1.area(4))
print("Area Value :",o1.area(4,5))