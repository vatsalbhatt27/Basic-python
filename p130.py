#Create a Dictionary  and list file in json

import json
a = ["Ruparel","Python",(10,32.9,80),{"City":"Junagadh"}]
b = json.dumps(a)
c = json.loads(b)
print(c)

