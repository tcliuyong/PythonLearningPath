# -*- coding: utf-8 -*-
from xlrd import open_workbook
from pyExcelerator import *
class excel:
    __input = ""
    __output = ""
    def __init__(self, input, output):
        self.__input = input
        self.__output = output
    def createExcel(self,sheet_name,content_list):
        w = Workbook()
        ws = w.add_sheet(sheet_name)
        for i in range(len(content_list)):
            for j in range(len(content_list[i])):
                ws.write(i,j,content_list[i][j])
        w.save(self.__output)
        print "create "+ self.__output + " complete!"
    def readExcel(self,sheel_name,column_num):
        data = open_workbook(self.__input)
        table = data.sheets()
        content_list= []
        content_element = []
        print len(table)
        for sname in  data.sheet_names():
            if(sname == sheel_name):
                content =  data.sheet_by_name(sname)
                nrows = content.nrows
                for i in range(nrows):
                    column = content.row_values(i)[0:column_num]
                    content_list.append(column)
                    del column
        return content_list

