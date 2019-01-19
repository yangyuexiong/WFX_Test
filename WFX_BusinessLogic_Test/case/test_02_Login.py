# -*- coding: utf-8 -*-
# @Time    : 2019/1/3 2:07 PM
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : test_02_Login.py
# @Software: PyCharm

from common.ban_warning import *
from common.myunit import StartEnd
import unittest
import requests

base_url1 = 'https://ptest.wavehk.cn/v2/user/ruleCode'
base_url2 = 'https://ptest.wavehk.cn/v1/user/login'

param_data1 = {
    "type": "login",
    "code": "1111",
    "mobile_fiex": "86",
    "sign": "5sCioY2cazwBz0aN\/Wa75zO8S6VmRdPJkijw9NQVD2XnnYqpLFI0jymDr0nnJ6kl",
    "apptype": "ios",
    "phone": "15013038819",
    "version": "2.4.0",
    "did": "12345dg"
}

param_data2 = {
    "mobile_fiex": "86",
    "apptype": "ios",
    "sign": "5sCioY2cazwBz0aN\/Wa753d9zJgVyLF8lTj+2My3rvG1aclEcaYIDinwaE14AzqC",
    "phone": "15013038819",
    "password": "yyy333",
    "version": "2.4.0",
    "did": "12345dg"
}


class LoginTest(StartEnd):
    """登录"""

    def test_login1(self):
        """正确验证码登录"""
        lo = requests.post(base_url1, json=param_data1, verify=False)
        # print(lo.json())
        # print('验证码登录:[{},{},{}]'.format(lo.json()['code'], lo.json()['message'], lo.json()['data']['phone']))

        assert lo.json()['code'] == 0
        assert lo.json()['message'] == 'ok'
        assert lo.json()['data']['phone'] == param_data1['phone']

    def test_login2(self):
        """错误验证码登录"""
        param_data1['code'] = '2222'
        lo = requests.post(base_url1, json=param_data1, verify=False)
        # print(lo.json())
        assert lo.json()['code'] == 20004
        assert lo.json()['message'] == '验证码错误或已过期'

    def test_login3(self):
        """正确密码登录"""
        lo = requests.post(base_url2, json=param_data2, verify=False)
        # print(lo.json())
        # print('密码登录:[{},{},{}]'.format(lo.json()['code'], lo.json()['message'], lo.json()['data']['phone']))

        assert lo.json()['code'] == 0
        assert lo.json()['message'] == 'ok'
        assert lo.json()['data']['phone'] == param_data1['phone']

    def test_login4(self):
        """错误登录密码"""
        param_data2['password'] = 'yyyy3333'
        lo = requests.post(base_url2, json=param_data2, verify=False)
        # print(lo.json())

        assert lo.json()['code'] == '20009'
        assert lo.json()['message'] == '密码不正确'


if __name__ == '__main__':
    unittest.main()
