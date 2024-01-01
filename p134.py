# database Select Record

import pymysql
con = pymysql.connect(host="localhost", user="root", password="", database="bca5")
c = con.cursor()
c.execute("select * from stud")
s1 = c.fetchall()
for i in s1:
    print(i)
c.close()
con.close()