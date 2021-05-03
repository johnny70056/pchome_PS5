# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 21:48:03 2021

@author: johnn
"""

# coding: utf-8

from selenium import webdriver
#import requests
from datetime import datetime
import time
#import sys

#啟動時間設定年、月、日、時、分、秒
startTime = datetime(2021, 4, 16, 11, 59, 59)
print('Program not starting yet...')
while datetime.now() < startTime:
	time.sleep(1)
print('Program now starts on %s' % startTime)
print('Executing...')
#如果使用headless會幫助跑的速度，因為不用顯示出來
option = webdriver.ChromeOptions()
#option.add_argument('headless')
option.add_argument("--lang=en")
driver = webdriver.Chrome(chrome_options=option,executable_path='./chromedriver.exe')
# 
#這邊放商品網址
url = 'https://24h.pchome.com.tw/prod/DGBJG9-A900B51SM?fq=/S/DGBJG9'

driver.get(url)
time.sleep(0.5)

button_buy = driver.find_element_by_xpath('//*[@id="ButtonContainer"]/button')

button_buy.click()
time.sleep(0.5)

button_check = driver.find_element_by_class_name("check")

button_check.click()

time.sleep(1)
account = driver.find_element_by_xpath('//*[@id="loginAcc"]')
account.clear()
account.send_keys('帳號')

password = driver.find_element_by_xpath('//*[@id="loginPwd"]')
password.clear()
password.send_keys('密碼')
driver.find_element_by_xpath('//*[@id="btnLogin"]').click()

time.sleep(6)
#找到一次付清按鈕
button_CC = driver.find_element_by_class_name('CC')
                                       
button_CC.click()

time.sleep(1)
threeword = driver.find_element_by_xpath('//*[@id="multi_CVV2Num"]')
threeword.clear()
threeword.send_keys('三碼')















