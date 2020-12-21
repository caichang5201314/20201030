# -*- coding: utf-8 -*-
from xlrd import open_workbook

bk = open_workbook(r'd:\emp.xls') #bk是Book类的对象
sheet = bk.sheet_by_name('empinfo') #sheet 是Sheet类的对象
print(sheet.nrows) #调Sheet类的静态属性 nrows

#读有多少列
print(sheet.ncols) #column

#读某单元格（ANALYST）

cell_value = sheet.cell_value(12,6) #下标从0开始
print(cell_value)

#读整个第X（7）行数据

row_values = sheet.row_values(6,4)
print(row_values)


#读某列（姓名）数据
col_values = sheet.col_values(5,5)
print(col_values)


#读整个列表数据

empinfo=[]
for i in range(5,14):
    empinfo.append(sheet.row_values(i,4))
print(empinfo)



