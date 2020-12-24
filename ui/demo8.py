# -*- coding: utf-8 -*-
from time import sleep

from pymysql import connect
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


driver = webdriver.Chrome()
driver.get('http://192.168.1.4/ecshop/admin/privilege.php?act=login')
driver.maximize_window()
driver.find_element_by_name('username').send_keys('caichang')
driver.find_element_by_name('password').send_keys('caichang1')
driver.find_element_by_class_name('btn-a').click()
sleep(1)

driver.switch_to.frame('menu-frame')
driver.find_element_by_link_text('商品列表').click()
driver.switch_to.default_content()
driver.switch_to.frame('main-frame')
sleep(1)

try:
    goods_name = driver.find_element_by_xpath('//*[@id="listDiv"]/table[1]/tbody/tr[3]/td[2]/span').text

    img_type = driver.find_element_by_xpath('//*[@id="listDiv"]/table[1]/tbody/tr[3]/td[5]/img').get_attribute('src').split('/')
    if img_type[-1]=='no.gif':
        is_on_sale = 1
    else:
        is_on_sale = 0
    
    
    driver.find_element_by_xpath('//*[@id="listDiv"]/table[1]/tbody/tr[3]/td[5]/img').click()
    
    conn = connect('192.168.1.4', 'root', 'root', 'ecshop', 3306)
    cursor = conn.cursor()
    cursor.execute("select is_on_sale from ecs_goods where goods_name='%s'" %goods_name)
    result = cursor.fetchone()
    #print(result[0])
    if result[0] == is_on_sale:
        print('测试通过')
    else:
        print('测试不通过')
except NoSuchElementException:
    print('对不起，没有任何商品')

