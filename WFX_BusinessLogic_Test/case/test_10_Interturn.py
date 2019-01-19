# -*- coding: utf-8 -*-
# @Time    : 2019/1/14 10:48 AM
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : test_10_Interturn.py
# @Software: PyCharm

from common.ban_warning import *
from common.public_func import *
from common.myunit import StartEnd
import unittest
import requests


class InterturnTest(StartEnd):
    """资金互转"""
    header = {
        'token': token()
    }

    # 资金互转  type: 1:跟随->MT5  // 2:MT5->跟随
    u1 = 'https://ptest.wavehk.cn/v2/mt5/moneyInterturn'
    p1 = {
        "version": "2.5",
        "apptype": "ios",
        "did": "12345dg",
        "money": "10.0",
        "type": "1",
        "sign": "5sCioY2cazwBz0aN\/Wa75zRRYv\/tvekiMeUdCUzNxTBd6wrcpTK\/fcs7UjLnclGK"
    }
    # 跟随账号余额计算
    u = 'https://ptest.wavehk.cn/v2/user/getUserInfo'
    p = {
        "version": "2.5",
        "sign": "5sCioY2cazwBz0aN\/Wa7599oH0LM1P+PSPUdZz5O+JFVGjc+9mh7KgQTWZpTKZuL",
        "apptype": "ios",
        "did": "12345dg"
    }

    # 持仓列表
    u2 = 'https://ptest.wavehk.cn/v2/mt5/getUserMt5OrderList'
    p2 = {
        "limit": "30",
        "did": "12345dg",
        "apptype": "ios",
        "version": "2.5",
        "page": "1",
        "order_type": "1",
        "sign": "5sCioY2cazwBz0aN\/Wa75\/X6Ni5wiWAUDc7Tg9s95phhqvZtTkO1YPACuzfmDT36"
    }
    # 平仓
    u3 = 'https://ptest.wavehk.cn/v2/mt5/closePosition'
    p3 = {
        "did": "12345dg",
        "order": '',
        "apptype": "ios",
        "sign": "5sCioY2cazwBz0aN\/Wa752wKMczWQfMYsK5Q7BKm02Zh1Rw7do0\/bbNsAzDaI1Sb",
        "version": "2.5"
    }

    def test_interturn(self):
        """全部平仓"""
        cc_id = []
        # 获取持仓所有id
        lo = requests.post(self.u2, json=self.p2, headers=self.header, verify=False)
        # print(lo.json())
        for i in lo.json()['data']['list']:
            cc_id.append(i['position'])
            # print(i['position'])
        print(cc_id)
        if cc_id:
            for j in cc_id:
                self.p3['order'] = j
                pc = requests.post(self.u3, json=self.p3, headers=self.header, verify=False)
                print(pc.json())
        else:
            print('====持仓为空====')

    def test_interturn0(self):
        """资金互转[跟随->MT5]"""
        lo = requests.post(self.u, json=self.p, headers=self.header, verify=False)
        lo1 = requests.post(self.u1, json=self.p1, headers=self.header, verify=False)
        print(lo1.json())

        a = float(lo1.json()['data']['mt5_canWithdraw'])
        b = float(lo.json()['data']['mt5_canWithdraw'])
        c = float(self.p1['money'])
        print('MT5余额:{} = {} + {}'.format(a, b, c))

        a1 = float(lo1.json()['data']['canWithdraw'])
        b1 = float(lo.json()['data']['canWithdraw'])
        print('跟随余额:{} = {} - {}'.format(a1, b1, c))
        assert a == b + c
        assert a1 == b1 - c

    def test_interturn1(self):
        """资金互转[MT5->跟随]"""
        lo = requests.post(self.u, json=self.p, headers=self.header, verify=False)
        self.p1['type'] = '2'
        lo1 = requests.post(self.u1, json=self.p1, headers=self.header, verify=False)
        print(lo1.json())

        a = float(lo1.json()['data']['canWithdraw'])
        b = float(lo.json()['data']['canWithdraw'])
        c = float(self.p1['money'])
        print('跟随余额:{} = {} + {}'.format(a, b, c))

        a1 = float(lo1.json()['data']['mt5_canWithdraw'])
        b1 = float(lo.json()['data']['mt5_canWithdraw'])
        print('MT5余额:{} = {} - {}'.format(a1, b1, c))
        assert a == b + c
        assert a1 == b1 - c

    def test_interturn2(self):
        """转入金额大于余额[跟随->MT5]"""
        self.p1['type'] = '1'
        self.p1['money'] = '999999999.99'
        lo = requests.post(self.u1, json=self.p1, headers=self.header, verify=False)
        print(lo.json())
        assert_json(lo.json(), 'code', 51006)
        assert_json(lo.json(), 'message', '转出金额不能大于可转出余额')

    def test_interturn3(self):
        """转入金额大于余额[MT5->跟随]"""
        self.p1['type'] = '2'
        self.p1['money'] = '999999.99'
        lo = requests.post(self.u1, json=self.p1, headers=self.header, verify=False)
        print(lo.json())
        assert_json(lo.json(), 'code', 51006)
        assert_json(lo.json(), 'message', '转出金额不能大于可转出余额')

    def test_interturn4(self):
        """转入负数[跟随->MT5]"""
        self.p1['type'] = '1'
        self.p1['money'] = '-1'
        lo = requests.post(self.u1, json=self.p1, headers=self.header, verify=False)
        print(lo.json())
        assert_json(lo.json(), 'code', 40004)
        assert_json(lo.json(), 'message', '转出金额必须大于0')

    def test_interturn5(self):
        """转入负数[MT5->跟随]"""
        self.p1['type'] = '2'
        self.p1['money'] = '-1'
        lo = requests.post(self.u1, json=self.p1, headers=self.header, verify=False)
        print(lo.json())
        assert_json(lo.json(), 'code', 40004)
        assert_json(lo.json(), 'message', '转出金额必须大于0')

    def test_interturn6(self):
        """转入绝对值大于余额负数[跟随->MT5]"""
        self.p1['type'] = '1'
        self.p1['money'] = '-999999999.99'
        lo = requests.post(self.u1, json=self.p1, headers=self.header, verify=False)
        print(lo.json())
        assert_json(lo.json(), 'code', 40004)
        assert_json(lo.json(), 'message', '转出金额必须大于0')

    def test_interturn7(self):
        """转入绝对值大于余额负数[MT5->跟随]"""
        self.p1['type'] = '2'
        self.p1['money'] = '-99999.99'
        lo = requests.post(self.u1, json=self.p1, headers=self.header, verify=False)
        print(lo.json())
        assert_json(lo.json(), 'code', 40004)
        assert_json(lo.json(), 'message', '转出金额必须大于0')

    def test_interturn8(self):
        """字符转入[跟随->MT5]"""
        self.p1['type'] = '1'
        self.p1['money'] = 'okc'
        lo = requests.post(self.u1, json=self.p1, headers=self.header, verify=False)
        print(lo.json())
        # assert_json(lo.json(), 'code', '999')
        # assert_json(lo.json(), 'msessage', '系统内部错误')
        # print('key:msessage:笔误')
        assert_json(lo.json(), 'code', 40004)
        assert_json(lo.json(), 'message', '转出金额必须大于0')

    def test_interturn9(self):
        """字符转入[MT5->跟随]"""
        self.p1['type'] = '2'
        self.p1['money'] = 'okc'
        lo = requests.post(self.u1, json=self.p1, headers=self.header, verify=False)
        print(lo.json())
        # assert_json(lo.json(), 'code', '999')
        # assert_json(lo.json(), 'msessage', '系统内部错误')
        # print('key:msessage:笔误')
        assert_json(lo.json(), 'code', 40004)
        assert_json(lo.json(), 'message', '转出金额必须大于0')

    def test_interturn10(self):
        """转入金额为空[跟随->MT5]"""
        self.p1['type'] = '1'
        self.p1['money'] = ''
        lo = requests.post(self.u1, json=self.p1, headers=self.header, verify=False)
        print(lo.json())
        # assert_json(lo.json(), 'code', 40004)
        # assert_json(lo.json(), 'message', '金额不能为空')
        assert_json(lo.json(), 'code', 40004)
        assert_json(lo.json(), 'message', '转出金额必须大于0')

    def test_interturn11(self):
        """转入金额为空[MT5->跟随]"""
        self.p1['type'] = '2'
        self.p1['money'] = ''
        lo = requests.post(self.u1, json=self.p1, headers=self.header, verify=False)
        print(lo.json())
        # assert_json(lo.json(), 'code', 40004)
        # assert_json(lo.json(), 'message', '金额不能为空')
        assert_json(lo.json(), 'code', 40004)
        assert_json(lo.json(), 'message', '转出金额必须大于0')


if __name__ == '__main__':
    unittest.main()
