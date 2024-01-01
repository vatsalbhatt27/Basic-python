# rename and remove file

import os
if os.path.exists("F:/abc.txt"):
    os.remove("F:/abc.txt")
else:
    print("File not found")