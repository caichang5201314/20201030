# -*- coding: utf-8 -*-
from time import sleep

from pymysql import connect
from selenium import webdriver
from selenium.webdriver.support.select import Select
from xlrd import open_workbook


wb = open_workbook(r'd:\emp.xls')
sheet = wb.sheet_by_name('商品信息表')

values= sheet.col_values(0,1)

for i in range(len(values)):
    conn = connect('192.168.1.4','root','root','ecshop',3306)
    cursor = conn.cursor()
    cursor.execute("delete from ecs_goods where goods_name='%s'" %values[i])
    conn.commit()

    driver = webdriver.Chrome()
    driver.get('http://192.168.1.4/ecshop/admin')
    driver.maximize_window()
    driver.find_element_by_name('username').send_keys('caichang')
    driver.find_element_by_name('password').send_keys('caichang1')
    driver.find_element_by_class_name('btn-a').click()
     
    driver.switch_to.frame('menu-frame')
    driver.find_element_by_link_text('商品列表').click()
    driver.switch_to.default_content()
    driver.switch_to.frame('main-frame')
    sleep(2)
    driver.find_element_by_xpath('//a[@href="goods.php?act=add"]').click()
    sleep(1)
    driver.find_element_by_name('goods_name').send_keys(values[i])
     
    Select(driver.find_element_by_name('cat_id')).select_by_visible_text('    小型手机')
    driver.find_element_by_xpath('//input[@value=" 确定 "]').click()
     
    sleep(2)
     
    cursor.execute("select * from ecs_goods where goods_name='%s'" %values[i])
    result = cursor.fetchone()
    print(result)
    print(type(result))
    if result[3]==values[i]:
        print('测试通过')
    else:
        print('测试不通过')
    
    driver.close()     
    conn.close()
    cursor.close()


