# -*- coding: utf-8 -*-
from xlrd import open_workbook
from xlutils.copy import copy
from xlwt.Formatting import Borders
from xlwt.Style import XFStyle

yuanshi_excel = open_workbook(r'd:\原始表.xls', formatting_info=True)
new_excel = copy(yuanshi_excel)
sheet = new_excel.get_sheet(0)

content_style = XFStyle()
border = Borders()
border.left = border.THIN
border.right = border.THIN
border.top = border.THIN
border.bottom = border.THIN

content_style.borders = border

sheet.write(2, 5, 14, content_style)
sheet.write(2, 8, '蔡昶', content_style)
new_excel.save(r'd:\新表.xls')

