# Regular Expresssion split Function

import re
t1 = "The rain in Spain"
x = re.split("\S",t1)
print(x)
x = re.split("\s",t1)
print(x)