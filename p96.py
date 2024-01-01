#Acces Specifier

class A:
    def fun(self):
        print("Public Funaction")
    def __fun(self):
        print("Private Function")
    def help(self):
        self.fun()
        self.__fun()
o1=A()
o1.help()