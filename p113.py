# regular Expression  Serch method

import re
t1 = "The rain in Spain"
x = re.search("Spain$", t1)
if x:
    print("Yes! We Have a match")
else:
    print("No Match")


