# Databse Update Record

import pymysql
name = input("Enter Any Name::")
con = pymysql.connect(host="localhost", user="root", password="", database="bca5")
c = con.cursor()
sql = "update stud set name='%s' where name='ccc'" %(name)
c.execute(sql)
con.commit()
print(c.rowcount,"Row Update...")
c.close()
con.close()