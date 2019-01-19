# -*- coding: utf-8 -*-
# @Time    : 2018/10/10 下午6:24
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : loginView.py
# @Software: PyCharm

from common.common_func import Common, NoSuchElementException, By
import logging


class LoginView(Common):
    pwd = (By.ID, 'com.wavehk.android:id/password_logo')
    username_type = (By.ID, 'com.wavehk.android:id/user_center_phone_edit')
    password_type = (By.ID, 'com.wavehk.android:id/user_center_password')
    code_type = (By.ID, 'com.wavehk.android:id/user_center_code_edit')
    loginBtn = (By.ID, 'com.wavehk.android:id/user_center_submit_button')

    tip_commit = (By.ID, 'com.wavehk.android:id/money_in')  # 转入标识

    def click_login_button(self):
        """登录按钮"""
        try:
            self.hide_keyboard()
            logging.info('===隐藏键盘===')
        except BaseException as e:
            logging.info('%s' % e)
            self.driver.find_element(*self.loginBtn).click()
            logging.info('ok!')
        else:
            self.driver.find_element(*self.loginBtn).click()
            logging.info('ok!')

    def pwd_login(self, username, password):
        """密码登录业务"""
        logging.info('============click 密码登录==============')
        self.driver.find_element(*self.welcome).click()
        self.driver.find_element(*self.pwd).click()

        logging.info('============send_accounts is:%s==============' % username)
        self.driver.find_element(*self.username_type).send_keys(username)

        logging.info('============send_password is:%s==============' % password)
        self.driver.find_element(*self.password_type).send_keys(password)

        logging.info('===登录===')
        self.click_login_button()

    def code_login(self, username, cod):
        """验证码登录业务"""
        logging.info('============send_accounts is:%s==============' % username)
        self.driver.find_element(*self.username_type).send_keys(username)
        logging.info('============send_cod is:%s==============' % cod)
        self.driver.find_element(*self.code_type).send_keys(cod)
        logging.info('===登录===')
        self.click_login_button()

    def login_action(self, username, password):
        """重置未登录状态"""
        if self.check_cancellation():
            self.pwd_login(username, password)
        else:
            self.logout_accounts()
            # self.check_cancellation()
            self.pwd_login(username, password)

    def check_login_status(self, test):
        """断言登录后的结果"""
        logging.info('=====check_login_status is: %s====' % test)
        if test == 'login_ok':
            try:
                element = self.driver.find_element(*self.tip_commit)
                return True
            except NoSuchElementException:
                return False
        elif test == 'login_fail':
            try:
                element = self.driver.find_element(*self.welcome)
                return True
            except NoSuchElementException:
                return False


if __name__ == '__main__':
    from devices.phones import android_phone

    driver = android_phone()
    from time import sleep

    l = LoginView(driver)
    l.login_action('15013038819', 'yyy333')

    # def ok(x):
    #     x.assertTrue(l.check_login_status())
    # ok(l)
