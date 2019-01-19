# -*- coding: utf-8 -*-
# @Time    : 2018/10/12 上午10:27
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : registerView.py
# @Software: PyCharm

from common.common_func import Common, NoSuchElementException, By
from businessView.loginView import LoginView
import logging
from datebase.db_operation import del_test_data


class RegisterView(LoginView):
    p = (By.XPATH,
         "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.EditText")

    p2 = (By.XPATH,
          "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[3]/android.widget.LinearLayout/android.widget.EditText")

    next_btn = (By.ID, 'com.wavehk.android:id/set_password_next')
    shi_ming = (By.ID, 'com.wavehk.android:id/view_action_bar_title')
    pass_btn = (By.ID, 'com.wavehk.android:id/ignore')

    def check_db(self, acc):  # 废除该方法
        """查询sql"""
        logging.info('======检查帐号是否注册======')

    def clear_acc(self, acc):  # 废除该方法
        """删除测试数据"""
        logging.info('======删除测试数据: %s======' % acc)
        del_test_data(acc)
        logging.info('======done======')

    def register(self, username, cod):
        """
        1.重置未登录状态
        2.注册
        """
        if self.check_cancellation():
            self.code_login(username, cod)
        else:
            self.logout_accounts()
            self.code_login(username, cod)

    def send_new_pwd(self, new_pwd):
        """输入登录密码跳过实名认证"""
        logging.info('===登录密码: %s===' % new_pwd)
        self.driver.find_element(*self.p).send_keys(new_pwd)
        self.driver.find_element(*self.p2).send_keys(new_pwd)
        self.driver.find_element(*self.next_btn).click()
        try:
            # self.hide_keyboard()
            self.driver.find_element(*self.shi_ming).click()
            self.driver.find_element(*self.pass_btn).click()
        except BaseException:
            self.driver.find_element(*self.shi_ming).click()
            self.driver.find_element(*self.pass_btn).click()

    def check_register_status(self, test):
        """断言注册后的结果"""
        logging.info('=====register is: %s====' % test)
        if test == 'register_ok':
            try:
                element = self.driver.find_element(*self.my)
                return True
            except NoSuchElementException:
                return False
        elif test == 'register_fail':
            try:
                element = self.driver.find_element(*self.shi_ming)
                return True
            except NoSuchElementException:
                return False
