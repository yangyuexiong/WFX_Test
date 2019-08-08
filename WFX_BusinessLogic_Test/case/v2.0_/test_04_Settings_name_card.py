# -*- coding: utf-8 -*-
# @Time    : 2019/1/7 10:00 AM
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : test_04_Settings_name_card.py
# @Software: PyCharm

from common.ban_warning import *
from common.public_func import *
from common.myunit import StartEnd
import unittest
import requests


class SettingTest1(StartEnd):
    """设置项测试"""
    setnickname_u = 'https://ptest.wavehk.cn/v1/user/setNickname'
    setnickname_j = {
        "nickname": "OKc01",
        "apptype": "ios",
        "version": "2.4.0",
        "sign": "5sCioY2cazwBz0aN\/Wa75yJC3Gj5dvONHh7Y4Lf2rrs59yqzmqt5Y8KheXxnTz2f",
        "did": "12345dg"
    }
    token = token()
    header = {
        "token": token
    }

    newCard_u = 'https://ptest.wavehk.cn/v1/bankcard/newCard'
    newCard_j = {
        "did": "12345dg",
        "bankname": "",
        "province": "广东省",
        "bankcard": "6227003320620176059",
        "version": "2.4.0",
        "bankaddress": "先烈支行",
        "contact": "",
        "type": 0,
        "swift_code": "",
        "apptype": "ios",
        "phone": "15013038819",
        "bankid": "",
        "opencard_code": "",
        "sign": "5sCioY2cazwBz0aN\/Wa759XSvEgXhkLj3uwQZ6WYVUcQXClWSycfDOBJLMq6tcu2"
    }

    remove_u = 'https://ptest.wavehk.cn/v1/bankcard/remove'
    remove_j = {
        "did": "12345dg",
        "bankname": "",
        "province": "",
        "bankcard": "",
        "version": "2.4.0",
        "bankaddress": "",
        "contact": "",
        "type": 0,
        "swift_code": "",
        "apptype": "ios",
        "phone": "",
        "bankid": '',
        "opencard_code": "",
        "sign": "5sCioY2cazwBz0aN\/Wa75zgHq\/PrTImlu4a2I4U7Bs001pjWSgfDSI9XxXMRjYdj"
    }

    def test_nickname1(self):
        """修改昵称"""
        lo = requests.post(self.setnickname_u, json=self.setnickname_j, headers=self.header, verify=False)
        print(lo.json())
        assert_json(lo.json(), 'code', 0)
        assert_json(lo.json(), 'message', 'ok')

    def test_nickname2(self):
        """违规昵称"""
        self.setnickname_j['nickname'] = 'Y-Y'
        lo = requests.post(self.setnickname_u, json=self.setnickname_j, headers=self.header, verify=False)
        assert_json(lo.json(), 'code', 20018)
        assert_json(lo.json(), 'message', '昵称包含2-16个字符，支持中英文、数字')

    def test_nickname3(self):
        """昵称为空"""
        self.setnickname_j['nickname'] = ''
        lo = requests.post(self.setnickname_u, json=self.setnickname_j, headers=self.header, verify=False)
        assert_json(lo.json(), 'code', 20018)
        assert_json(lo.json(), 'message', '昵称包含2-16个字符，支持中英文、数字')

    def test_bankcards1(self):
        """中国银行卡绑定"""
        lo = requests.post(self.newCard_u, json=self.newCard_j, headers=self.header, verify=False)
        print(lo.json())
        assert_json(lo.json(), 'code', 0)
        assert_json(lo.json(), 'message', '添加成功')

        msg = get_msg(self.token)['data'][0]['content']
        assert msg == '你已成功为银行卡尾号%s的卡片进行绑定' % self.newCard_j['bankcard'][-4:]

    def test_bankcards2(self):
        """已绑定"""
        lo = requests.post(self.newCard_u, json=self.newCard_j, headers=self.header, verify=False)
        # print(lo.json())
        assert_json(lo.json(), 'code', 10000)
        assert_json(lo.json(), 'message', '该银行卡已绑定')

    def test_bankcards3(self):
        """解绑"""
        getBankcards_u = 'https://ptest.wavehk.cn/v1/bankcard/getBankcards'
        getBankcards_j = {
            "apptype": "ios",
            "version": "2.4.0",
            "sign": "5sCioY2cazwBz0aN\/Wa75xoTM8NgYnLq0pM3P2fPcNsPJoyGNj9NzCzSGexlk\/gi",
            "did": "12345dg"
        }
        lo = requests.post(getBankcards_u, json=getBankcards_j, headers=self.header, verify=False)
        # print(lo.json())
        self.remove_j['bankid'] = lo.json()['data'][0]['bankid']

        lo = requests.post(self.remove_u, json=self.remove_j, headers=self.header, verify=False)
        # print(lo.json())
        assert_json(lo.json(), 'code', 0)
        assert_json(lo.json(), 'message', '解绑成功')

    def test_bankcards4(self):
        """银行卡信息错误"""
        self.newCard_j['bankcard'] = '6227003320620176051'
        # self.newCard_j['phone'] = '15220035010'
        lo = requests.post(self.newCard_u, json=self.newCard_j, headers=self.header, verify=False)
        # print(lo.json())
        assert_json(lo.json(), 'code', 30002)
        assert_json(lo.json(), 'message', '你的银行卡持卡人信息不正确(请检查姓名、身份证、银行卡、预留电话是否一致)')

    def test_bankcards5(self):
        """银行卡为空"""
        self.newCard_j['bankcard'] = ''
        lo = requests.post(self.newCard_u, json=self.newCard_j, headers=self.header, verify=False)
        # print(lo.json())
        assert_json(lo.json(), 'code', 10000)
        assert_json(lo.json(), 'message', '请输入银行卡卡号')

    def test_bankcards6(self):
        """手机号为空"""
        self.newCard_j['phone'] = ''
        lo = requests.post(self.newCard_u, json=self.newCard_j, headers=self.header, verify=False)
        # print(lo.json())
        assert_json(lo.json(), 'code', 10000)
        assert_json(lo.json(), 'message', '请输入手机号码')


if __name__ == '__main__':
    unittest.main()
