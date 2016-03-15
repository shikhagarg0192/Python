from __future__ import print_function
import MySQLdb as my

db = my.connect(host="localhost",
user="shikhagarg",
passwd="root",
db="world"
)

print(db)
cursor = db.cursor()
id1=7
operation="<"
print(cursor)
number_of_rows = cursor.execute("select * from city where id {} {}".format(operation,id1))
result = cursor.fetchall()
print(number_of_rows)
for row in result:
    print(row[0],row[1])
db.close()
