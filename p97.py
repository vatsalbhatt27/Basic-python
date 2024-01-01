#protected Specifier

class A:
    _name="MK"
    _rno=1
    def disp(self):
        print("Name is :",self._name)
        print("Roll No is :",self._rno)
o1=A()
o1.disp()