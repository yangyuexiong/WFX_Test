# -*- coding: utf-8 -*-
# @Time    : 2019-07-17 15:44
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : dataReady.py
# @Software: PyCharm

from common.ban_warning import *
import requests
import random
from time import sleep

phone = 15012345600  # 注册号码递增 1
n = 1  # 名称标示
email_f_name = 1  # 邮箱前缀递增 1
login_phone = 15012345600  # 登录账号 递增1
add_mt5 = 1
c = []
m = []


def register():
    global n
    global phone
    u1 = 'https://ptest.wavehk.cn/v2/user/ruleCode'
    u2 = 'https://ptest.wavehk.cn/v2/user/setPwd'
    u3 = 'https://ptest.wavehk.cn/v2/user/uploadIdCard'
    u4 = 'https://ptest.wavehk.cn/v2/user/setTransactionPassWord'

    header = {
        "source": 'bl',
        "token": ""
    }

    d1 = {
        "sign": "5sCioY2cazwBz0aN\/Wa75yuma7Zgz6237oxESWgqTTNXOTT4J27ebGWFhWFCrufQ",
        "type": "login",
        "mobile_fiex": "86",
        "apptype": "ios",
        "code": "1111",
        "version": "3.0",
        "did": "12345dg",
        "phone": str(phone)
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
        "idcard": random.randint(111111111, 999999999),
        "version": "3.0",
        "apptype": "ios",
        "surname": "测",
        "idcard1": "8533148f-b146-4b0f-9a6c-b81562432aad",
        "sign": "5sCioY2cazwBz0aN\/Wa75\/MhFk0ldE0iX8+v0od\/oCEcFgdI2GgVtbRz\/tPqNi34",
        "name": str(n),
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

    n += 1
    phone += 1


def login():
    global login_phone
    u = 'https://ptest.wavehk.cn/v2/user/ruleCode'
    header = {
        "source": 'bl',
        "token": ""
    }
    d = {
        "type": "login",
        "apptype": "ios",
        "version": "3.0",
        "phone": login_phone,
        "code": "1111",
        "mobile_fiex": "86",
        "sign": "5sCioY2cazwBz0aN\/Wa7508NxsJZjheLwrb+zdDzlPR3psYC\/v7c83mdCd9JlkV1",
        "did": "12345dg"
    }
    r = requests.post(u, json=d, headers=header, verify=False)
    login_phone += 1
    return r.json()['data']['token']


def bind_mail():
    global email_f_name

    u = 'https://ptest.wavehk.cn/v1/user/setEmail'

    header = {
        "source": 'bl',
        "token": login()
    }
    d = {
        "did": "12345dg",
        "sign": "5sCioY2cazwBz0aN\/Wa758e1jelPUPhyGGLg5cny1MAworSfMyFu5rbqaCoeSZ9u",
        "code": "1111",
        "apptype": "ios",
        "version": "3.0",
        "email": "{}@126.com".format(email_f_name),
        "code_token": ""
    }

    r = requests.post(u, json=d, headers=header, verify=False)
    print(r.json())
    email_f_name += 1


def register_mt5_real():
    global add_mt5
    u = 'https://ptest.wavehk.cn/v2/mt5/addUser'

    header = {
        "source": 'bl',
        "token": login()
    }

    d = {
        "email": "{}@126.com".format(add_mt5),
        "sign": "5sCioY2cazwBz0aN\/Wa75+gj4kg1eeHCCZC2qn1SQXoSVG2oFccArrBQGilJu\/8u",
        "apptype": "ios",
        "accounttype": "real",
        "did": "12345dg",
        "version": "3.0"
    }
    r = requests.post(u, json=d, headers=header, verify=False)
    print(r.json())
    add_mt5 += 1


def mt5_admin():
    s = requests.Session()
    u = 'https://plan.dvcfx.com:448/user/login'
    d = {
        'account': 'admin',
        'password': 'admin123'

    }
    r = s.post(u, data=d, verify=False)
    print(r.json())

    return s


def mt5_get_test_list(req):
    u = 'https://plan.dvcfx.com:448/client/listPage'
    d = {
        'pageSize': 100,
        'pageNum': 1,
        'dateType': 0,
        'dateStart': ' 2019-07-17',
        'dateEnd': '2019-07-18',
        'columnKey': 'name',
        'columnValue': '测'
    }
    r = req.post(u, data=d, verify=False)
    # print(r.json()['data']['list'])
    test_user_list = r.json()['data']['list']
    return test_user_list


def mt5_recharge(req):
    global c
    global m
    u = 'https://plan.dvcfx.com:448/moneyIO/addMoneyInOut'
    print(c)
    print(m)
    d = {
        'clientId': c[0],
        'mt5Id': m[0],
        'type': 1,
        'payType': '电汇',
        'amountUsd': 1000,
        'amountCny': 6.75,
        'remark': '测试',
        'payRate': 6.75,
        'invoiceImgId': 407
    }
    r = req.post(u, data=d, verify=False)
    print(r.json())
    c.pop(0)
    m.pop(0)


if __name__ == '__main__':
    pass
    ''' 数据准备 
    
    # 注册账号
    # for i in range(0, 21):
    #     register()

    # 绑定邮箱
    # for i in range(0, 21):
    #     bind_mail()

    # 开通MT5账号
    # for i in range(0, 20):
    #   register_mt5_real()
    
    '''

    # mt5后台登录
    r = mt5_admin()

    # mt5后台登录并且获取测试账号list
    clientId = [i['id'] for i in mt5_get_test_list(r)]
    mt5Id = [i['mt5Id'] for i in mt5_get_test_list(r)]
    # print(clientId)
    # print(mt5Id)
    c = clientId
    m = mt5Id

    # 充值
    r = mt5_admin()
    for i in range(0, 20):
        sleep(0.7)
        mt5_recharge(r)
