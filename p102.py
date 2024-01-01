class emp:
    name="MK"
    salary=10000

    def show(self):
        print("Name is :",self.name)
        print("Salary is :",self.salary)
e1=emp()

print(getattr(e1,"name"))
print(hasattr(e1,"City"))
print(setattr(e1,"Height",1555))
print(getattr(e1,"Height"))
print(getattr(e1,"salary"))
#print(delattr(emp,"Salary"))
