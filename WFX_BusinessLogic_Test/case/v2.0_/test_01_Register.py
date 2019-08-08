# -*- coding: utf-8 -*-
# @Time    : 2019/1/2 4:55 PM
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : test_01_Register.py
# @Software: PyCharm

from common.ban_warning import *
from test_db.test_db import db
from common.myunit import StartEnd
import unittest
import requests


class RegisterInit(StartEnd):
    """注册__init__"""

    # @unittest.skip('pass')
    def test_register99(self):
        """清除test_register6数据"""
        cur = db.cursor()
        sql_delete = "delete from t_users where email='y@126.com' or email='e@126.com'"
        try:
            cur.execute(sql_delete)  # 执行sql语句
            db.commit()
        except Exception as e:
            db.rollback()
        finally:
            db.close()  # 关闭连接
        print('清除数据----ok')

    # def test_02(self):
    #     print('b')


class RegisterOk(StartEnd):
    """注册"""
    base_url1 = 'https://ptest.wavehk.cn/v2/user/ruleCode'
    base_url2 = 'https://ptest.wavehk.cn/v2/user/setPwd'
    base_url3 = 'https://ptest.wavehk.cn/v2/user/uploadIdCard'
    base_url4 = 'https://ptest.wavehk.cn/v2/user/setTransactionPassWord'
    login = 'https://ptest.wavehk.cn/v1/user/login'

    header = {
        "token": ""
    }

    param_data1 = {
        "sign": "5sCioY2cazwBz0aN\/Wa755izJuPHKOXbB1wY3KHwmasOqvCmlTeLyYRsD4Mr\/F8d",
        "mobile_fiex": "86",
        "version": "2.2.1",
        "code": "1111",
        "apptype": "ios",
        "phone": "e@126.com",
        "type": "login",
        "did": "12345dg"
    }

    param_data2 = {
        "version": "2.2.1",
        "apptype": "ios",
        "code_token": "125aa95be9808546c7fc1c71f5456f61",
        "did": "12345dg",
        "sign": "5sCioY2cazwBz0aN\/Wa756ddsUIR4M4jjgmjZo6nPS0bFLl7vmmTsa87IhgWvPRe",
        "pwd": "yyy333"
    }

    param_data3 = {
        "idcard": "13922129963",
        "surname": "跃",
        "sign": "5sCioY2cazwBz0aN\/Wa7535iCPBV\/J1uZCFx7tALW5q1qS5xIONiPg5\/GuVS9eGb",
        "name": "神",
        "idcard2": "7505fd9e-c384-47ba-b993-41d5477b6d29",
        "version": "2.2.1",
        "type": "2",
        "apptype": "ios",
        "idcard1": "7425560a-56e8-4575-919e-d4607876253a",
        "did": "12345dg"
    }

    param_data4 = {
        "apptype": "ios",
        "password": "666666",
        "did": "12345dg",
        "sign": "5sCioY2cazwBz0aN\/Wa758JSX+45Vzv5czGwlkFTvZawHrBugm1H9BDSMBFeNRVv",
        "version": "2.2.1"
    }

    @unittest.skip('pass')
    def test_register7(self):
        """注册成功"""
        r1 = requests.post(self.base_url1, json=self.param_data1, verify=False)
        print(r1.json()['data']['code_token'])
        code_token = r1.json()['data']['code_token']
        print('===r1===')

        self.param_data2['code_token'] = code_token
        r2 = requests.post(self.base_url2, json=self.param_data2, verify=False)
        print(r2.json()['data']['token'])
        print('===r2===')

        token = r2.json()['data']['token']
        self.header['token'] = token
        r3 = requests.post(self.base_url3, json=self.param_data3, headers=self.header, verify=False)
        print(r3.json())
        print('===r3===')

        r4 = requests.post(self.base_url4, json=self.param_data4, headers=self.header, verify=False)
        print(r4.json())
        print('===r4===')


class RegisterTest(StartEnd):
    base_url1 = 'https://ptest.wavehk.cn/v2/user/ruleCode'
    base_url2 = 'https://ptest.wavehk.cn/v2/user/setPwd'
    base_url3 = 'https://ptest.wavehk.cn/v2/user/uploadIdCard'
    base_url4 = 'https://ptest.wavehk.cn/v2/user/setTransactionPassWord'
    login = 'https://ptest.wavehk.cn/v1/user/login'

    header = {
        "token": ""
    }

    param_data1 = {
        "sign": "5sCioY2cazwBz0aN\/Wa755izJuPHKOXbB1wY3KHwmasOqvCmlTeLyYRsD4Mr\/F8d",
        "mobile_fiex": "86",
        "version": "2.2.1",
        "code": "1111",
        "apptype": "ios",
        "phone": "e@126.com",
        "type": "login",
        "did": "12345dg"
    }

    param_data2 = {
        "version": "2.2.1",
        "apptype": "ios",
        "code_token": "125aa95be9808546c7fc1c71f5456f61",
        "did": "12345dg",
        "sign": "5sCioY2cazwBz0aN\/Wa756ddsUIR4M4jjgmjZo6nPS0bFLl7vmmTsa87IhgWvPRe",
        "pwd": "yyy333"
    }

    param_data3 = {
        "idcard": "13922129963",
        "surname": "跃",
        "sign": "5sCioY2cazwBz0aN\/Wa7535iCPBV\/J1uZCFx7tALW5q1qS5xIONiPg5\/GuVS9eGb",
        "name": "神",
        "idcard2": "7505fd9e-c384-47ba-b993-41d5477b6d29",
        "version": "2.2.1",
        "type": "2",
        "apptype": "ios",
        "idcard1": "7425560a-56e8-4575-919e-d4607876253a",
        "did": "12345dg"
    }

    param_data4 = {
        "apptype": "ios",
        "password": "666666",
        "did": "12345dg",
        "sign": "5sCioY2cazwBz0aN\/Wa758JSX+45Vzv5czGwlkFTvZawHrBugm1H9BDSMBFeNRVv",
        "version": "2.2.1"
    }

    # @unittest.skip('pass')
    def test_register1(self):
        """验证错误"""
        self.param_data1['code'] = '2222'
        r1 = requests.post(self.base_url1, json=self.param_data1, verify=False)
        # print(r1.json())
        assert r1.json()['code'] == 20004
        assert r1.json()['message'] == '验证码错误或已过期'
        self.param_data1['code'] = '1111'

    # @unittest.skip('pass')
    def test_register2(self):
        """手机号已存在"""
        self.param_data1['phone'] = '15013038819'
        r1 = requests.post(self.base_url1, json=self.param_data1, verify=False)
        # print(r1.json())
        assert r1.json()['code'] == 0
        assert r1.json()['message'] == 'ok'

    # @unittest.skip('pass')
    def test_register3(self):
        """邮箱已存在"""
        self.param_data1['phone'] = 'yang6333yyx@126.com'
        r1 = requests.post(self.base_url1, json=self.param_data1, verify=False)
        # print(r1.json())
        assert r1.json()['code'] == 0
        assert r1.json()['message'] == 'ok'
        self.param_data1['phone'] = 'e@126.com'

    # @unittest.skip('pass')
    def test_register4(self):
        """不符合规则的密码"""
        self.param_data2['pwd'] = 'yyy33'
        r1 = requests.post(self.base_url1, json=self.param_data1, verify=False)
        print(r1.json()['data']['code_token'])
        code_token = r1.json()['data']['code_token']

        self.param_data2['code_token'] = code_token
        r2 = requests.post(self.base_url2, json=self.param_data2, verify=False)
        # print(r2.json())
        assert r2.json()['code'] == 20007
        assert r2.json()['message'] == '密码强度过弱,密码为6-15位字母、数字或符号组合'

    # @unittest.skip('pass')
    def test_register5(self):
        """密码为空"""
        self.param_data2['pwd'] = ''
        r1 = requests.post(self.base_url1, json=self.param_data1, verify=False)
        print(r1.json()['data']['code_token'])
        code_token = r1.json()['data']['code_token']

        self.param_data2['code_token'] = code_token
        r2 = requests.post(self.base_url2, json=self.param_data2, verify=False)
        # print(r2.json())
        assert r2.json()['code'] == 20007
        assert r2.json()['message'] == '密码强度过弱,密码为6-15位字母、数字或符号组合'

    # @unittest.skip('pass')
    def test_register6(self):
        """不符合规则的交易密码"""
        self.param_data1['phone'] = 'y@126.com'
        self.param_data2['pwd'] = 'yyy333'
        self.param_data3['idcard'] = '87254091'
        self.param_data3['surname'] = 'G'
        self.param_data3['name'] = 'G'
        self.param_data4['password'] = 'yyyyyy'
        r = requests.post(self.base_url1, json=self.param_data1, verify=False)
        # print(r1.json()['data']['code_token'])
        code_token = r.json()['data']['code_token']

        self.param_data2['code_token'] = code_token
        r2 = requests.post(self.base_url2, json=self.param_data2, verify=False)
        # print(r2.json()['data']['token'])

        token = r2.json()['data']['token']
        self.header['token'] = token
        r3 = requests.post(self.base_url3, json=self.param_data3, headers=self.header, verify=False)
        # print(r3.json())

        r4 = requests.post(self.base_url4, json=self.param_data4, headers=self.header, verify=False)
        # print(r4.json())
        assert r4.json()['code'] == 6001
        assert r4.json()['message'] == '交易密码必须6位数字'


if __name__ == '__main__':
    unittest.main()
