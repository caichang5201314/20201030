# -*- coding: utf-8 -*-
from selenium import webdriver
from xlrd import open_workbook
from xlutils.copy import copy
from time import sleep

driver = webdriver.Chrome()
driver.get('https://login.51job.com/login.php')
driver.maximize_window()
driver.find_element_by_id('loginname').send_keys('15920413866')
driver.find_element_by_id('password').send_keys('xiu360360')
driver.find_element_by_id('login_btn').click()

driver.find_element_by_link_text('职位搜索').click()
driver.find_element_by_id('keywordInput').send_keys('软件测试工程师')
driver.find_element_by_id('search_btn').click()

#print(driver.find_element_by_xpath('/html/body/div[2]/div[3]/div/div[2]/div[4]/div[1]/div[1]/div[2]/a'))

# /html/body/div[2]/div[3]/div/div[2]/div[4]/div[1]/div[1]/div[2]/a
# /html/body/div[2]/div[3]/div/div[2]/div[4]/div[1]/div[2]/div[2]/a
sleep(2)

driver.find_element_by_class_name('chall').click()


company = []
for i in range(1, 51):
    company.append(driver.find_element_by_xpath('/html/body/div[2]/div[3]/div/div[2]/div[4]/div[1]/div[%d]/div[2]/a' %i).text)
print(company)

yuanshi_excel = open_workbook(r'd:\emp.xls',formatting_info=True)
sheet = yuanshi_excel.sheet_by_name('黑名单公司')
black_company = sheet.col_values(0,1)
print(black_company)



new_excel = copy(yuanshi_excel)
sheet = new_excel.get_sheet(3)
for i in range(len(company)):
    sheet.write(i+1,0,company[i])
    if company[i] in black_company:
        # 去除打勾 
        #driver.find_element_by_css_selector('body > div:nth-child(4) > div.j_result > div > div.leftbox > div:nth-child(4) > div.j_joblist > div:nth-child(%d) > div.e_icons.ick' %(i+1)).click()
        driver.find_element_by_xpath('/html/body/div[2]/div[3]/div/div[2]/div[4]/div[1]/div[%d]/div[1]' %(i+1)).click()
        #点击批量申请
        

new_excel.save(r'd:\caichang.xls')