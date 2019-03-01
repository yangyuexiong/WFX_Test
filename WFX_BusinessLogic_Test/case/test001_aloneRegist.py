# -*- coding: utf-8 -*-
# @Time    : 2019/2/15 2:06 PM
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : test001_aloneRegist.py
# @Software: PyCharm


from common.ban_warning import *
from test_db.test_db import db
from common.myunit import StartEnd
import unittest
import requests

"""单独注册"""

base_url1 = 'https://ptest.wavehk.cn/v2/user/ruleCode'
base_url2 = 'https://ptest.wavehk.cn/v2/user/setPwd'
base_url3 = 'https://ptest.wavehk.cn/v2/user/uploadIdCard'
base_url4 = 'https://ptest.wavehk.cn/v2/user/setTransactionPassWord'

p1 = {
    "pwd": "yyy333",
    "apptype": "ios",
    "did": "12345dg",
    "version": "2.5.0",
    "code_token": "25292972a56cd8f01b8a23706c10e62a",
    "sign": "5sCioY2cazwBz0aN\/Wa75xmy9tm25SqmuKujlEtn6G4qO4NsdJOr3ny9BnJFHq8L"
}

p2 = {
    "pwd": "yyy333",
    "apptype": "ios",
    "did": "12345dg",
    "version": "2.5.0",
    "code_token": "25292972a56cd8f01b8a23706c10e62a",
    "sign": "5sCioY2cazwBz0aN\/Wa75xmy9tm25SqmuKujlEtn6G4qO4NsdJOr3ny9BnJFHq8L"
}

p3 = {
    "surname": "Y",
    "idcard1": "0112fe0c-0ad8-4524-b64e-bb3a9731fe06",
    "apptype": "ios",
    "sign": "5sCioY2cazwBz0aN\/Wa75zdHhQJ0G9CPQn8eic\/xz+DR5NbAVmZZBIV0a0he8ccl",
    "name": "Y",
    "idcard2": "ac19d2e3-f10a-480c-9433-120bbe52615b",
    "idcard": "709394",
    "type": "2",
    "version": "2.5.0",
    "did": "12345dg"
}

p4 = {
    "apptype": "ios",
    "password": "666666",
    "did": "12345dg",
    "version": "2.5.0",
    "sign": "5sCioY2cazwBz0aN\/Wa75wfeQw+1\/QAOfzxW7oh1mmGA12blNNk2bUqyQPlhFIfM"
}

header = {
    'token': ''
}


@unittest.skip('pass')
def test_register7():
    """注册成功"""
    r1 = requests.post(base_url1, json=p1, verify=False)
    print(r1.json()['data']['code_token'])
    code_token = r1.json()['data']['code_token']

    p2['code_token'] = code_token
    r2 = requests.post(base_url2, json=p2, verify=False)
    print(r2.json()['data']['token'])

    token = r2.json()['data']['token']
    header['token'] = token
    r3 = requests.post(base_url3, json=p3, headers=header, verify=False)
    print(r3.json())

    r4 = requests.post(base_url4, json=p4, headers=header, verify=False)
    print(r4.json())


if __name__ == '__main__':
    unittest.main()
