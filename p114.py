# regular Expression Start Function

import re
t1 = "The rain in Spain"
x = re.findall("in", t1)
print(x)
x = re.search("\s", t1)
print("The First White-Space Character is located in Position",x.start())