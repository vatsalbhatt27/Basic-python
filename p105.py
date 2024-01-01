# selection Sort

a=[10,5,40,30,8,3,4]
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