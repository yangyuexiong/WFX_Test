# -*- coding: utf-8 -*-
# @Time    : 2019/1/21 4:29 PM
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : capital_func.py
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
def get_user_info(n=None):
    url_1 = 'https://ptest.wavehk.cn/v2/user/getUserInfo'
    param_1 = {
        "did": "12345dg",
        "sign": "5sCioY2cazwBz0aN\/Wa75wCSlO2HygaA3sJJtyrQaf5SxMdc7jjxbije0DDcuF1y",
        "apptype": "ios",
        "version": "2.5"
    }
    result_1 = requests.post(url_1, json=param_1, headers=header, verify=False)
    print('{}{}{}'.format('-' * 30, 'getUserInfo', '-' * 30))
    amount = result_1.json()['data']['amount']  # 总资产
    income = result_1.json()['data']['income']  # 累计收益
    yesterdayIncome = result_1.json()['data']['yesterdayIncome']  # 昨日收益
    canWithdraw = result_1.json()['data']['canWithdraw']  # 波浪余额
    mt5_canWithdraw = result_1.json()['data']['mt5_canWithdraw']  # MT5账户余额
    follow_money = result_1.json()['data']['follow_money']  # 跟随总金额
    follow_income_ing = result_1.json()['data']['follow_income_ing']  # 跟随收益
    msg = '总资产:{}\n累计收益:{}\n昨日收益:{}\n波浪余额:{}\nMT5账户余额:{}\n跟随总金额:{}\n跟随收益:{}\n'.format(amount, income, yesterdayIncome,
                                                                                      canWithdraw, mt5_canWithdraw,
                                                                                      follow_money, follow_income_ing)
    if n:
        print(result_1.json()['data'])
        print(msg)
    dict1 = {
        "总资产": float(amount),
        "累计收益": float(income),
        "昨日收益": float(yesterdayIncome),
        "波浪余额": float(canWithdraw),
        "MT5账户余额": float(mt5_canWithdraw),
        "跟随总金额": float(follow_money),
        "跟随收益": float(follow_income_ing),
    }
    return dict1


# 收益
def profit(n=None, date=None, diy_fd=None, diy_ld=None):
    import datetime
    import calendar
    from datetime import timedelta
    """
    date='zr'
    :return 昨日收益

    date='lj'
    :return 累计所有的收益

    date='by'
    :return 本月所有的收益

    date='sy'
    :return 上月所有的收益

    date='jr'
    :return 今日所有的收益

    date='jyn'
    :return 近一年所有的收益

    date='diy'
    :return 自定义时间内收益
    """

    url_2 = 'https://ptest.wavehk.cn/v2/user/incomeBill25'
    url_2x = 'https://ptest.wavehk.cn/v2/user/profitDetailedListNew'

    param_2 = {
        "sign": "5sCioY2cazwBz0aN\/Wa757sUMoyDuCrNFRN7hLrsmEwNK+jrHqmQ4TrBPunxHptV",
        "did": "12345dg",
        "apptype": "ios",
        "start_date": '',
        "limit": "99999",
        "version": "2.5",
        "end_date": '',
        "page": ""
    }

    param_2x = {
        "sign": "5sCioY2cazwBz0aN\/Wa756FamEqfoC13HCGw\/xudw9y8LBPZTh5cPY\/w01LY1SSe",
        "did": "12345dg",
        "apptype": "ios",
        "start_date": "",
        "limit": "99999",
        "version": "2.5",
        "end_date": "",
        "page": "1"
    }

    dict1 = {}
    dict1x = {}
    msg = ''
    profit_title = ''
    now_time = datetime.datetime.now()

    if date == 'zr':

        yesterday = now_time - datetime.timedelta(days=1)
        # print(yesterday.strftime('%Y-%m-%d'))
        day = yesterday.strftime('%Y-%m-%d')
        param_2['start_date'] = day
        param_2['end_date'] = day
        param_2x['start_date'] = day
        param_2x['end_date'] = day

    elif date == 'lj':
        param_2['start_date'] = ''
        param_2['end_date'] = ''
        param_2x['start_date'] = ''
        param_2x['end_date'] = ''

    elif date == 'by':

        x = now_time.strftime('%Y%m%d')
        send_year = int(x[0:4])
        send_month = int(x[5:6])
        month_range = calendar.monthrange(send_year, send_month)
        first_day = datetime.date(year=datetime.date.today().year, month=datetime.date.today().month, day=1)
        last_day = datetime.date(datetime.date.today().year, datetime.date.today().month, 1) + datetime.timedelta(
            month_range[-1] - 1)  # 减1天
        # print(send_year)
        # print(send_month)
        # print(month_range[-1])
        # print(first_day, type(first_day))
        # print(last_day)
        param_2['start_date'] = str(first_day)
        param_2['end_date'] = str(last_day)
        param_2x['start_date'] = str(first_day)
        param_2x['end_date'] = str(last_day)

    elif date == 'sy':
        first_day = get_last_month_first_day()
        last_day = get_last_month_last_day()
        param_2['start_date'] = str(first_day)
        param_2['end_date'] = str(last_day)
        param_2x['start_date'] = str(first_day)
        param_2x['end_date'] = str(last_day)

    elif date == 'jr':
        today = datetime.date.today()
        param_2['start_date'] = str(today)
        param_2['end_date'] = str(today)
        param_2x['start_date'] = str(today)
        param_2x['end_date'] = str(today)

    elif date == 'jyn':
        today = datetime.date.today()
        last_year = today - timedelta(days=365)
        param_2['start_date'] = str(last_year)
        param_2['end_date'] = str(today)
        param_2x['start_date'] = str(last_year)
        param_2x['end_date'] = str(today)

    elif date == 'diy':
        if diy_fd and diy_ld:
            param_2['start_date'] = str(diy_fd)
            param_2['end_date'] = str(diy_ld)
            param_2x['start_date'] = str(diy_fd)
            param_2x['end_date'] = str(diy_ld)
        else:
            pass
    else:
        return '传入参数错误'
    result_2 = requests.post(url_2, json=param_2, headers=header, verify=False)

    """ 
    income:          昨日合计收益//累计总收益//本月合计收益//上月合计收益//今日合计收益//近一年合计收益//自定义
    follow_income:   昨日跟随收益//跟随总收益//本月跟随收益//上月跟随收益//今日跟随收益//近一年跟随收益//自定义
    trade_income:    昨日交易收益//交易总收益//本月交易收益//上月交易收益//今日交易收益//近一年交易收益//自定义
    activity_income: 昨日活动收益//活动总收益//本月活动收益//上月活动收益//今日活动收益//近一年活动收益//自定义
    """

    income = result_2.json()['data']['income']
    follow_income = result_2.json()['data']['follow_income']
    trade_income = result_2.json()['data']['trade_income']
    activity_income = result_2.json()['data']['activity_income']

    if date == 'zr':
        dict1 = {
            '昨日合计收益': float(income),
            '昨日跟随收益': float(follow_income),
            '昨日交易收益': float(trade_income),
            '昨日活动收益': float(activity_income),
        }
        profit_title = '昨日收益'
        msg = '昨日-合计收益:{}\n昨日-跟随收益:{}\n昨日-交易收益:{}\n昨日-活动收益:{}\n'

    if date == 'lj':
        dict1 = {
            '累计-总收益': float(income),
            '跟随-总收益': float(follow_income),
            '交易-总收益': float(trade_income),
            '活动-总收益': float(activity_income),
        }
        profit_title = '累计收益'
        msg = '累计-总收益:{}\n跟随-总收益:{}\n交易-总收益:{}\n活动-总收益:{}\n'

    if date == 'by':
        dict1 = {
            '本月合计收益': float(income),
            '本月跟随收益': float(follow_income),
            '本月交易收益': float(trade_income),
            '本月活动收益': float(activity_income),
        }
        profit_title = '本月收益'
        msg = '本月合计收益:{}\n本月跟随收益:{}\n本月交易收益:{}\n本月活动收益:{}\n'

    if date == 'sy':
        dict1 = {
            '上月合计收益': float(income),
            '上月跟随收益': float(follow_income),
            '上月交易收益': float(trade_income),
            '上月活动收益': float(activity_income),
        }
        profit_title = '上月收益'
        msg = '上月合计收益:{}\n上月跟随收益:{}\n上月交易收益:{}\n上月活动收益:{}\n'

    if date == 'jr':
        dict1 = {
            '今日合计收益': float(income),
            '今日跟随收益': float(follow_income),
            '今日交易收益': float(trade_income),
            '今日活动收益': float(activity_income),
        }
        profit_title = '今日收益'
        msg = '今日合计收益:{}\n今日跟随收益:{}\n今日交易收益:{}\n今日活动收益:{}\n'

    if date == 'jyn':
        dict1 = {
            '近一年合计收益': float(income),
            '近一年跟随收益': float(follow_income),
            '近一年交易收益': float(trade_income),
            '近一年活动收益': float(activity_income),
        }
        profit_title = '近一年收益'
        msg = '近一年合计收益:{}\n近一年跟随收益:{}\n近一年交易收益:{}\n近一年活动收益:{}\n'

    if date == 'diy':
        dict1 = {
            '{}到{}合计收益'.format(diy_fd, diy_ld): float(income),
            '{}到{}跟随收益'.format(diy_fd, diy_ld): float(follow_income),
            '{}到{}交易收益'.format(diy_fd, diy_ld): float(trade_income),
            '{}到{}活动收益'.format(diy_fd, diy_ld): float(activity_income),
        }
        profit_title = '{}到{}收益'.format(diy_fd, diy_ld)
        d_m = '{}到{}'.format(diy_fd, diy_ld)
        msg = '%s合计收益:{}\n%s跟随收益:{}\n%s交易收益:{}\n%s活动收益:{}\n' % (d_m, d_m, d_m, d_m)

    result_2x = requests.post(url_2x, json=param_2x, headers=header, verify=False)

    print('{}{}{}'.format('-' * 30, '%s', '-' * 30) % profit_title)

    '''收益明细计算
    gsmx//jymx//hdmx:金额集
    gsmx_sum//jymx_sum//hdmx_sum:金额集总和
    '''
    gsmx = []
    jymx = []
    hdmx = []
    gsmx_sum = 0
    jymx_sum = 0
    hdmx_sum = 0
    for i in result_2x.json()['data']['data']:
        # print('i', i)
        for j in i['list']:
            # print('j', j)
            if j['type'] == '跟单收益':
                gsmx.append(j['income'])
            elif j['type'] == '交易收益':
                jymx.append(j['income'])
            elif j['type'] == '活动获得奖金':
                hdmx.append(j['income'])
            else:
                pass

    print('跟随收益金额列表:', gsmx)
    print('交易收益金额列表:', jymx)
    print('活动收益金额列表:', hdmx)

    for g in gsmx:
        gsmx_sum += float(g)

    for y in jymx:
        jymx_sum += float(y)

    for h in hdmx:
        hdmx_sum += float(h)

    print(gsmx_sum)
    print(jymx_sum)
    print(hdmx_sum)

    if date == 'zr':
        dict1x = {
            '昨日跟随收益': gsmx_sum,
            '昨日交易收益': jymx_sum,
            '昨日活动收益': hdmx_sum,
        }

    if date == 'lj':
        dict1x = {
            '跟单收益-总和': gsmx_sum,
            '交易收益-总和': jymx_sum,
            '活动获得奖金-总和': hdmx_sum,
        }

    if date == 'by':
        dict1x = {
            '本月跟随收益': gsmx_sum,
            '本月交易收益': jymx_sum,
            '本月活动收益': hdmx_sum,
        }

    if date == 'sy':
        dict1x = {
            '上月跟随收益': gsmx_sum,
            '上月交易收益': jymx_sum,
            '上月活动收益': hdmx_sum,
        }

    if date == 'jr':
        dict1x = {
            '今日跟随收益': gsmx_sum,
            '今日交易收益': jymx_sum,
            '今日活动收益': hdmx_sum,
        }

    if date == 'jyn':
        dict1x = {
            '近一年跟随收益': gsmx_sum,
            '近一年交易收益': jymx_sum,
            '近一年活动收益': hdmx_sum,
        }

    if date == 'diy':
        dict1x = {
            '{}到{}跟随收益'.format(diy_fd, diy_ld): gsmx_sum,
            '{}到{}交易收益'.format(diy_fd, diy_ld): jymx_sum,
            '{}到{}活动收益'.format(diy_fd, diy_ld): hdmx_sum,
        }

    if n:
        # print(result_2.json())
        # print(result_2x.json())
        print(msg.format(income, follow_income, trade_income, activity_income))

    return dict1, dict1x


# 可用余额
def available_balance():
    url_5 = 'https://ptest.wavehk.cn/v2/user/getUserInfo'
    param_5 = {
        "apptype": "ios",
        "did": "12345dg",
        "version": "2.5",
        "sign": "5sCioY2cazwBz0aN\/Wa754ZreIo2JJymjMlQC0Oo\/BTfCHapogHMvwGNaclRlmVm"
    }
    result_5 = requests.post(url_5, json=param_5, headers=header, verify=False)
    print('{}{}{}'.format('-' * 30, '可用余额', '-' * 30))
    canWithdraw = result_5.json()['data']['canWithdraw']
    mt5_canWithdraw = result_5.json()['data']['mt5_canWithdraw']
    dict5 = {
        '跟随可用余额': canWithdraw,
        'MT5可用余额': mt5_canWithdraw,
    }
    return dict5


if __name__ == '__main__':
    pass
    # r1 = get_user_info(1)
    # print(r1, '\n', '-' * 100)
    # r2 = yesterday_earnings()
    # print(r2, '\n', '-' * 100)
    # r3 = accumulated_income()
    # print(r3, '\n', '-' * 100)
    # r4 = income_details()
    # print(r4, '\n', '-' * 100)
    # r5 = available_balance()
    # print(r5, '\n', '-' * 100)

    print('=' * 100)
    '''收益'''
    # zr = profit(n=1, date='zr')
    # print(zr, '\n\n\n\n')

    # lj = profit(n=1, date='lj')
    # print(lj)

    # by = profit(date='by')
    # print(by)

    # sy = profit(date='sy')
    # print(sy)

    # jr = profit(date='jr')
    # print(jr)

    # jyn = profit(date='jyn')
    # print(jyn)

    # diy = profit(date='diy', diy_fd='2019-01-11', diy_ld='2019-01-23')
    # print(diy)

    # date_list = ['zr', 'lj', 'by', 'sy', 'jr', 'jyn', 'diy']
    # for i in date_list:
    #     r = profit(n=1, date=i, diy_fd='2019-01-11', diy_ld='2019-01-23')
    #     print(r)
