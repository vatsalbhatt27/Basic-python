# private specifier

class A:
    __name = 0
    __rno = 0
    __branch = 0
    def __init__(self,name,rno,branch):
        self.__name = name
        self.__rno = rno
        self.__branch = branch
    def __disp(self):
        print("Name is :",self.__name)
        print("Roll No is :",self.__rno)
        print("Branch is :",self.__branch)
    def access(self):
        self.__disp()

o1=A("MK",1,"Keshod")
o1.access()