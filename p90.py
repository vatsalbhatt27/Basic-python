# class method

class Calc1:
    def sum(self,a,b):
        return a+b
class Calc2:
    def mul(self,a,b):
        return a*b
class Calc3(Calc1,Calc2):
    def div(self,a,b):
        return a/b
d=Calc3()
print("Sum of Two NO is :",d.sum(10,20))
print("Multi of Two No is :",d.mul(10,20))
print("Div of Two No is :",d.div(10,20))