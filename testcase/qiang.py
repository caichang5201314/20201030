# -*- coding: utf-8 -*-
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()
driver.get('https://www.12306.cn')
driver.maximize_window()
driver.find_element_by_link_text('登录').click()
driver.find_element_by_link_text('账号登录').click()
driver.find_element_by_id('J-userName').send_keys('caichang_52000000')
driver.find_element_by_id('J-password').send_keys('caichang111')
sleep(10)
driver.find_element_by_id('J-login').click()
sleep(2)
ActionChains(driver.find_element_by_xpath('//*[@id="pop_160973212295035683"]/div[2]/div[3]/a')).send_keys(Keys.ENTER).perform()
driver.find_element_by_link_text('首页').click()

