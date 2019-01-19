# -*- coding: utf-8 -*-
# @Time    : 2018/10/2 下午10:09
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : myunit.py
# @Software: PyCharm

import unittest
from common.desired_caps import appium_android
import logging
from time import sleep


class StartEnd(unittest.TestCase):
    def setUp(self):
        logging.info('==========setUp==========')
        self.driver = appium_android()

    def tearDown(self):
        logging.info('==========tearDown==========')
        sleep(5)
        self.driver.close_app()
