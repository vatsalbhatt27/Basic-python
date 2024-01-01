# Linear Search

l1=[4,2,3,5,9]
no=int(input("Enter Searching Number : "))
found=False
for i in range(len(l1)):
    if l1[i]==no:
        found=True
        print("%d is Found at  Position %d"%(no,i))
        break
if found==False:
    print("%d is not Found in List"%no)
