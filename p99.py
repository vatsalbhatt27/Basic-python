# private specifier

class student:
    __name = 0
    __rno = 0
    __branch = 0
    def __init__(self,name,rno,branch):
        self.__name = name
        self.__rno = rno
        self.__branch = branch
    def _disp(self):
        print("Name is :",self.__name)
        print("Roll No is :",self.__rno)
        print("Branch is :",self.__branch)
class stud(student):
    def disp(self):
        self._disp()

o1=stud("MK",1,"Keshod")
o1.disp()