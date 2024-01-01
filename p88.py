# inheritance class

class a1:
    def s1(self):
        print("MAin Class")
class a2(a1):
    def s2(self):
        print("Sub Class")
o1=a2()
o1.s1()
o1.s2()