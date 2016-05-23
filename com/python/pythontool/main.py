# coding=utf-8
import sys
from pql import MysqlTools
from sample import SampleAttribute
from pexcel import excel

host="127.0.0.1"
user="root"
passwd="liuyong"
db="testdb"
port=3306
if __name__=="__main__":
    #pql = MysqlTools.MysqlTools(host, user, passwd, db, port)
    # l = [3.0,2.0,3.0,5.0,6.0,7.0]
    # sampleAttribute = SampleAttribute.sample(l)
    #median = sampleAttribute.calMedian();
    # print(sampleAttribute.mean)
    # print(sampleAttribute.calVariance())
    # print(sampleAttribute.calCV())
    # print(sampleAttribute.Moment2())
    # print(sampleAttribute.Moment3())
    # print(sampleAttribute.Moment4())
    # print(sampleAttribute.calCenterMoment2())
    # print(sampleAttribute.calCenterMoment3())
    # print(sampleAttribute.calCenterMoment4())
    # print(sampleAttribute.calKurtosis())
    # print(sampleAttribute.calMedia())
    # column_name = ("username","passwd")
    # #values = (("test1","ss"),("test2","ss"))
    # #pql.insertIntoDB("user",column_name, values)
    # records = pql.selectFromDB("select * from user")
    # pql.insertIntoDBFromText("user", column_name,r"demo\\person.txt")
    content_list=[[1,2,3,4],[1,2,3,4],[1,2,3,4]]
    pexcel = excel.excel("D:\\test.xls","D:\\test.xls")
    #pexcel.createExcel("test",content_list)
    data = pexcel.readExcel("test1",3)
    print data