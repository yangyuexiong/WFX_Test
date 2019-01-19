# -*- coding: utf-8 -*-
# @Time    : 2018/10/2 下午9:46
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : common_fun.py
# @Software: PyCharm

from baseView.baseView import BaseView
from common.desired_caps import appium_android
from selenium.common.exceptions import NoSuchElementException
import logging
from selenium.webdriver.common.by import By
import time, os
import csv


class Common(BaseView):
    cancelBtn = (By.ID, '')
    skipBtn = (By.ID, '')
    login_into = (By.ID, 'com.wavehk.android:id/line')

    def check_cancellation(self):
        logging.info('==========检查是否注销==========')
        try:
            print('1')
            driver.find_elements_by_id("com.wavehk.android:id/line")
            e = driver.find_elements_by_id("com.wavehk.android:id/line")
            print(e)
            # login_into = self.driver.find_element(*self.login_into)
        except NoSuchElementException:
            print('3')
            pass
        else:
            print('2')
            # login_into.click()
            driver.click()

    def check_cancelBtn(self):
        logging.info('==========check_cancelBtn==========')
        try:
            cancelBtn = self.driver.find_element(*self.cancelBtn)
        except NoSuchElementException:
            pass
        else:
            cancelBtn.click()

    def get_size(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return x, y

    def getTime(self):
        self.now = time.strftime("%Y-%m-%d %H_%M_%S")
        return self.now

    def getScreenShot(self, module):
        this_time = self.getTime()
        image_file = os.path.dirname(os.path.dirname(__file__)) + '/screenshots/%s_%s.png' % (module, this_time)

        logging.info('截图 %s ' % module)
        self.driver.get_screenshot_as_file(image_file)

    def get_csv_data(self, csv_file, line):
        with open(csv_file, 'r', encoding='utf-8-sig') as f:
            reader = csv.reader(f)
            for index, row in enumerate(reader, 1):
                if index == line:
                    return row


if __name__ == '__main__':
    driver = appium_android()
    c = Common(driver)
    c.check_cancellation()
    # c.getScreenShot('首页')
