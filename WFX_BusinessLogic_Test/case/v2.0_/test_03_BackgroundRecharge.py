# -*- coding: utf-8 -*-
# @Time    : 2019/1/3 4:48 PM
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : test_03_BackgroundRecharge.py
# @Software: PyCharm

from common.ban_warning import *
from common.public_func import *
from selenium import webdriver
from common.myunit import StartEnd
import unittest
import requests

# 浏览器
driver = webdriver.PhantomJS(executable_path='../phantomjs-2.1.1-macosx/bin/phantomjs')

from time import sleep
import time
import datetime

now_time = datetime.datetime.now()
now_time_c = time.mktime(now_time.timetuple())


def login_admin(url):
    # driver.get("http://ptest.wavehk.cn:8080")
    driver.get(url)
    sleep(5.8)
    driver.find_element_by_id('pd-form-username').send_keys('admin')
    sleep(0.3)
    driver.find_element_by_name('password').send_keys('123456')
    sleep(0.3)
    driver.find_element_by_xpath('//*[@id="login-form"]/div[6]/div/button').click()
    print('登录成功')


class RechargeTest(StartEnd):
    """后台充值"""
    money = '100'
    user_id = '9681'
    user_info = {}
    driver_swicth = True

    def test_Recharge1(self):
        """后台充值后对应数据变化"""
        '''
        获取用户信息
        '''
        self.user_info = sclect_user(self.user_id)
        # print(self.user_info)
        '''
        后台充值
        '''
        u = "http://ptest.wavehk.cn:8080/admin/account/users2/deposit/ids/%s" % self.user_id
        login_admin(u)
        sleep(4.5)
        driver.save_screenshot("1.png")
        driver.find_element_by_name('ramount').send_keys(self.money)
        sleep(0.8)
        driver.find_element_by_xpath('//*[@id="edit-form"]/div[3]/div/button[1]').click()
        sleep(0.5)
        driver.save_screenshot("2.png")
        # driver.quit()
        print('======充值成功======')
        '''
        检查充值后变化
        '''
        # 总资产计算
        new_user_obj = sclect_user(self.user_id)
        old_ramount = self.user_info['ramount']
        add_ramount = float(self.money)
        print('原资产:', old_ramount, type(old_ramount))
        print('充值金额:', add_ramount, type(add_ramount))
        new_ramount = new_user_obj['ramount']
        print('充值后金额:', new_ramount, type(new_ramount))
        assert float(new_ramount) == float(old_ramount) + add_ramount

        # 积分
        old_account_integral = self.user_info['account_integral']
        new_account_integral = new_user_obj['account_integral']
        print('原有积分:%s' % old_account_integral)
        print('充值后积分:%s' % new_account_integral)
        if int(self.money) >= 10:
            assert int(new_account_integral) == int(old_account_integral) + int(self.money) / 10
        else:
            print('充值金额小于10美元,不增加积分。')

    def test_Recharge2(self):
        """积分记录"""
        self.driver_swicth = False
        base_url1 = 'https://ptest.wavehk.cn/v2/UserLevel/getUserIntegralList'
        header = {
            "token": token()
        }
        param_data1 = {
            "did": "12345dg",
            "type": "3",
            "sign": "5sCioY2cazwBz0aN\/Wa754q7krwmNsvS2VHMRhvjQnrPrsqpNnY\/EGrVa1YDSrZ3",
            "limit": 20,
            "page": 1,
            "apptype": "ios",
            "version": "2.4.0"
        }
        lo = requests.post(base_url1, json=param_data1, headers=header, verify=False)
        assert int(lo.json()['data'][0]['integral']) == int(int(self.money) / 10)

        if int(self.money) >= 10:
            t = lo.json()['data'][0]['create_time']
            t1 = datetime.datetime.strptime(t, '%Y-%m-%d %H:%M:%S')
            t2 = time.mktime(t1.timetuple())
            # print(t2)
            # print(now_time_c)
            # print(t2 - now_time_c)
            assert now_time_c - t2 <= 60
        else:
            print('充值金额小于10美元,不增加积分。')

        # print(lo.json()['data'][0]['integral'])
        # print(lo.json()['data'][0]['description'])
        # print(lo.json()['data'][0]['create_time'])


if __name__ == '__main__':
    unittest.main()
