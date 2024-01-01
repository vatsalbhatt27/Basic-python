#Abstract base class

from abc import ABC
class bca(ABC):
    def sem(self):
        pass
class sem1(bca):
    def sem(self):
        print("BCA sem-1")
class sem2(bca):
    def sem(self):
        print("BCA sem-1")
class sem3(bca):
    def sem(self):
        print("BCA sem-3")
o1=sem1()
o1.sem()
o1=sem2()
o1.sem()
o1=sem3()
o1.sem()