# -*- coding: utf-8 -*-
# @Time    : 2019/1/15 2:58 PM
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : test_11_Count_v2_4_.py
# @Software: PyCharm


from common.ban_warning import *
from common.public_func import *
from common.myunit import StartEnd
import unittest
import requests

header = {
    'token': token()
}

# getUserInfo
u = 'https://ptest.wavehk.cn/v2/user/getUserInfo'
p = {
    "version": "2.5",
    "sign": "5sCioY2cazwBz0aN\/Wa7599oH0LM1P+PSPUdZz5O+JFVGjc+9mh7KgQTWZpTKZuL",
    "apptype": "ios",
    "did": "12345dg"
}
result = requests.post(u, json=p, headers=header, verify=False)

# 跟随管理
u1 = 'https://ptest.wavehk.cn/v1/Documentary/userfollowing'
p1 = {
    "apptype": "ios",
    "sign": "5sCioY2cazwBz0aN\/Wa759Ux4C7UgPr7\/9zH9Iuu9jTWfocrtkoAwIT\/Op59YCCA",
    "version": "2.5",
    "did": "12345dg"
}

lo = requests.post(u1, json=p1, headers=header, verify=False)
zjz = lo.json()['networth_total']
zje = lo.json()['follow_price_total']

amount = float(result.json()['data']['amount'])  # 总资产
canwithdraw = float(result.json()['data']['canWithdraw'])  # 跟随账户余额
follow_money = float(result.json()['data']['follow_money'])  # 跟随金额
gensuishouyi = round(float(zjz) - float(zje), 2)  # 跟随收益
mt5_canWithdraw = float(result.json()['data']['mt5_canWithdraw'])  # MT5余额

gensui_zuori = round(float(zjz) - float(zje), 2)  # 跟随昨日收益
gensui_leiji = ''  # 跟随累计收益
jiaoyi_zuori = float(result.json()['data']['mt5_yesterday_income'])  # 交易昨日收益
jiaoyi_leiji = float(result.json()['data']['income'])  # 交易累计收益

zuori_count = float(result.json()['data']['yesterdayIncome'])  # 昨日总收益

leiji_shouyi = float(result.json()['data']['income'])  # 累计收益

# 资产明细
u2 = 'https://ptest.wavehk.cn/v2/user/assetsDetailed'
p2 = {
    "apptype": "ios",
    "sign": "5sCioY2cazwBz0aN\/Wa758y98yl6azoa6hzCnIebzLkdZkCPgz\/ooCuHf9QwBjMH",
    "version": "2.5",
    "did": "12345dg"
}
lo1 = requests.post(u2, json=p2, headers=header, verify=False)
zijin_dict = {
    '昨日跟随收益': lo1.json()['data']['yesterday_follow_income'],
    '累计跟随收益': lo1.json()['data']['follow_income'],
    '昨日交易收益': lo1.json()['data']['mt5_yesterday_income'],
    '累计交易收益': lo1.json()['data']['mt5_income'],
    '总资产': lo1.json()['data']['amount'],
    '跟随账户余额': lo1.json()['data']['follow_amount'],
    '跟随金额': lo1.json()['data']['follow_money'],
    '跟随收益': lo1.json()['data']['follow_income_ing'],
    'MT5余额': lo1.json()['data']['mt5_balance'],
}

# 收益账单
u3 = 'https://ptest.wavehk.cn/v2/user/incomeBillNew'
p3 = {
    "sign": "5sCioY2cazwBz0aN\/Wa75ymF7MOr0vlBh3jqK5Je8iANX4TGMMLpxJQe8kcndLWs",
    "apptype": "ios",
    "version": "2.5",
    "currency": "USD",
    "date": "2019-01",
    "type": "week",
    "did": "12345dg"
}
u3_1 = 'https://ptest.wavehk.cn/v2/user/profitDetailedListNew'
p3_1 = {
    "limit": "999999999",
    "end_date": "",
    "version": "2.5",
    "apptype": "ios",
    "page": "1",
    "did": "12345dg",
    "sign": "5sCioY2cazwBz0aN\/Wa75ymbqvoNc\/QQMufRDTTKibQQ18HiVM8zaXqaDcwHgihH",
    "start_date": ""
}
u3_2 = 'https://ptest.wavehk.cn/v2/user/incomeBill25'
p3_2 = {
    "limit": "",
    "did": "12345dg",
    "end_date": "",
    "page": "",
    "version": "2.5",
    "apptype": "ios",
    "start_date": "",
    "sign": "5sCioY2cazwBz0aN\/Wa75+GX9yjWBr0a+B4HLy25w3Rfo4Otu+GvS62scXQkNLcr"
}
lo3 = requests.post(u3, json=p3, headers=header, verify=False)
lo3_1 = requests.post(u3_1, json=p3_1, headers=header, verify=False)
lo3_2 = requests.post(u3_2, json=p3_2, headers=header, verify=False)

# 交易管理
u4 = 'https://ptest.wavehk.cn/v2/mt5/getUserMt5OrderList'
p4 = {
    "apptype": "ios",
    "page": "1",
    "version": "2.5",
    "did": "12345dg",
    "sign": "5sCioY2cazwBz0aN\/Wa75yetb3ny81QMYp7PD63FKa2SjE7wa5XgWkbKP7wD+T36",
    "limit": "30",
    "order_type": "1"
}
lo4 = requests.post(u4, json=p4, headers=header, verify=False)

# 持仓列表
u5 = 'https://ptest.wavehk.cn/v2/mt5/getUserMt5OrderList'
p5 = {
    "limit": "30",
    "did": "12345dg",
    "apptype": "ios",
    "version": "2.5",
    "page": "1",
    "order_type": "1",
    "sign": "5sCioY2cazwBz0aN\/Wa75\/X6Ni5wiWAUDc7Tg9s95phhqvZtTkO1YPACuzfmDT36"
}
# 平仓
u6 = 'https://ptest.wavehk.cn/v2/mt5/closePosition'
p6 = {
    "did": "12345dg",
    "order": '',
    "apptype": "ios",
    "sign": "5sCioY2cazwBz0aN\/Wa752wKMczWQfMYsK5Q7BKm02Zh1Rw7do0\/bbNsAzDaI1Sb",
    "version": "2.5"
}


def pingcang():
    cc_id = []
    # 获取持仓所有id
    lo = requests.post(u5, json=p5, headers=header, verify=False)
    # print(lo.json())
    for i in lo.json()['data']['list']:
        cc_id.append(i['position'])
        # print(i['position'])
    print('持仓订单号列表', cc_id)
    if cc_id:
        for j in cc_id:
            p6['order'] = j
            pc = requests.post(u6, json=p6, headers=header, verify=False)
            # print(pc.json())
            print('====全部平仓完成====')
    else:
        print('====持仓为空====')


@unittest.skip('废弃v2.4版本')
class TotalAssets(StartEnd):
    """总资产"""

    def test_0(self):
        """明细"""
        print(result.json())

        print('-' * 33)
        print('总资产:{}\n跟随账户余额:{}\n跟随金额:{}\n跟随收益:{}\nMT5余额:{}:'.format(amount, canwithdraw, follow_money, gensuishouyi,
                                                                      mt5_canWithdraw))
        print('-' * 33)

    def test_01(self):
        """跟随账户余额"""
        # 总资产 - 跟随金额 - 跟随收益 - MT5余额
        print('跟随账户余额:{}=总资产:{}-跟随金额:{}-跟随收益:{}-MT5余额:{}'.format(canwithdraw, amount, follow_money, gensuishouyi,
                                                                 mt5_canWithdraw))
        assert canwithdraw == round(amount - follow_money - gensuishouyi - mt5_canWithdraw, 2)
        assert canwithdraw == float(zijin_dict['跟随账户余额'])

    def test_02(self):
        """跟随金额"""
        # 总资产 - 跟随账户余额 - 跟随收益 - MT5余额
        print('跟随金额:{}=总资产:{}-跟随账户余额:{}-跟随收益:{}-MT5余额:{}'.format(follow_money, amount, canwithdraw, gensuishouyi,
                                                                 mt5_canWithdraw))
        assert follow_money == round(amount - canwithdraw - gensuishouyi - mt5_canWithdraw, 2)
        assert follow_money == float(zijin_dict['跟随金额'])

    def test_03(self):
        """跟随收益"""
        # 总资产 - 跟随账户余额 - 跟随金额 - MT5余额
        print('跟随收益:{}=总资产:{}-跟随账户余额:{}-跟随金额:{}-MT5余额:{}'.format(gensuishouyi, amount, canwithdraw, follow_money,
                                                                 mt5_canWithdraw))
        assert gensuishouyi == round(amount - canwithdraw - follow_money - mt5_canWithdraw, 2)
        assert gensuishouyi == float(zijin_dict['跟随收益'])

    def test_04(self):
        """MT5余额"""
        # 总资产 - 跟随账户余额 - 跟随金额 - 跟随收益
        print('跟随金额:{}=总资产:{}-跟随账户余额:{}-跟随收益:{}-跟随收益:{}'.format(mt5_canWithdraw, amount, canwithdraw, follow_money,
                                                                gensuishouyi))
        assert mt5_canWithdraw == round(amount - canwithdraw - follow_money - gensuishouyi, 2)
        print(mt5_canWithdraw)
        print(round(amount - canwithdraw - follow_money - gensuishouyi, 2))

    def test_05(self):
        """总资产"""
        # 平仓释放MT5预付款
        pingcang()
        # 跟随账户余额 + 跟随金额 + 跟随收益 + MT5余额
        print('总资产:{} = {} + {} + {} + {}'.format(amount, canwithdraw, follow_money, gensuishouyi, mt5_canWithdraw))
        assert amount == round(canwithdraw + gensuishouyi + follow_money + mt5_canWithdraw, 2)
        print(amount)
        print(float(zijin_dict['总资产']))
        # assert amount == float(zijin_dict['总资产'])

    @unittest.skip('打印数据')
    def test_06(self):
        print(zijin_dict)


@unittest.skip('废弃v2.4版本')
class YesterdayIncome(StartEnd):
    """昨日收益"""

    # 昨日跟随收益 + 昨日交易收益
    def test_01(self):
        """1"""

        print('昨日总收益:{}\n昨日跟随收益:{}\n昨日交易收益:{}'.format(zuori_count, zijin_dict['昨日跟随收益'], zijin_dict['昨日交易收益']))
        assert zuori_count == float(zijin_dict['昨日跟随收益']) + float(zijin_dict['昨日交易收益'])


@unittest.skip('废弃v2.4版本')
class AccumulatedIncome(StartEnd):
    """累计收益"""

    # 跟随收益 + 交易收益 + 活动收益
    def test_01(self):
        """累计收益计算1"""
        ljgs = zijin_dict['累计跟随收益']
        ljjy = zijin_dict['累计交易收益']
        print('跟随累计收益:{}\n交易累计收益:{}\n累计总收益:{}'.format(gensuishouyi, ljjy, leiji_shouyi))

        assert float(ljgs) == gensuishouyi
        assert leiji_shouyi == gensuishouyi + float(ljjy)

    def test_02(self):
        """收益账单计算2"""
        # print(lo3_1.json()['data']['data'])
        total_revenue = 0
        for i in lo3_1.json()['data']['data']:
            # print(i)
            # print(i['date'])
            # print(i['list'])
            for j in i['list']:
                # print(j['income'])
                total_revenue += float(j['income'])
        print('累计总收益:{} = 累计跟随收益:{} + 累计交易收益:{}'.format(round(total_revenue, 2), zijin_dict['累计跟随收益'],
                                                        zijin_dict['累计交易收益']))
        # print(round(total_revenue, 2))
        # print(zijin_dict['累计跟随收益'])
        # print(zijin_dict['累计交易收益'])
        # print(lo3_2.json()['data']['follow_income'])
        # print(lo3_2.json()['data']['trade_income'])
        # print(lo3_2.json()['data']['income'])
        assert round(total_revenue, 2) == round(float(zijin_dict['累计跟随收益']) + float(zijin_dict['累计交易收益']), 2)
        assert float(zijin_dict['累计跟随收益']) == lo3_2.json()['data']['follow_income']
        assert float(zijin_dict['累计交易收益']) == lo3_2.json()['data']['trade_income']
        assert lo3_2.json()['data']['income'] == round(
            lo3_2.json()['data']['follow_income'] + lo3_2.json()['data']['trade_income'], 2)
        assert lo3_2.json()['data']['income'] == round(total_revenue, 2)

    def test_03(self):
        """3"""


@unittest.skip('废弃v2.4版本')
class AvailableBalance(StartEnd):
    """可用余额"""

    # 总资产 - 跟随净值 == 跟随余额 + MT5余额
    def test_01(self):
        """1"""
        print('总金额:{}\n跟随净值:{}\n跟随余额:{}\nMT5余额:{}'.format(amount, zjz, canwithdraw, mt5_canWithdraw))
        # print(round(amount - zjz, 2))
        # print(canwithdraw + mt5_canWithdraw)
        assert round(amount - zjz, 2) == canwithdraw + mt5_canWithdraw


if __name__ == '__main__':
    unittest.main()
