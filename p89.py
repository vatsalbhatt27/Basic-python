# multiple inheritance

class a1:
    def s1(self):
        print("MAin Class")
class a2(a1):
    def s2(self):
        print("Sub Class")
class a3(a2):
    def s3(self):
        print("Class A3")
o1=a3()
o1.s1()
o1.s2()
o1.s3()