# -*- coding: utf-8 -*-
# @Time    : 2019-07-24 11:37
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : test_001_Register.py
# @Software: PyCharm

from all_import import *


class RegisterOk(StartEnd):
    """注册"""

    def test_register(self):
        """111"""
        print(self)
        u1 = 'https://ptest.wavehk.cn/v2/user/ruleCode'
        u2 = 'https://ptest.wavehk.cn/v2/user/setPwd'
        u3 = 'https://ptest.wavehk.cn/v2/user/uploadIdCard'
        u4 = 'https://ptest.wavehk.cn/v2/user/setTransactionPassWord'

        d1 = {
            "sign": "5sCioY2cazwBz0aN\/Wa75yuma7Zgz6237oxESWgqTTNXOTT4J27ebGWFhWFCrufQ",
            "type": "login",
            "mobile_fiex": "86",
            "apptype": "ios",
            "code": "1111",
            "version": "3.0",
            "did": "12345dg",
            "phone": str(register_phone)
        }

        d2 = {
            "sign": "5sCioY2cazwBz0aN\/Wa75\/gKRon7gQTxqe4dWCTkb78n5ke73L7uNprEihBAQsR6",
            "did": "12345dg",
            "prrv": "AppStore",
            "apptype": "ios",
            "version": "3.0",
            "code_token": "",
            "pwd": "yyy333"
        }

        d3 = {
            "idcard": '',
            "version": "3.0",
            "apptype": "ios",
            "surname": "测",
            "idcard1": "8533148f-b146-4b0f-9a6c-b81562432aad",
            "sign": "5sCioY2cazwBz0aN\/Wa75\/MhFk0ldE0iX8+v0od\/oCEcFgdI2GgVtbRz\/tPqNi34",
            "name": '',
            "idcard2": "a87308f2-eb32-4eda-a223-ed8e5b54b1af",
            "did": "12345dg",
            "type": "5"
        }

        d4 = {
            "did": "12345dg",
            "password": "666666",
            "version": "3.0",
            "sign": "5sCioY2cazwBz0aN\/Wa759eYSUvw\/IqF57LLxzCkPmma2xkoBAVCGa46\/+ow1wP7",
            "apptype": "ios"
        }
        r1 = requests.post(u1, json=d1, headers=header, verify=False)
        print(r1.json())
        print(r1.json()['data']['code_token'])

        d2['code_token'] = r1.json()['data']['code_token']
        r2 = requests.post(u2, json=d2, headers=header, verify=False)
        print(r2.json())

        header['token'] = r2.json()['data']['token']
        r3 = requests.post(u3, json=d3, headers=header, verify=False)
        print(r3.json())

        r4 = requests.post(u4, json=d4, headers=header, verify=False)
        print(r4.json())


if __name__ == '__main__':
    pass
