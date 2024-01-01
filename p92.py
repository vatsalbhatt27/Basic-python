# method Overriding

class BOB:
    def rate(self):
        return 10
class SBI:
    def rate(self):
        return 7
class ICICI:
    def rate(self):
        return 8
b1=BOB()
b2=SBI()
b3=ICICI()

print("BOB Rate of Intrest is :",b1.rate())
print("SBI Rate of Intrest is :",b2.rate())
print("ICICI Rate of Intrest is :",b3.rate())