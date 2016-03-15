from __future__ import print_function

import MySQLdb as my
db = my.connect(host="localhost",
                user="shikhagarg",
                passwd="root",
                db="world")

cursor=db.cursor()
sql="insert into city values(null,'Mars city','MAC','MARC',1233)"

num = cursor.execute(sql)
db.commit()
db.close()
