#bubble Short

def bubble_sort(sort_list):
    for i in range(len(sort_list)):
        for j in range(len(sort_list)-1):
            if sort_list[j] > sort_list[j+1]:
                sort_list[j],sort_list[j+1] = sort_list[j+1],sort_list[j]
                print(sort_list)
lst=[]
size = int(input("Enter Size :"))
for i in range(size):
    no= int(input("Enter Elements :"))
    lst.append(no)
bubble_sort(lst)