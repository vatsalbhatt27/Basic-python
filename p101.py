#Abstract class

from abc import ABC
class a1(ABC):
    def a1(self):
        print("Abstract Base Class")
class a2(a1):
    def a1(self):
        super().a1()
        print("Sub Class")
o1=a2()
o1.a1()