# Regular Expression MULTILINE Keyword

import re
a = """Ruparel Education Pvt. Ltd.
201, Punit Shopping Center
M.G. Road
Junagadh"""
k1 = re.findall(r"\w",a)
print(k1)
k2 = re.findall(r"\w+",a,re.MULTILINE)
print(k2)
