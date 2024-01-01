# dictionary in json

import json
s1 = {
    "Name":"Ruparel",
    "City":"Junagadh",
    "Mobile":7600044051
}
with open("data.json","w") as f1:
    json.dump(s1,f1)

with open("data.json","r") as f2:
    b = json.load(f2)
print(b)
