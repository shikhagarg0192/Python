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
print(cursor.fetchone())
db.close()
