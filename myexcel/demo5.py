# -*- coding: utf-8 -*-
from pymysql import connect
conn = connect(host='152.21.1.111', user='test01', password="123456", database='testdb', port=3306,charset='utf8')
cursor = conn.cursor()
#执行sql语句
cursor.execute('select * from audit_test')
result = cursor.fetchall()
print(result)
#用完一定记得关闭游标和连接
cursor.close()
conn.close()