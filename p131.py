#Create a Dictionary  and list file in json

import json
a = '{"Name":"Ruparel","City":"Junagadh","Mobile":7600044051,"Subject":["J2EE","Asp.net","Python","Project","Practical"]}'
p = json.loads(a)
print(json.dumps(p,indent=4,sort_keys=True))
