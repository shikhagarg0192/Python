from __future__ import print_function

import MySQLdb as my
try:
    db = my.connect(host="localhost",
                user="shikhagarg",
                passwd="root",
                db="world")
    cursor= db.cursor()
    sql = "select * from city"
    num=cursor.execute(sql)
    print(num)
    db.close()

except my.DataError as e:
    print("Data error")
    print(e)
except my.InternalError as e:
    print("Internal error")
    print(e)
except my.IntegrityError as e:
    print("Integrity error")
    print(e)
except my.OperationalError as e:
    print("Operational error")
    print(e)
except my.NotSupportedError as e:
    print("Not supported error")
    print(e)
except my.ProgrammingError as e:
    print("Programming error")
    print(e)
except :
    print("Unknown error occured")
