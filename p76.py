# dictionary using loop

d1={"Name":"Ruparel","Subject":"J2EE","Year":"2020"}
print(d1)

for i in d1:
    print(i)
for i in d1.values():
    print(i)

print("Keys","\t"," Values")
for i,j in d1.items():
    print(i,"\t",j)
    print(i,j,end=" ")
    print()