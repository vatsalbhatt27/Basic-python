# Databse Delete Record

import pymysql
name = input("Enter Any Name::")
con = pymysql.connect(host="localhost", user="root", password="", database="bca5")
c = con.cursor()
sql = "delete from stud where name='%s'" %(name)
c.execute(sql)
con.commit()
print(c.rowcount,"Row Deleted...")
c.close()
con.close()