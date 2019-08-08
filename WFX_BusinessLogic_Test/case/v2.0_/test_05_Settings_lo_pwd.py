# -*- coding: utf-8 -*-
# @Time    : 2019/1/7 2:48 PM
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : test_05_Settings_lo_pwd.py
# @Software: PyCharm

from common.ban_warning import *
from common.public_func import *
from common.myunit import StartEnd
import unittest
import requests


class SettingTest2(StartEnd):
    """用户密码测试"""
    header = {
        "token": token()
    }
    edit_password_u = 'https://ptest.wavehk.cn/v1/user/editPassword'
    edit_password_p = {
        "old": "yyy333",
        "repassword": "qqq111",
        "apptype": "ios",
        "sign": "5sCioY2cazwBz0aN\/Wa75zS7XaF74EGPjE3uTfBUu2TIRZc1j4aR051AvQe6pgmM",
        "did": "12345dg",
        "key": "",
        "version": "2.4.0",
        "password": "qqq111"
    }

    edit_password_p2 = {
        "old": "qqq111",
        "repassword": "yyy333",
        "apptype": "ios",
        "sign": "5sCioY2cazwBz0aN\/Wa75zS7XaF74EGPjE3uTfBUu2TIRZc1j4aR051AvQe6pgmM",
        "did": "12345dg",
        "key": "",
        "version": "2.4.0",
        "password": "yyy333"
    }

    r_pwd_u1 = 'https://ptest.wavehk.cn/v2/user/ruleCode'
    r1 = {
        "code": "1111",
        "apptype": "ios",
        "sign": "5sCioY2cazwBz0aN\/Wa759\/5pZ+NSm+Rcj1hXiS0\/5Zo7YNoHr7IxFmznL1L5Xkh",
        "did": "12345dg",
        "phone": "15013038819",
        "mobile_fiex": "86",
        "type": "forget",
        "version": "2.4.0"
    }

    r_pwd_u2 = 'https://ptest.wavehk.cn/v2/user/setPwd'
    r2 = {
        "code_token": "",
        "apptype": "ios",
        "version": "2.4.0",
        "sign": "5sCioY2cazwBz0aN\/Wa759qZYj1Nlgwd9FM0fCW2Bo7SWVGAUVpEDaFLeLNCO8Cu",
        "did": "12345dg",
        "pwd": "yyy333"
    }

    def test_login_pwd1(self):
        """登录密码修改"""
        lo = requests.post(self.edit_password_u, json=self.edit_password_p, headers=self.header, verify=False)
        # print(lo.json())
        assert_json(lo.json(), 'code', 0)
        assert_json(lo.json(), 'message', '修改成功')

    def test_login_pwd2(self):
        """还原密码便于下次再次执行用例"""
        lo = requests.post(self.edit_password_u, json=self.edit_password_p2, headers=self.header, verify=False)
        # print(lo.json())
        assert_json(lo.json(), 'code', 0)
        assert_json(lo.json(), 'message', '修改成功')

    def test_login_pwd3(self):
        """原密码错误"""
        self.edit_password_p['old'] = 'yyyyy11111'
        lo = requests.post(self.edit_password_u, json=self.edit_password_p, headers=self.header, verify=False)
        # print(lo.json())
        assert_json(lo.json(), 'code', 20012)
        assert_json(lo.json(), 'message', '原始密码不正确')

    def test_login_pwd4(self):
        """原密码为空"""
        self.edit_password_p['old'] = ''
        lo = requests.post(self.edit_password_u, json=self.edit_password_p, headers=self.header, verify=False)
        # print(lo.json())
        assert_json(lo.json(), 'code', 10000)
        assert_json(lo.json(), 'message', '请输入原始密码')

    def test_login_pwd5(self):
        """两次新密码不一致"""
        self.edit_password_p['old'] = 'yyy333'
        self.edit_password_p['password'] = 'ccc125'
        self.edit_password_p['repassword'] = 'ccc122'
        lo = requests.post(self.edit_password_u, json=self.edit_password_p, headers=self.header, verify=False)
        # print(lo.json())
        assert_json(lo.json(), 'code', 20010)
        assert_json(lo.json(), 'message', '确认密码跟设置密码不一致')

    def test_login_pwd6(self):
        """新密码不规范"""
        self.edit_password_p['old'] = 'yyy333'
        self.edit_password_p['password'] = 'ccc12'
        self.edit_password_p['repassword'] = 'ccc12'
        lo = requests.post(self.edit_password_u, json=self.edit_password_p, headers=self.header, verify=False)
        assert_json(lo.json(), 'code', 20007)
        assert_json(lo.json(), 'message', '密码强度过弱,密码为6-15位字母、数字或符号组合')

    def test_login_pwd7(self):
        """新密码为空"""
        self.edit_password_p['old'] = 'yyy333'
        self.edit_password_p['password'] = ''
        self.edit_password_p['repassword'] = ''
        lo = requests.post(self.edit_password_u, json=self.edit_password_p, headers=self.header, verify=False)
        # print(lo.json())
        assert_json(lo.json(), 'code', 10000)
        assert_json(lo.json(), 'message', '请输入密码')

    def test_login_pwd8(self):
        """全部为空"""
        self.edit_password_p['old'] = ''
        self.edit_password_p['password'] = ''
        self.edit_password_p['repassword'] = ''
        lo = requests.post(self.edit_password_u, json=self.edit_password_p, headers=self.header, verify=False)
        # print(lo.json())
        assert_json(lo.json(), 'code', 10000)
        assert_json(lo.json(), 'message', '请输入原始密码')

    def test_r_pwd1(self):
        """重置登录密码"""
        lo = requests.post(self.r_pwd_u1, json=self.r1, headers=self.header, verify=False)
        code_token = lo.json()['data']['code_token']
        self.r2['code_token'] = code_token
        lo2 = requests.post(self.r_pwd_u2, json=self.r2, headers=self.header, verify=False)
        # print(lo2.json())
        assert_json(lo2.json(), 'code', 0)
        assert_json(lo2.json(), 'message', '修改成功')

    def test_r_pwd2(self):
        """重置的密码不规范"""
        lo = requests.post(self.r_pwd_u1, json=self.r1, headers=self.header, verify=False)
        code_token = lo.json()['data']['code_token']
        self.r2['code_token'] = code_token
        self.r2['pwd'] = 'yyy33'
        lo2 = requests.post(self.r_pwd_u2, json=self.r2, headers=self.header, verify=False)
        # print(lo2.json())
        assert_json(lo2.json(), 'code', 20007)
        assert_json(lo2.json(), 'message', '密码强度过弱,密码为6-15位字母、数字或符号组合')

    def test_r_pwd3(self):
        """密码为空"""
        lo = requests.post(self.r_pwd_u1, json=self.r1, headers=self.header, verify=False)
        code_token = lo.json()['data']['code_token']
        self.r2['code_token'] = code_token
        self.r2['pwd'] = ''
        lo2 = requests.post(self.r_pwd_u2, json=self.r2, headers=self.header, verify=False)
        # print(lo2.json())
        assert_json(lo2.json(), 'code', 20007)
        assert_json(lo2.json(), 'message', '密码强度过弱,密码为6-15位字母、数字或符号组合')

    def test_r_pwd4(self):
        """重置登录密码 错误验证码"""
        self.r1['code'] = '2222'
        lo = requests.post(self.r_pwd_u1, json=self.r1, headers=self.header, verify=False)
        # print(lo.json())
        assert_json(lo.json(), 'code', 20004)
        assert_json(lo.json(), 'message', '验证码错误或已过期')


if __name__ == '__main__':
    unittest.main()
