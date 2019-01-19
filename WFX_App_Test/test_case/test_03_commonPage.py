# -*- coding: utf-8 -*-
# @Time    : 2018/10/16 下午4:30
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : test_03_commonPage.py
# @Software: PyCharm


from common.myunit import StartEnd
from businessView.commonPage import *
import unittest
import logging
from data.datas import test_data, test_data_pwd


class CommonPageTest(StartEnd):

    @unittest.skip('test1')
    def test_CommonPageTest1(self):
        """1.入口测试"""
        logging.info('===test_CommonPageTest1===')

        c = CommonPage(self.driver)
        c.check_index(test_data['phone2'], test_data_pwd['phone2'])

    def test_CommonPageTest2(self):
        """2.市场行情"""
        logging.info('===test_CommonPageTest2===')
        c = CommonPage(self.driver)
        c.check_quotation()

    def test_CommonPageTest3(self):
        """3.昨日排行榜"""
        logging.info('===test_CommonPageTest3===')
        c = CommonPage(self.driver)
        c.check_zr()

    def test_CommonPageTest4(self):
        """4.优惠活动"""
        logging.info('===test_CommonPageTest4===')
        c = CommonPage(self.driver)
        c.check_p_activities()


if __name__ == '__main__':
    unittest.main()
