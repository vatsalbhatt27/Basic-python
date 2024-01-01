#sets
a ={10,20,30,40,1,2}
b={1,2,3,4,0}

print(a)
print(b)
print(type(a))
print(type(b))

print(a&b)
print(a | b)
print(a-b)
print(b-a)
x=a.difference(b)
print(x)
x=a.union(b)
print(x)
x=a.intersection(b)
print(x)