# -*- coding: utf-8 -*-
from selenium import webdriver



driver = webdriver.Chrome()
driver.get('http://192.168.1.4/ecshop/admin/privilege.php?act=login')
driver.maximize_window()


driver.find_element_by_name('username').send_keys('caichang')
driver.find_element_by_name('password').send_keys('caichang1')
driver.find_element_by_class_name('btn-a').click()


driver.switch_to.frame('menu-frame')
driver.find_element_by_link_text('商品列表').click()
driver.switch_to.default_content()
driver.switch_to.frame('main-frame')

driver.find_element_by_name('keyword').send_keys('车')
driver.find_element_by_xpath("//input[@value=' 搜索 ']").click()

#driver.find_element_by_css_selector('.caichang')
#driver.find_element_by_tag_name(name)
#//*[@id="listDiv"]/table[1]/tbody/tr[3]/td[2]/span

