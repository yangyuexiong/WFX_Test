# -*- coding: utf-8 -*-
# @Time    : 2019/1/21 4:15 PM
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : test_11_Count_v2_5_.py
# @Software: PyCharm


from common.ban_warning import *
from common.public_func import *
from common.capital_func import *
from common.myunit import StartEnd
import unittest
import requests

header = {
    'token': token()
}


# 总资产
class TotalAssets(StartEnd):

    def test_00(self):
        """明细"""
        print(get_user_info(1))

    def test_01(self):
        """波浪余额"""
        # 波浪余额 = 总资产 - 跟随总金额 - 跟随收益 - MT5余额
        r = get_user_info()
        print(r)
        # print(round(r['总资产'] - r['跟随总金额'] - r['跟随收益'] - r['MT5账户余额'], 2))
        assert r['波浪余额'] == round(r['总资产'] - r['跟随总金额'] - r['跟随收益'] - r['MT5账户余额'], 2)

    def test_02(self):
        """跟随总金额"""
        r = get_user_info()
        print(r)
        # 跟随总金额 = 总资产 - 波浪余额 - 跟随收益 - MT5余额
        assert r['跟随总金额'] == round(r['总资产'] - r['波浪余额'] - r['跟随收益'] - r['MT5账户余额'], 2)

    def test_03(self):
        """跟随收益"""
        # 跟随收益 = 总资产 - 波浪余额 - 跟随总金额 - MT5余额
        r = get_user_info()
        print(r)
        assert r['跟随收益'] == round(r['总资产'] - r['波浪余额'] - r['跟随总金额'] - r['MT5账户余额'], 2)

    def test_04(self):
        """MT5账户余额"""
        # MT5账户余额 = 总资产 - 跟随账户余额 - 波浪余额 - 跟随收益
        r = get_user_info()
        print(r)
        assert r['MT5账户余额'] == round(r['总资产'] - r['波浪余额'] - r['跟随总金额'] - r['跟随收益'], 2)

    def test_05(self):
        """总资产"""
        # 平仓释放MT5预付款
        # 总资产 = 波浪余额 + MT5账户余额 + 跟随总金额 + 跟随收益
        r = get_user_info()
        print(r)
        assert r['总资产'] == round(r['波浪余额'] + r['MT5账户余额'] + r['跟随总金额'] + r['跟随收益'], 2)


# 收益账单
class IncomeStatement(StartEnd):

    def test_01(self):
        """昨日合计收益"""
        # 昨日合计收益 = 昨日跟随收益 + 昨日交易收益 + 昨日活动收益
        r = profit(date='zr')
        print(r[0])
        print(r[1])
        assert r[0]['昨日合计收益'] == round(r[0]['昨日跟随收益'] + r[0]['昨日交易收益'] + r[0]['昨日活动收益'], 2)
        assert r[0]['昨日合计收益'] == round(r[1]['昨日跟随收益'] + r[1]['昨日交易收益'] + r[1]['昨日活动收益'], 2)

    def test_02(self):
        """累计-总收益"""
        # 累计-总收益 = 跟随-总收益 + 交易-总收益 + 活动-总收益
        r = profit(date='lj')
        print(r[0])
        print(r[1])
        assert r[0]['累计-总收益'] == round(r[0]['跟随-总收益'] + r[0]['交易-总收益'] + r[0]['活动-总收益'], 2)
        assert r[0]['累计-总收益'] == round(r[1]['跟单收益-总和'] + r[1]['交易收益-总和'] + r[1]['活动获得奖金-总和'], 2)

    def test_03(self):
        """本月收益"""
        # 本月收益 = 本月跟随收益 + 本月交易收益 + 本月活动收益
        r = profit(date='by')
        print(r[0])
        print(r[1])
        assert r[0]['本月合计收益'] == round(r[0]['本月跟随收益'] + r[0]['本月交易收益'] + r[0]['本月活动收益'], 2)
        assert r[0]['本月合计收益'] == round(r[1]['本月跟随收益'] + r[1]['本月交易收益'] + r[1]['本月活动收益'], 2)

    def test_04(self):
        """上月收益"""
        # 上月收益 = 上月跟随收益 + 上月交易收益 + 上月活动收益
        r = profit(date='sy')
        print(r[0])
        print(r[1])
        assert r[0]['上月合计收益'] == round(r[0]['上月跟随收益'] + r[0]['上月交易收益'] + r[0]['上月活动收益'], 2)
        assert r[0]['上月合计收益'] == round(r[1]['上月跟随收益'] + r[1]['上月交易收益'] + r[1]['上月活动收益'], 2)

    def test_05(self):
        """今日收益"""
        # 今日收益 = 今日跟随收益 + 今日交易收益 + 今日活动收益
        r = profit(date='jr')
        print(r[0])
        print(r[1])
        assert r[0]['今日合计收益'] == round(r[0]['今日跟随收益'] + r[0]['今日交易收益'] + r[0]['今日活动收益'], 2)
        assert r[0]['今日合计收益'] == round(r[1]['今日跟随收益'] + r[1]['今日交易收益'] + r[1]['今日活动收益'], 2)

    def test_06(self):
        """近一年收益"""
        # 近一年收益 = 近一年跟随收益 + 近一年交易收益 + 近一年活动收益
        r = profit(date='jyn')
        print(r[0])
        print(r[1])
        assert r[0]['近一年合计收益'] == round(r[0]['近一年跟随收益'] + r[0]['近一年交易收益'] + r[0]['近一年活动收益'], 2)
        assert r[0]['近一年合计收益'] == round(r[1]['近一年跟随收益'] + r[1]['近一年交易收益'] + r[1]['近一年活动收益'], 2)

    def test_07(self):
        """自定义日期区间的收益"""
        diy_fd = '2019-01-11'
        diy_ld = '2019-01-23'
        a1 = '{}到{}合计收益'.format(diy_fd, diy_ld)
        a2 = '{}到{}跟随收益'.format(diy_fd, diy_ld)
        a3 = '{}到{}交易收益'.format(diy_fd, diy_ld)
        a4 = '{}到{}活动收益'.format(diy_fd, diy_ld)
        r = profit(date='diy', diy_fd=diy_fd, diy_ld=diy_ld)
        print(r[0])
        results1 = r[0][a2] + r[0][a3] + r[0][a4]
        results2 = r[1][a2] + r[1][a3] + r[1][a4]
        assert r[0][a1] == round(results1, 2)
        assert r[0][a1] == round(results2, 2)


if __name__ == '__main__':
    unittest.main()
