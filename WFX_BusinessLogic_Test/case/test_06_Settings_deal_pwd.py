# -*- coding: utf-8 -*-
# @Time    : 2019/1/7 3:35 PM
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : test_06_Settings_deal_pwd.py
# @Software: PyCharm

from common.ban_warning import *
from common.public_func import *
from common.myunit import StartEnd
import unittest
import requests


class SettingTest3(StartEnd):
    """交易密码测试"""
    header = {
        "token": token()
    }
    update_deal_u = 'https://ptest.wavehk.cn/v2/user/updateTransactionPassWord'
    update_deal_p = {
        "password": "777777",
        "apptype": "ios",
        "version": "2.4.0",
        "sign": "5sCioY2cazwBz0aN\/Wa750DZGR4cHcgrS3Vf8lxdNbFXBzCTpH\/34eLx9PYGOjbn",
        "did": "12345dg",
        "formerly_password": "666666"
    }
    update_deal_p2 = {
        "password": "666666",
        "apptype": "ios",
        "version": "2.4.0",
        "sign": "5sCioY2cazwBz0aN\/Wa750DZGR4cHcgrS3Vf8lxdNbFXBzCTpH\/34eLx9PYGOjbn",
        "did": "12345dg",
        "formerly_password": "777777"
    }

    r_deal_pwd_u = 'https://ptest.wavehk.cn/v2/user/getResetCode'
    r_deal_pwd_p = {
        "idcard": "44010219940219361X",
        "version": "2.4.0",
        "apptype": "ios",
        "sign": "5sCioY2cazwBz0aN\/Wa75\/SKYwRGA3EvER9p058FxRKg+zJwn8SG3eL46shNGwh8",
        "code": "4031",
        "did": "12345dg"
    }

    r_deal_pwd_u2 = 'https://ptest.wavehk.cn/v2/user/getResetCode'
    r_deal_pwd_p2 = {
        "version": "2.4.0",
        "apptype": "ios",
        "password": "666666",
        "sign": "5sCioY2cazwBz0aN\/Wa75wEO4u7gyUj9qFWYiHNfA4lCGHyPHADflez7RjwYTb4J",
        "did": "12345dg"
    }

    def test_deal_pwd1(self):
        """修改交易密码"""
        lo = requests.post(self.update_deal_u, json=self.update_deal_p, headers=self.header, verify=False)
        # print(lo.json())
        assert_json(lo.json(), 'code', 0)
        assert_json(lo.json(), 'message', '修改成功')

    def test_deal_pwd2(self):
        """还原"""
        lo = requests.post(self.update_deal_u, json=self.update_deal_p2, headers=self.header, verify=False)
        assert_json(lo.json(), 'code', 0)
        assert_json(lo.json(), 'message', '修改成功')

    def test_deal_pwd3(self):
        """原密码错误"""
        self.update_deal_p['formerly_password'] = '111111'
        lo = requests.post(self.update_deal_u, json=self.update_deal_p, headers=self.header, verify=False)
        # print(lo.json())
        assert_json(lo.json(), 'code', 20013)
        assert_json(lo.json(), 'message', '原密码不正确')

    def test_deal_pwd4(self):
        """新密码不符合规则"""
        self.update_deal_p['formerly_password'] = '666666'
        self.update_deal_p['password'] = '3333333'
        lo = requests.post(self.update_deal_u, json=self.update_deal_p, headers=self.header, verify=False)
        # print(lo.json())
        assert_json(lo.json(), 'code', 6001)
        assert_json(lo.json(), 'message', '交易密码必须6位数字')

    def test_deal_pwd5(self):
        """新密码为空"""
        self.update_deal_p['password'] = ''
        lo = requests.post(self.update_deal_u, json=self.update_deal_p, headers=self.header, verify=False)
        # print(lo.json())
        assert_json(lo.json(), 'code', 6001)
        assert_json(lo.json(), 'message', '交易密码必须6位数字')

    def test_deal_pwd6(self):
        """全部为空"""
        self.update_deal_p['formerly_password'] = ''
        self.update_deal_p['password'] = ''
        lo = requests.post(self.update_deal_u, json=self.update_deal_p, headers=self.header, verify=False)
        # print(lo.json())
        assert_json(lo.json(), 'code', 6001)
        assert_json(lo.json(), 'message', '交易密码必须6位数字')

    @unittest.skip('缺少万能验证码')
    def test_r_deal_pwd1(self):
        """重置交易密码"""
        # lo = requests.post(self.r_deal_pwd_u2, json=self.r_deal_pwd_p2, headers=self.header, verify=False)
        # print(lo.json())


if __name__ == '__main__':
    unittest.main()
