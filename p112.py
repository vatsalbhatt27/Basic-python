# Regular Expression

import re
"""s1 = "201, @@@ Ruparel Education 7600044051"
print(s1)
r = re.compile('[a-f]')
print(r.findall(s1))
r = re.compile("\d")
print(r.findall(s1))
r = re.compile("\d+")
print(r.findall(s1))
r = re.compile("\w")
print(r.findall(s1))
r = re.compile("\w+")
print(r.findall(s1))
r = re.compile("\W")
print(r.findall(s1))
r = re.compile("\W+")
print(r.findall(s1))
r = re.compile("\s")
print(r.findall(s1))
s1 = "Ruparel Education Pvt. Ltd. RUPAREL EDUCATION PVT LTD"
r = re.compile("[a-f]",flags=re.IGNORECASE)
print(r.findall(s1))
r = re.compile("[a-f]+",flags=re.IGNORECASE)
print(r.findall(s1))"""
s1 = "Box A contains 3 red and 5 white balls, Box B contains 4 red and 2 blue balls"
print(s1)
r = re.sub(r'\d',"@",s1)
print(r)

