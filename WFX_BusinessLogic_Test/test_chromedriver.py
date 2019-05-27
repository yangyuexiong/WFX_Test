# -*- coding: utf-8 -*-
# @Time    : 2019-05-27 09:45
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : test_chromedriver.py
# @Software: PyCharm


from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')  # 解决DevToolsActivePort文件不存在的报错
chrome_options.add_argument('window-size=1920x3000')  # 指定浏览器分辨率
chrome_options.add_argument('--disable-gpu')  # 谷歌文档提到需要加上这个属性来规避bug
chrome_options.add_argument('--hide-scrollbars')  # 隐藏滚动条, 应对一些特殊页面
chrome_options.add_argument('blink-settings=imagesEnabled=false')  # 不加载图片, 提升速度
chrome_options.add_argument('--headless')  # 浏览器不提供可视化页面. linux下如果系统不支持可视化不加这条会启动失败
# chrome_options.binary_location = "./chromedriver_for_mac/chromedriver"  # 手动指定使用的浏览器位置
driver = webdriver.Chrome(executable_path='./chromedriver_for_mac/chromedriver', chrome_options=chrome_options)
driver.get('https://www.baidu.com')
print(driver.title)
driver.quit()
# driver.close()
