# -*- coding: utf-8 -*-
# @Time    : 2018/10/2 下午9:44
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : baseView.py
# @Software: PyCharm


class BaseView:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, *loc):
        return self.driver.find_element(*loc)

    def find_elements(self, *loc):
        return self.driver.find_elements(*loc)

    def get_window_size(self):
        return self.driver.get_window_size()

    def swipe(self):
        return self.driver.swipe()
