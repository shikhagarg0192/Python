from __future__ import print_function

import MySQLdb as my
db = my.connect(host="localhost",
                user="shikhagarg",
                passwd="root",
                db="world")
cursor = db.cursor()
print(cursor)
sql = "select * from city"
num = cursor.execute(sql)
while True:
    row=cursor.fetchone()
    if row==None:
        break
    print(row)

cursor = db.cursor()
num=cursor.execute(sql)
print(cursor.fetchmany(3))

db.close()
