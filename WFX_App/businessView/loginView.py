# -*- coding: utf-8 -*-
# @Time    : 2018/10/10 下午3:10
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : loginView.py
# @Software: PyCharm

import logging
from common.common_fun import Common, NoSuchElementException, By


class LoginView(Common):
    # login_into = (By.ID, 'com.wavehk.android:id/line')
    username_type = (By.ID, 'com.wavehk.android:id/user_center_phone_edit')
    password_type = (By.ID, 'com.wavehk.android:id/user_center_code_edit')
    loginBtn = (By.ID, 'com.wavehk.android:id/user_center_submit_button')

    def login_action(self, username, password):
        self.check_cancellation()
        # self.check_skipBtn()
        logging.info('============login_action==============')
        logging.info('username is:%s' % username)
        self.driver.find_element(*self.username_type).send_keys(username)

        logging.info('password is:%s' % password)
        self.driver.find_element(*self.password_type).send_keys(password)

        logging.info('click loginBtn')
        self.driver.find_element(*self.loginBtn).click()
        logging.info('login finished!')


if __name__ == '__main__':
    from common.desired_caps import appium_android

    driver = appium_android()
    from time import sleep

    sleep(5)
    l = LoginView(driver)
    l.login_action('15013038819', '1111')
