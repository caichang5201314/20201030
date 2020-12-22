# -*- coding: utf-8 -*-
from pymysql import connect


class MyMySQL():

    def __init__(self, host, user, password, database, port):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.port = port
        
    def get_connect(self,host, user, password, database, port):
        conn = connect(host, user, password, database, port)
        return conn
    
    def __getcursor(self,host, user, password, database, port):
        conn = self.get_connect(host, user, password, database, port)
        cursor = conn.cursor()
        return cursor
    
    def execute(self,host, user, password, database, port,sql):
        self.__getcursor(host, user, password, database, port).execute(sql)
        result = self.__getcursor(host, user, password, database, port).fetchall()
        return result
    
    def close(self,host, user, password, database, port):
        self.__getcursor(host, user, password, database, port).close()
        self.get_connect(host, user, password, database, port).close()
    
my = MyMySQL()
print(my.execute('192.168.1.4','root','root','cms',3306,'select * from _cai_student_cai'))