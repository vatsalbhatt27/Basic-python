# run-time input in write mode

s=input("Enter some text:")
f=open("F:/a1.txt","w")
f.write(s)
f.close()

f=open("F:/a1.txt")
for i in f:
    print(i)