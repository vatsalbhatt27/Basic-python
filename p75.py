# declare same key

d1={1:"J2EE",2:"Asp.net",3:"Python",2:"Practical"}
print(d1)
d2=d1.copy()
print(d2)

#d1.clear()
#print(d1)
print(d2.get(1))
print(d2.items())
print(d2.values())
print(d2.keys())
print(d1)

#d2.pop(2)
#print(d1)

#d1.popitem()
#print(d1)

d1.update({3:"Basic Python"})
print(d1)