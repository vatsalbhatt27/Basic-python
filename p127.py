#json

import json
a = (10, 20, 30, 40, 50)
print(type(a))
b = json.dumps(a)
print(b)
print(type(b))
print(type(json.loads(b)))
