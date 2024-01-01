# selection Sort Run-Time Input
a=[]
size=int(input("Enter size of List:"))
for i in range(size):
    no=int(input("Enter list Element :"))
    a.append(no)
print("Input Array::",a)
for i in range(len(a)):
    min_id=i
    for j in range(i+1,len(a)):
        if a[min_id]>a[j]:
            min_id=j
        a[i],a[min_id]=a[min_id],a[i]
print("Sorted Array:")
for i in range(len(a)):
    print("%d :"%(a[i]))