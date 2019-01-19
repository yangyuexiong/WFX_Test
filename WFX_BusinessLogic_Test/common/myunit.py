# -*- coding: utf-8 -*-
# @Time    : 2019/1/2 4:50 PM
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : myunit.py
# @Software: PyCharm


import unittest
import logging
from selenium import webdriver
from time import sleep
import os

"""
ps -ef | grep phantomjs
killall phantomjs
"""


class StartEnd(unittest.TestCase):
    driver_swicth = False
    # mac
    if driver_swicth:
        # mac
        driver = webdriver.PhantomJS(executable_path='../phantomjs-2.1.1-macosx/bin/phantomjs')
        # Windows
        # driver = webdriver.PhantomJS(executable_path=r'..\phantomjs-2.1.1-windows\bin\phantomjs.exe')

    def setUp(self):
        print('======测试开始======')

    def tearDown(self):
        # self.driver.quit()
        if self.driver_swicth:
            # mac
            os.system("killall phantomjs")
        print('======测试结束======')
