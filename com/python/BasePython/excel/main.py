# -*- coding: utf-8 -*-
import xlrd
from pyExcelerator import *
column_num = 5 #正要处理的列数
row_sum = 0  #全局控制列数
def make_excel(input,sheet_name ,output):
    data = xlrd.open_workbook(input)
    w = Workbook()
    ws = w.add_sheet(sheet_name)     #创建一个工作表
    table = data.sheets()[0]
    nrows = table.nrows
    global row_sum
    for i in range(nrows):
        column = table.row_values(i)[0:11]
        for x in range(11):
            ws.write(row_sum,x,column[x])
        if i == 0 or column[column_num] == '':
            row_sum = row_sum + 1
            continue
        add_rows5 = column[5].split("\n")
        add_rows6 = column[6].split("\n")
        add_rows_len = len(add_rows5)
        row_sum = row_sum + 1

        for l in range(add_rows_len):

            for j in range(11):
                if j == 5:
                    ws.write(row_sum + l,j,add_rows5[l])
                if j == 6:
                    ws.write(row_sum + l,j,add_rows6[l])
        row_sum = row_sum + add_rows_len
    w.save(output)
if __name__=="__main__":
    make_excel('50.xlsx','随机处理','out.xls')