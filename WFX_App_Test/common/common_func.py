# -*- coding: utf-8 -*-
# @Time    : 2018/10/10 下午5:31
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : common_func.py
# @Software: PyCharm

from baseView.baseView import BaseView
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time, os
import logging
import csv


class Common(BaseView):
    my = (By.ID, 'com.wavehk.android:id/foot_d')
    settings = (By.ID, 'com.wavehk.android:id/my_top_bar_setting')
    logout = (By.XPATH,
              '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[9]/android.widget.TextView')
    logout2 = (By.ID, 'com.wavehk.android:id/go_btn')
    login_btn = (By.ID, 'com.wavehk.android:id/user_center_submit_button')
    welcome = (By.ID, 'com.wavehk.android:id/welcome_text')

    lv_up = (By.ID, 'com.wavehk.android:id/update_cancel')

    # def check_lv_up(self):
    #     """检查更新提示"""
    #     try:
    #         self.driver.find_element(*self.lv_up).click()
    #     except BaseException:
    #         pass

    def check_cancellation(self):
        """检查登录未状态"""
        self.driver.find_element(*self.my).click()
        try:
            login_btn = self.driver.find_element(*self.welcome)
            logging.info('=====未登录======')
            return True
        except NoSuchElementException:
            logging.info('=====已登录======')
            return False

    def login_accounts(self, username, password, v_code, username_type, password_type, loginbtn):
        if not v_code:
            logging.info('============send_keys==============')
            logging.info('username is:%s' % username)
            self.driver.find_element(*username_type).send_keys(username)

            logging.info('password is:%s' % password)
            self.driver.find_element(password_type).send_keys(password)

            logging.info('登录')
            self.driver.find_element(*loginbtn).click()
            logging.info('ok!')
        else:
            pass

    def logout_accounts(self):
        """退出登录"""
        logging.info('=====退出登录======')
        self.driver.find_element(*self.settings).click()
        self.driver.find_element(*self.logout).click()
        self.driver.find_element(*self.logout2).click()
        logging.info('=====退出done======')
        self.driver.find_element(*self.my).click()
        logging.info('=====click my======')

    def get_size(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return x, y

    def get_time(self):
        self.now = time.strftime("%Y-%m-%d %H_%M_%S")
        return self.now

    def get_screenShot(self, module):
        this_time = self.get_time()
        image_file = os.path.dirname(os.path.dirname(__file__)) + '/screenshots/%s_%s.png' % (module, this_time)

        logging.info('截图 %s ' % module)
        self.driver.get_screenshot_as_file(image_file)

    def get_csv_data(self, csv_file, line):
        with open(csv_file, 'r', encoding='utf-8-sig') as f:
            reader = csv.reader(f)
            for index, row in enumerate(reader, 1):
                if index == line:
                    return row

    def h(self):
        return self.hide_keyboard()


if __name__ == '__main__':
    from devices.phones import android_phone

    driver = android_phone()
    c = Common(driver)
    c.check_cancellation()
