# -*- coding: utf-8 -*-
# @Time    : 2019/2/15 2:47 PM
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : tiaoshi.py
# @Software: PyCharm

from common.ban_warning import *
import requests


def app_login():
    phone = ['15220035010', '15013038819']
    base_url1 = 'https://ptest.wavehk.cn/v2/user/ruleCode'

    param_data1 = {
        "type": "login",
        "code": "1111",
        "mobile_fiex": "86",
        "sign": "5sCioY2cazwBz0aN\/Wa75zO8S6VmRdPJkijw9NQVD2XnnYqpLFI0jymDr0nnJ6kl",
        "apptype": "ios",
        "phone": phone[1],
        "version": "2.4.0",
        "did": "12345dg"
    }

    lo = requests.post(base_url1, json=param_data1, verify=False)
    print(lo.json())
    return lo.json()


if __name__ == '__main__':
    pass
    # app_login()
