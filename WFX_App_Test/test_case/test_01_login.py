# -*- coding: utf-8 -*-
# @Time    : 2018/10/3 下午12:51
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : test_01_login.py
# @Software: PyCharm

from common.myunit import StartEnd
from businessView.loginView import *
import unittest


class LoginTest(StartEnd):

    # @unittest.skip('test_login1_normal')
    def test_login1_normal(self):
        """1.正确的手机号与密码"""
        logging.info('======test_login1_normal=====')

        l = LoginView(self.driver)
        l.login_action('15013038819', 'yyy333')
        self.assertTrue(l.check_login_status('login_ok'), msg='login fail!')

    # @unittest.skip('test_login2_normal')
    def test_login2_normal(self):
        """2.正确的手机号与错误密码"""
        logging.info('======test_login2_normal=====')

        l = LoginView(self.driver)
        l.login_action('15013038819', 'yyy331')
        self.assertTrue(l.check_login_status('login_fail'), msg='test fail!')

    # @unittest.skip('test_login3_normal')
    def test_login3_normal(self):
        """3.未注册的手机号码"""
        logging.info('======test_login3_normal=====')

        l = LoginView(self.driver)
        l.login_action('15013038818', 'yyy333')
        self.assertTrue(l.check_login_status('login_fail'), msg='test fail!')

    # @unittest.skip('test_login4_normal')
    def test_login4_normal(self):
        """4.正确邮箱与正确密码"""
        logging.info('======test_login4_normal=====')

        l = LoginView(self.driver)
        l.login_action('yang6333yyx@126.com', 'yyy333')
        self.assertTrue(l.check_login_status('login_ok'), msg='test fail!')

    # @unittest.skip('test_login5_normal')
    def test_login5_normal(self):
        """5.正确邮箱与错误密码"""
        logging.info('======test_login5_normal=====')

        l = LoginView(self.driver)
        l.login_action('yang6333yyx@126.com', 'yyy331')
        self.assertTrue(l.check_login_status('login_fail'), msg='test fail!')

    # @unittest.skip('test_login6_normal')
    def test_login6_normal(self):
        """6.未注册的邮箱"""
        logging.info('======test_login6_normal=====')

        l = LoginView(self.driver)
        l.login_action('yang63331yyx@126.com', 'yyy333')
        self.assertTrue(l.check_login_status('login_fail'), msg='test fail!')


if __name__ == '__main__':
    unittest.main()
