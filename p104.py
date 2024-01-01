# Binary Search

def binary_search(sort_list,length,key):
    start=0
    end=length-1
    while start <= end:
        mid = int(start + end/2)
        if key==sort_list[mid]:
            print("Entered Number %d is Present at Position %d"%(key,mid))
            return -1
        elif key < sort_list[mid]:
            end = mid-1
        elif key > sort_list[mid]:
            start = mid+1
        else:
            print("Element is Not Found ")

l1=[]
size=int(input("Enter size of List:"))
for i in range(size):
    no=int(input("Enter list Element :"))
    l1.append(no)
l1.sort()
ch=int(input("Enter Number to be Search :"))
binary_search(l1,size,ch)