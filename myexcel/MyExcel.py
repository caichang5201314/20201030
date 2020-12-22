# -*- coding: utf-8 -*-
from xlrd import open_workbook


class MyExcel():

    def __init__(self, workbook_name, sheet_name):
        self.workbook_name = workbook_name
        self.sheet_name = sheet_name

    def __sheet(self):
        bk = open_workbook(self.workbook_name) 
        sheet = bk.sheet_by_name(self.sheet_name)
        return sheet
    
    # 读总行数
    def total_rows(self):
        return self.__sheet().nrows

    # 读总列数
    def total_columns(self):
        return self.__sheet().ncols  
    
    # 读单元格值
    def cell_value(self, row, col):
        cell_value = self.__sheet().cell_value(row, col)
        return cell_value
    
    # 读某行值
    def row_values(self, row, start_col, end_col=None):
        if end_col == None:
            end_col = self.total_columns()
        row_values = self.__sheet().row_values(row, start_col, end_col)
        return row_values
    
    # 读某列值
    def col_values(self, col, start_row, end_row=None):
        if end_row == None:
            end_row = self.total_rows()
        col_values = self.__sheet().col_values(col, start_row, end_row)
        return col_values
    
    # 读整个列表
    def list_of_values(self, start_row, start_col, end_row=None, end_col=None):
        if end_col == None:
            end_col = self.total_columns()
        if end_row == None:
            end_row = self.total_rows()
        empinfo = []
        for i in range(start_row, end_row):
            empinfo.append(self.__sheet().row_values(i, start_col, end_col))
        return empinfo


my = MyExcel(r'd:\emp.xls', 'empinfo')
print(my.total_rows())
print(my.total_columns())
print(my.cell_value(12, 6))

print(my.row_values(6, 4))
print(my.col_values(5, 5))
my.list_of_values(5, 4)
print(my.list_of_values(6, 5, 10, 7))
