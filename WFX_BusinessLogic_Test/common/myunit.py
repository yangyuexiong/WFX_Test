# -*- coding: utf-8 -*-
# @Time    : 2019/1/2 4:50 PM
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : myunit.py
# @Software: PyCharm


import unittest
import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import os

"""
ps -ef | grep phantomjs
killall phantomjs
"""

"""
ps -ef | grep chromedriver
killall chromedriver
"""


class StartEnd(unittest.TestCase):
    driver_swicth = False
    # mac
    if driver_swicth:
        """PhantomJ用于旧版selenuim"""
        # mac
        # driver = webdriver.PhantomJS(executable_path='../phantomjs-2.1.1-macosx/bin/phantomjs')
        # Windows
        # driver = webdriver.PhantomJS(executable_path=r'..\phantomjs-2.1.1-windows\bin\phantomjs.exe')
        """chromedriver无头用于新版selenuim"""
        chrome_options = Options()
        chrome_options.add_argument('--no-sandbox')  # 解决DevToolsActivePort文件不存在的报错
        chrome_options.add_argument('window-size=1920x3000')  # 指定浏览器分辨率
        chrome_options.add_argument('--disable-gpu')  # 谷歌文档提到需要加上这个属性来规避bug
        chrome_options.add_argument('--hide-scrollbars')  # 隐藏滚动条, 应对一些特殊页面
        chrome_options.add_argument('blink-settings=imagesEnabled=false')  # 不加载图片, 提升速度
        chrome_options.add_argument('--headless')  # 浏览器不提供可视化页面. linux下如果系统不支持可视化不加这条会启动失败
        # chrome_options.binary_location = "./chromedriver_for_mac/chromedriver"  # 手动指定使用的浏览器位置
        # mac: 将chromedriver放在 /usr/bin 可以直接使用。
        # 放在项目目录下添加路径:executable_path='./chromedriver_for_mac/chromedriver'。
        driver = webdriver.Chrome(executable_path='./chromedriver_for_mac/chromedriver', chrome_options=chrome_options)

    def setUp(self):
        print('======测试开始======')

    def tearDown(self):
        self.driver.quit()
        if self.driver_swicth:
            # mac
            # os.system("killall phantomjs")
            os.system("killall chromedriver")
        print('======测试结束======')
