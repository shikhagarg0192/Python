from __future__ import print_function

import MySQLdb as my
try:
    db = my.connect(host="localhost",
                    user="shikhagarg",
                    passwd="root",
                    db="world")
    
    cursor = db.cursor()
    name = "newcity"
    cc = 'SNC'
    district = 'someyork'
    pop = 2232422
    
    data = [
        ('city1','MAC','dis1',23421),
        ('city2','sdf','dis2',23422),
        ('city3','sad','dis3',23424),
        ('city4','sdw','dis4',23423)]
    
    sql = "insert into city(name,countrycode,district,population)\
    values(%s,%s,%s,%s)"
    
    num = cursor.executemany(sql,data)
    db.commit()
    db.close()

except my.Error as e:
    print(e)
except :
    print("Unknown error occured")
