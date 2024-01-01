# run-time input in append mode

s=input("Enter some text:")
f=open("F:/a1.txt","a")
f.write(s + "\n")
f.close()

f=open("F:/a1.txt")
for i in f:
    print(i)