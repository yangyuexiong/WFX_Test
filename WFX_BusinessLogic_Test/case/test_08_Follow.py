# -*- coding: utf-8 -*-
# @Time    : 2019/1/8 3:45 PM
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : test_08_Follow.py
# @Software: PyCharm

from common.ban_warning import *
from common.public_func import *
from common.myunit import StartEnd
import unittest
import requests
from bs4 import BeautifulSoup as bs4
import re


def set_dict_s(analyst_id, day):
    import random
    import datetime

    login = 'http://plan.wavehk.cn:8310/login'

    acc = {
        'username': '17688958885',
        'password': 'abc123456'
    }

    profit = [10, 50, 100, 200]
    analyst_p = {
        'analystId': int(analyst_id),
        'amount': 5000.0,
        # 'analystProfits[0].date': 20190109,
        # 'analystProfits[0].profit': 100.0,
    }

    # 登录
    s = requests.Session()
    s.post(login, acc, verify=False)
    cookies = s.cookies

    """
    获取首次添加时间
    """
    u = 'http://plan.wavehk.cn:8310/analyst/profit/list'
    p = {
        'analystId': analyst_id
    }
    lo0 = requests.post(u, p, cookies=cookies, verify=False)
    html = lo0.text
    soup = bs4(html, 'lxml')
    # print(soup)
    l1 = soup.select('input[class="form-control analystProfitDate"]')[0]
    d1 = str(l1)[83:-3]
    d2 = re.sub("\D", "", d1)
    d3 = '{}-{}-{}'.format(str(d2)[0:4], str(d2)[4:6], str(d2)[6:8])
    # print(d2)
    # print(d3)

    now = datetime.datetime.now().strftime("%Y-%m-%d")

    okc1 = datetime.datetime.strptime('{} 00:00:00'.format(str(now)), '%Y-%m-%d %H:%M:%S')
    # okc2 = datetime.datetime.strptime('2018-12-1 00:00:00', '%Y-%m-%d %H:%M:%S')
    okc2 = datetime.datetime.strptime('{} 00:00:00'.format(str(d3)), '%Y-%m-%d %H:%M:%S')
    delta = okc1 - okc2
    # print(delta.days)

    if delta.days > 30:
        print('执行')
        num = 0
        for i in range(0, int(day)):
            # print(num)
            k1 = 'analystProfits[%s].date' % str(num)
            k2 = 'analystProfits[%s].profit' % str(num)
            # print(k1)
            # print(k2)
            now = datetime.datetime.now()
            add_day = now + datetime.timedelta(days=i)
            # print(add_day.strftime("%Y%m%d"))
            # zip(a, b)
            analyst_p[k1] = add_day.strftime("%Y%m%d")
            analyst_p[k2] = random.choice(profit)
            num += 1
        return analyst_p
    else:
        return False


class SetAnalyst(StartEnd):
    """分析师收益设置"""
    driver_swicth = True
    login = 'http://plan.wavehk.cn:8310/login'

    acc = {
        'username': '17688958885',
        'password': 'abc123456'
    }

    analyst_u = 'http://plan.wavehk.cn:8310/analyst/update'

    def test_set_analyst1(self):
        """登录分析师后台-设置收益"""

        # 登录
        s = requests.Session()
        s.post(self.login, self.acc, verify=False)
        cookies = s.cookies

        # 设置每日盈亏
        analyst_p = set_dict_s(275, 30)
        # print(analyst_p)

        # 设置
        if analyst_p:
            lo = requests.post(self.analyst_u, analyst_p, cookies=cookies, verify=False)
            print(lo.text)

    @unittest.skip('PhantomJS')
    def test_set_analyst0(self):
        """PhantomJS登录分析师后台"""
        self.driver_swicth = True
        driver = self.driver
        u = 'http://plan.wavehk.cn:8310/analyst/list'
        driver.get(u)
        driver.find_element_by_id('username').send_keys('17688958885')
        driver.find_element_by_id('password').send_keys('abc123456')
        driver.find_element_by_class_name('form-group').click()
        driver.find_element_by_xpath('/html/body/div/div/div/form/div[3]/button').click()
        driver.save_screenshot("3.png")
        self.driver_swicth = False


@unittest.skip('pass_08')
class FollowTest(StartEnd):
    header = {
        "token": token()
    }
    follow_u = 'https://ptest.wavehk.cn/v1/Documentary/follow'
    follow_p = {
        "coupon_id": 0,
        "version": "2.5",
        "an_id": "275",
        "f_id": "",
        "apptype": "ios",
        "follow_price": 500,
        "sign": "5sCioY2cazwBz0aN\/Wa751AusYH7ZXib6Xr2aCGoo4LgkH860jhupDeyujFuHoZm",
        "did": "12345dg",
        "stop_price": 250
    }

    def test_follow1(self):
        """跟随成功"""

        # lo = requests.post(self.follow_u, json=self.follow_p, headers=self.header, verify=False)
        # print(lo.json())


if __name__ == '__main__':
    unittest.main()
