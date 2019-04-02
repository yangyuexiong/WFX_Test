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


"""
analystId	272
amount	2000.0
analystProfits[0].date	20190301
analystProfits[0].profit	1.0
analystProfits[1].date	20190302
analystProfits[1].profit	2

"""

x1 = [x * x for x in range(1, 11) if x % 2 == 0]
print(x1)

l = []
for x in range(1, 11):
    if x % 2 == 0:
        l.append(x * x)
print(l)


def xxx(x):
    return x + 1


print(xxx(2))

f = lambda x: x + 1
print(f(2))

import profile
import cProfile

"""
ncall：函数运行次数

tottime： 函数的总的运行时间，减去函数中调用子函数的运行时间

第一个percall：percall = tottime / nclall 

cumtime:函数及其所有子函数调整的运行时间，也就是函数开始调用到结束的时间。

第二个percall：percall = cumtime / nclall 

"""

if __name__ == '__main__':
    pass
    # cProfile.run('app_login()')
    # app_login()
