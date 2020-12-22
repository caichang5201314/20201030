# -*- coding: utf-8 -*-

from pymysql import connect
conn = connect(host='192.168.1.4', user='root', password="root", database='cms', port=3306)
cursor = conn.cursor()

cursor.execute('select * from _cai_student_cai')
result = cursor.fetchall()

#print(result)

from xlwt.Formatting import Borders, Font, Alignment, Pattern
from xlwt.Style import XFStyle
from xlwt.Workbook import Workbook

wb = Workbook('utf-8')
sheet = wb.add_sheet('学生信息')
title = ['编号', '姓名', '生日', '性别']

title_style = XFStyle()
border = Borders()
border.left = border.THIN
border.right = border.THIN
border.top = border.THIN
border.bottom = border.THIN

font = Font()
font.bold = True

alignment = Alignment()
alignment.horz = alignment.HORZ_CENTER

pattern = Pattern()
pattern.pattern = pattern.SOLID_PATTERN
pattern.pattern_fore_colour = 0x35

title_style.borders = border
title_style.font = font
title_style.alignment = alignment
title_style.pattern = pattern

for i in range(len(title)):
    sheet.write(4, i + 4, title[i], title_style)
    
content = result

content_style = XFStyle()
border = Borders()
border.left = border.THIN
border.right = border.THIN
border.top = border.THIN
border.bottom = border.THIN

content_style.borders = border

for i in range(len(content)):
    for j in range(len(content[i])):
        sheet.write(5 + i, 4 + j, content[i][j], content_style)

cursor.close()
conn.close()
wb.save(r'd:\学生表.xls')

