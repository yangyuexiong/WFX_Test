# -*- coding: utf-8 -*-
# @Time    : 2018/10/12 上午11:22
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : test_02_register.py
# @Software: PyCharm

from common.myunit import StartEnd, SQLTest
from businessView.registerView import *
import unittest
import logging
from data.datas import test_data
from datebase.db_operation import s


class RegisterInit(SQLTest):

    def test_init(self):
        """RegisterInit"""
        s(test_data['phone'])
        s(test_data['email'])
        logging.info('===RegisterInit Done===')


class RegisterTest(StartEnd):
    phone = '13533385515'
    phone2 = '15013038819'
    email = 'yangyuexiongaini@126.com'
    code_msg = '1111'
    err_code_msg = '12345'
    new_pwd = 'yyy333'

    def test_register1(self):
        """手机号注册"""
        logging.info('======test_register1=====')

        r = RegisterView(self.driver)
        logging.info('===注册===')
        r.register(test_data['phone'], self.code_msg)
        r.send_new_pwd(self.new_pwd)
        self.assertTrue(r.check_register_status('register_ok'), msg='register_ok!')
        # del_test_data(test_data['phone'])

    def test_register2(self):
        """邮箱注册"""
        logging.info('======test_register2=====')

        r = RegisterView(self.driver)
        logging.info('===注册===')
        r.register(test_data['email'], self.code_msg)
        r.send_new_pwd(self.new_pwd)
        self.assertTrue(r.check_register_status('register_ok'), msg='register_ok!')
        # del_test_data(test_data['email'])

    # @unittest.skip('test_register3')
    def test_register3(self):
        """邮箱与验证码错误"""
        logging.info('======test_register3=====')

        r = RegisterView(self.driver)
        logging.info('===注册===')
        r.register(self.email, self.err_code_msg)
        self.assertTrue(r.check_login_status('login_fail'), msg='test fail!')

    # @unittest.skip('test_register4')
    def test_register4(self):
        """手机与验证码错误"""
        logging.info('======test_register4=====')

        r = RegisterView(self.driver)
        logging.info('===注册===')
        r.register(self.phone, self.err_code_msg)
        self.assertTrue(r.check_login_status('login_fail'), msg='test fail!')

    # @unittest.skip('test_register5')
    def test_register5(self):
        """已经注册的手机"""
        logging.info('======test_register5=====')

        r = RegisterView(self.driver)
        logging.info('===注册===')
        r.register(self.phone2, self.err_code_msg)
        self.assertTrue(r.check_login_status('login_fail'), msg='test fail!')

    # def test_register6(self):
    #     """删除测试数据"""
    #     logging.info('======test_register6=====')
    #
    #     del_test_data(test_data['phone'])
    #     del_test_data(test_data['email'])


if __name__ == '__main__':
    unittest.main()
