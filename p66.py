# list using loop

l1=[10,20,30,40]
print("printing original list")

for i in l1:
    print(i)
l1.remove(30)
print("New List is :")

for i in l1:
    print(i)