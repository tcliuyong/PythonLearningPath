import MySQLdb
import sys,os
if __name__=="__main__":
    try:
        conn = MySQLdb.connect(host="localhost",user="root",passwd="liuyong", db="test")
    except Exception,e:
        print e
        sys.exit()
    cursor = conn.cursor()
    sql = "insert into user1(username, age) VALUES (%s, %s)"
    value = (("test1",1),("test1",2))
    try:
        cursor.executemany(sql, value)
    except Exception,e:
        print e
    sql = "select * from user1"
    cursor.execute(sql)
    data = cursor.fetchall()
    if data:
        for x in data:
            print x[0], x[1]
    cursor.close()
    conn.close()


