# -*- coding: utf-8 -*-
# @Time    : 2019-07-26 10:21
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : repgoogle.py
# @Software: PyCharm

# selenium:3.12.0
# webdriver:2.38
# chrome.exe: 65.0.3325.181（正式版本） （32 位）
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime

start_time = datetime.now()
print(start_time)
options = webdriver.ChromeOptions()
options.add_argument('headless')
# 引入chromedriver.exe
chromedriver = "/Users/yangyuexiong/Desktop/WFX_Test/WFX_BusinessLogic_Test/chromedriver_for_mac/chromedriver"
driver = webdriver.Chrome(executable_path=chromedriver, chrome_options=options)
driver.set_window_size(1280, 800)
# driver.get('https://www.baidu.com')
driver.get('https://www.google.com')
# print(driver.title)
driver.find_element_by_name("q").send_keys("okc")
driver.find_element_by_name('q').send_keys(Keys.ENTER)
print(driver.find_element_by_xpath('//*[@id="resultStats"]').text)
# driver.find_element_by_xpath('//*[@id="resultStats"]/text()')
# driver.save_screenshot("3.png")
# print(driver.title)
driver.quit()

end_time = datetime.now()
print(end_time)
