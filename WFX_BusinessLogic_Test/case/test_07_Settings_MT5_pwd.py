# -*- coding: utf-8 -*-
# @Time    : 2019/1/7 4:17 PM
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : test_07_Settings_MT5_pwd.py
# @Software: PyCharm

from common.ban_warning import *
from common.public_func import *
from common.myunit import StartEnd
import unittest
import requests


class SettingTest4(StartEnd):
    """MT5密码测试"""
    header = {
        "token": token()
    }

    r_mt5_pwd_u = 'https://ptest.wavehk.cn/v2/mt5/changePassowrdByOldPassword'
    r_mt5_pwd_p = {
        "apptype": "ios",
        "did": "12345dg",
        "new_password_two": "yyyy3333",
        "new_password_one": "yyyy3333",
        "sign": "5sCioY2cazwBz0aN\/Wa75yBvSXNe6v+tjP2W+lfH0bD5ri0imGGyzNc+uNK4YALc",
        "old_password": "qqqq1111",
        "version": "2.4.0"
    }
    r_mt5_pwd_p2 = {
        "apptype": "ios",
        "did": "12345dg",
        "new_password_two": "qqqq1111",
        "new_password_one": "qqqq1111",
        "sign": "5sCioY2cazwBz0aN\/Wa75yBvSXNe6v+tjP2W+lfH0bD5ri0imGGyzNc+uNK4YALc",
        "old_password": "yyyy3333",
        "version": "2.4.0"
    }

    def test_r_mt5_pwd1(self):
        """修改MT5密码"""
        lo = requests.post(self.r_mt5_pwd_u, json=self.r_mt5_pwd_p, headers=self.header, verify=False)
        # print(lo.json())
        assert_json(lo.json(), 'code', 0)
        assert_json(lo.json(), 'message', '修改密码成功')

    def test_r_mt5_pwd2(self):
        """还原"""
        lo = requests.post(self.r_mt5_pwd_u, json=self.r_mt5_pwd_p2, headers=self.header, verify=False)
        # print(lo.json())
        assert_json(lo.json(), 'code', 0)
        assert_json(lo.json(), 'message', '修改密码成功')

    def test_r_mt5_pwd3(self):
        """原密码错误"""
        self.r_mt5_pwd_p['old_password'] = '1'
        lo = requests.post(self.r_mt5_pwd_u, json=self.r_mt5_pwd_p, headers=self.header, verify=False)
        # print(lo.json())
        assert_json(lo.json(), 'code', 60000)
        assert_json(lo.json(), 'message', '旧密码错误')

    def test_r_mt5_pwd4(self):
        """原密码为空"""
        self.r_mt5_pwd_p['old_password'] = ''
        lo = requests.post(self.r_mt5_pwd_u, json=self.r_mt5_pwd_p, headers=self.header, verify=False)
        # print(lo.json())
        assert_json(lo.json(), 'code', 60000)
        assert_json(lo.json(), 'message', '旧密码错误')

    def test_r_mt5_pwd5(self):
        """新密码为空"""
        self.r_mt5_pwd_p['old_password'] = 'qqqq1111'
        self.r_mt5_pwd_p['new_password_one'] = ''
        self.r_mt5_pwd_p['new_password_two'] = ''
        lo = requests.post(self.r_mt5_pwd_u, json=self.r_mt5_pwd_p, headers=self.header, verify=False)
        # print(lo.json())
        assert_json(lo.json(), 'code', 20007)
        assert_json(lo.json(), 'message', '密码强度过弱,密码为8-15位字母、数字或符号组合')

    def test_r_mt5_pwd6(self):
        """新密码两次不一致"""
        self.r_mt5_pwd_p['old_password'] = 'qqqq1111'
        self.r_mt5_pwd_p['new_password_one'] = 'wwww1234'
        self.r_mt5_pwd_p['new_password_two'] = 'wwww1111'
        lo = requests.post(self.r_mt5_pwd_u, json=self.r_mt5_pwd_p, headers=self.header, verify=False)
        # print(lo.json())
        assert_json(lo.json(), 'code', 60000)
        assert_json(lo.json(), 'message', '两次输入的新密码不一致')

    def test_r_mt5_pwd7(self):
        """新密码不符合规则"""
        self.r_mt5_pwd_p['old_password'] = 'qqqq1111'
        self.r_mt5_pwd_p['new_password_one'] = '123456'
        self.r_mt5_pwd_p['new_password_two'] = '123456'
        lo = requests.post(self.r_mt5_pwd_u, json=self.r_mt5_pwd_p, headers=self.header, verify=False)
        # print(lo.json())
        assert_json(lo.json(), 'code', 20007)
        assert_json(lo.json(), 'message', '密码强度过弱,密码为8-15位字母、数字或符号组合')


class SettingTest4_1(StartEnd):
    header = {
        "token": token()
    }
    mt5_u = 'https://ptest.wavehk.cn/v2/user/ruleCode'
    mt5_p = {
        "type": "update",
        "apptype": "ios",
        "phone": "15013038819",
        "code": "1111",
        "did": "12345dg",
        "sign": "5sCioY2cazwBz0aN\/Wa759auMk+M3Yh\/bpyaUjt9PjbUngGF7JPCp57GLiYXI1xc",
        "version": "2.4.0",
        "mobile_fiex": "86"
    }

    mt5_u2 = 'https://ptest.wavehk.cn/v2/mt5/changePassWordByCode'
    mt5_p2 = {
        "code_token": "",
        "apptype": "ios",
        "did": "12345dg",
        "new_password_two": "qqqq1111",
        "new_password_one": "qqqq1111",
        "sign": "5sCioY2cazwBz0aN\/Wa7538CIvJ2CH8vIHEVU+jO9aAdKsUDAjhmCuzn8+N9DuNX",
        "version": "2.4.0"
    }

    def test_reset_mt5_pwd1(self):
        """重置mt5密码"""
        lo = requests.post(self.mt5_u, json=self.mt5_p, headers=self.header, verify=False)
        code_token = lo.json()['data']['code_token']
        self.mt5_p2['code_token'] = code_token
        lo2 = requests.post(self.mt5_u2, json=self.mt5_p2, headers=self.header, verify=False)
        # print(lo2.json())
        assert_json(lo2.json(), 'code', 0)
        assert_json(lo2.json(), 'message', '修改密码成功')

    def test_reset_mt5_pwd2(self):
        """验证码错误"""
        self.mt5_p['code'] = '2341'
        lo = requests.post(self.mt5_u, json=self.mt5_p, headers=self.header, verify=False)
        # print(lo.json())
        assert_json(lo.json(), 'code', 20004)
        assert_json(lo.json(), 'message', '验证码错误或已过期')

    def test_reset_mt5_pwd3(self):
        """使用其他手机进行修改"""
        self.mt5_p['phone'] = '15220035010'
        self.mt5_p['code'] = '1111'
        lo = requests.post(self.mt5_u, json=self.mt5_p, headers=self.header, verify=False)
        code_token = lo.json()['data']['code_token']
        self.mt5_p2['code_token'] = code_token
        lo2 = requests.post(self.mt5_u2, json=self.mt5_p2, headers=self.header, verify=False)
        print(lo2.json())
        assert_json(lo2.json(), 'code', 60000)
        assert_json(lo2.json(), 'message', '修改密码失败')

    def test_reset_mt5_pwd4(self):
        """密码为空/不符合规则"""
        self.mt5_p['phone'] = '15013038819'
        self.mt5_p['code'] = '1111'
        lo = requests.post(self.mt5_u, json=self.mt5_p, headers=self.header, verify=False)
        code_token = lo.json()['data']['code_token']
        self.mt5_p2['code_token'] = code_token
        self.mt5_p2['new_password_one'] = ''
        self.mt5_p2['new_password_two'] = ''
        lo2 = requests.post(self.mt5_u2, json=self.mt5_p2, headers=self.header, verify=False)
        # print(lo2.json())
        assert_json(lo2.json(), 'code', 20007)
        assert_json(lo2.json(), 'message', '密码强度过弱,密码为8-15位字母、数字或符号组合')


if __name__ == '__main__':
    unittest.main()
