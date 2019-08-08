# -*- coding: utf-8 -*-
# @Time    : 2019/1/11 11:37 AM
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : test_09_Transaction.py
# @Software: PyCharm

from common.ban_warning import *
from common.public_func import *
from common.myunit import StartEnd
import unittest
import requests


@unittest.skip('pass_09')
class TransactionTest(StartEnd):
    header = {
        'token': token()
    }
    # 开仓
    o_u = 'https://ptest.wavehk.cn/v2/mt5/openingPosition'
    o_p = {
        "sl": "",
        "tp": "",
        "volume": "1.0",
        "did": "12345dg",
        "symbol": "XAUUSD",
        "tradecmd": "0",
        "apptype": "ios",
        "version": "2.5",
        "comment": "",
        "sign": "5sCioY2cazwBz0aN\/Wa75\/cJZu7qDvAGA+sQBCVXNpU93tIlJ7zNTVxv2551YbOC"
    }
    # 平仓
    o_c_u = 'https://ptest.wavehk.cn/v2/mt5/closePosition'
    o_c_p = {
        "did": "12345dg",
        "order": '',
        "apptype": "ios",
        "sign": "5sCioY2cazwBz0aN\/Wa752wKMczWQfMYsK5Q7BKm02Zh1Rw7do0\/bbNsAzDaI1Sb",
        "version": "2.5"
    }

    def test_transaction1(self):
        """开仓"""

        lo = requests.post(self.o_u, json=self.o_p, headers=self.header, verify=False)
        print(lo.json())
        assert_json(lo.json(), 'code', 0)
        assert_json(lo.json(), 'message', '获取数据成功')
        print(str(lo.json()['data']['orderId']))
        self.o_c_p['order'] = str(lo.json()['data']['orderId'])

    def test_transaction2(self):
        """数据断言"""

    def test_transaction3(self):
        """平仓"""
        # lo = requests.post(self.o_c_u, json=self.o_c_p, headers=self.header, verify=False)
        # print(lo.json())


if __name__ == '__main__':
    unittest.main()
