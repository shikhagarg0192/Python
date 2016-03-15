from __future__ import print_function

import MySQLdb as my
db = my.connect(host="localhost",
                user="shikhagarg",
                passwd="root",
                db="world")
cursor = db.cursor()
print(cursor)
city = "%dam%"

sql = "select * from city where name like '{}'".format(city)
number_of_rows = cursor.execute(sql)
result = cursor.fetchall()
for row in result:
    print(row[0],row[1])
db.close()
