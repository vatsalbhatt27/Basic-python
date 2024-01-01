# write mode

f=open("F:/a1.txt","w")
f.write("Bca sem-5")
f.close()

f=open("F:/a1.txt")
for i in f:
    print(i)