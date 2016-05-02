# coding=utf-8
import sys
import MysqlTools
host="127.0.0.1"
user="root"
passwd="liuyong"
db="testdb"
port=3306
if __name__=="__main__":
    pql = MysqlTools(host, user, passwd, db, port)
    column_name = ("username","passwd")
    #values = (("test1","ss"),("test2","ss"))
    #pql.insertIntoDB("user",column_name, values)
    records = pql.selectFromDB("select * from user")
    print records
    pql.insertIntoDBFromText("user", column_name,r"D:\\person.txt")
