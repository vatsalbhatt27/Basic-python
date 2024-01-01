#insert sort

def insert_sort(arr):
    for i in range(1,len(arr)):
        key =arr[i]
        j =i - 1
        while j>=0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -=1
        arr[j+1]=key
arr=[12,13,11,5,6]
print(arr)
insert_sort(arr)
for i in range(len(arr)):
    print("%d" %arr[i])