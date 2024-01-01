# exception handling in For Loop

import sys
a1=['a',0,2]
for i in a1:
    try:
        print("List of Values :",i)
        ans=1/int(i)
        break
    except:
        print("Exception :",sys)
        print("Next Entery")
print("Ans :",i,"is",ans)