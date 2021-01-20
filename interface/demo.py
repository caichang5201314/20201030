# -*- coding: utf-8 -*-

from requests.api import request
from xlrd import open_workbook
from xlutils.copy import copy
from xlwt.Formatting import Borders
from xlwt.Style import XFStyle


wb = open_workbook(r'd:\emp.xls',formatting_info=True)
sheet = wb.sheet_by_name('手机号码归属地查询')
row_value = sheet.row_values(1,1)
print(row_value)

content_style = XFStyle()
border = Borders()
border.left = border.THIN
border.right = border.THIN
border.top = border.THIN
border.bottom = border.THIN

content_style.borders = border

url = row_value[1]
params = row_value[3]
response = request(method=row_value[2],url=url, params=params)
print(response.status_code)
print(response.text)
if response.status_code==row_value[5]:
    #{"resultcode":"101","reason":"错误的请求KEY","result":null,"error_code":10001}写入对应的单元格
    new_wb = copy(wb)
    new_sheet = new_wb.get_sheet(5)
    new_sheet.write(1,7,response.text,content_style)
    if response.text==row_value[4]:
        new_sheet.write(1,8,'通过'.content_style)
    else:
        new_sheet.write(1,8,'不通过',content_style)
    new_wb.save(r'd:\接口测试报告.xls')
    #再拿这个结果和预期结果字段比，如果一致就在是否通过这个字段中写通过，否则写不通过
    #pass
    
    
    
