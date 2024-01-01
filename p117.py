# Regular Expression Span() and group() Function

import re
s1 = "How are you, How is everything"
x = re.search("How", s1)
print(x)
print(x.span())
print(x.group())
print(x.string)
