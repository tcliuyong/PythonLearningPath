# coding=utf-8
import MySQLdb
class MysqlTools(object):
    __host = "127.0.0.1"
    __user = "root"
    __passwd = ""
    __db = ""
    __port = 3306
    __conn = ""
    __cur = ""
    def __init__(self, host, user, passwd, db, port):
        self.__host = host
        self.__db = db
        self.__passwd = passwd
        self.__port = port
        self.__user = user
        try:
            self.__conn = MySQLdb.connect(host=self.__host,user=self.__user, passwd=self.__passwd, db=self.__db, port=self.__port,charset="UTF8")
            self.__cur = self.__conn.cursor()
        except MySQLdb.Error,e:
            print "Mysql Error %d: %s" % (e.args[0], e.args[1])
    def testConnect(self):
        try:
            self.__conn = MySQLdb.connect(host=self.__host,user=self.__user, passwd=self.__passwd, db=self.__db, port=self.__port)
            self.__cur = self.__conn.cursor()
            self.__cur.execute("show databases;")
            self.__cur.close()
            self.__conn.close()
            print "Connect successful"
        except MySQLdb.Error,e:
            print "Mysql Error %d: %s" % (e.args[0], e.args[1])
    def getConnection(self):
        try:
            self.__conn = MySQLdb.connect(host=self.__host,user=self.__user, passwd=self.__passwd, db=self.__db, port=self.__port)
            self.__cur = self.__conn.cursor()
        except MySQLdb.Error,e:
            print "Mysql Error %d: %s" % (e.args[0], e.args[1])
            self.__conn.close()
            self.__cur.close()
        return self.__conn, self.__cur
    def insertIntoDB(self,tableName, column_name, values):
        insertSql = "insert into " + tableName + str(column_name).replace("'","") + " values ("
        insertSql = insertSql + "%s," * len(column_name)
        insertSql = insertSql[0:len(insertSql) - 1]
        insertSql = insertSql + ")"
        self.__cur.execute("BEGIN")
        num = self.__cur.executemany(insertSql,values)
        self.__conn.commit()
        print str(num) + "条插入成功"
    def selectFromDB(self, sql):
        self.__cur.execute(sql)
        records = self.__cur.fetchall()
        return records
    def insertIntoDBFromText(self, table_name, column_name ,filepath, separator="\t"):
        f = open(filepath, "r")
        elements = []
        for line in f.readlines():
            element = line.split(separator)
            element[-1] = element[-1].strip()
            element = tuple(element)
            elements.append(element)
        elements = tuple(elements)
        self.insertIntoDB(table_name, column_name, elements)
    def __del__(self):
        self.__cur.close()
        print "游标关闭成功"
        self.__conn.close()
        print "连接关闭成功"