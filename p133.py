# Database Insert Record

import pymysql
rno = int(input("Enter Any Number::"))
name = input("Enter Name::")
city = input("Enter City::")
mo = input("Enter Mobile Number::")

con = pymysql.connect(host="localhost", user="root", password="", database="bca5")
c = con.cursor()

str="insert into stud values(%d, '%s', '%s', '%s')"%(rno, name, city, mo)

ans = c.execute(str)
if(ans > 0):
    con.commit()
    print("1 Row Inserted....")
else:
    print("Error")
c.close()
con.close()