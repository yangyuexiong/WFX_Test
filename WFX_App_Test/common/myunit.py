# -*- coding: utf-8 -*-
# @Time    : 2018/10/11 下午1:22
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : myunit.py
# @Software: PyCharm

import unittest
from devices.phones import android_phone
import logging
from time import sleep


class StartEnd(unittest.TestCase):
    def setUp(self):
        logging.info('==========setUp==========')
        self.driver = android_phone()

        try:
            self.driver.find_element_by_id('com.wavehk.android:id/update_cancel').click()
        except BaseException:
            logging.info('=====no-up=====')

    def tearDown(self):
        logging.info('==========tearDown==========\n')
        sleep(2)
        self.driver.close_app()


class SQLTest(unittest.TestCase):
    def setUp(self):
        logging.info('==========测试数据初始化==========')

    def tearDown(self):
        logging.info('==========done==========\n')
