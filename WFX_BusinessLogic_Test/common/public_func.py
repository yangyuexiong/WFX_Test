# -*- coding: utf-8 -*-
# @Time    : 2019/1/4 10:13 AM
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : public_func.py
# @Software: PyCharm


from test_db.test_db import db
import requests
from common.ban_warning import *


# 断言json
def assert_json(json_obj, key, v):
    assert json_obj[key] == v


# app登录
def app_login():
    base_url1 = 'https://ptest.wavehk.cn/v2/user/ruleCode'

    param_data1 = {
        "type": "login",
        "code": "1111",
        "mobile_fiex": "86",
        "sign": "5sCioY2cazwBz0aN\/Wa75zO8S6VmRdPJkijw9NQVD2XnnYqpLFI0jymDr0nnJ6kl",
        "apptype": "ios",
        "phone": "15013038819",
        "version": "2.4.0",
        "did": "12345dg"
    }

    lo = requests.post(base_url1, json=param_data1, verify=False)
    return lo.json()


# 令牌
def token():
    return app_login()['data']['token']


# 获取系统消息
def get_msg(token):
    u = 'https://ptest.wavehk.cn/v1/Msgbox/getMessage'
    p = {
        "pagesize": 30,
        "apptype": "ios",
        "sign": "5sCioY2cazwBz0aN\/Wa753\/VGQ10COZchqBs0FFD3T9+KMBZD5H4CHalCaupEKw1",
        "did": "12345dg",
        "type": "system",
        "version": "2.4.0",
        "page": 1
    }
    header = {
        'token': token
    }

    lo = requests.post(u, json=p, headers=header, verify=False)

    return lo.json()


# 获取user
def sclect_user(user_id):
    d3 = {}
    cur = db.cursor()
    db.ping(reconnect=True)
    sql = "select * from t_users where id='%s'" % user_id
    try:
        cur.execute(sql)  # 执行sql语句

        '''获取字段列表'''
        # print(cur.description)
        data_dict = []
        for field in cur.description:
            data_dict.append(field[0])
        # print(data_dict)
        # print(len(data_dict))

        '''获取字段内容'''
        results = cur.fetchall()  # 获取查询的所有记录
        # print(results)
        # print(list(results[0]))
        # print(len(list(results[0])))

        '''合并'''
        d1 = data_dict
        d2 = list(results[0])
        d3 = dict(zip(d1, d2))
        # print(d1)
        # print(d2)
        # print(d3['ramount'], type(d3['ramount']))
        # print(int(1.51), float(1.52))
        # n = '1.5'
        # x = d3['ramount']
        # print(float(x)+1.5)

        # 遍历结果
        # for row in results:
        #     id = row[0]
        # name = row[1]
        # password = row[2]
        # print(id, name, password)
        # print(id)
    except Exception as e:
        raise e
    finally:
        db.close()  # 关闭连接
        return d3


if __name__ == '__main__':
    pass
    # print(app_login())
    # print(token())
    # print(sclect_user('4294'))

    import time
    import datetime

    # np = 20190109
    #
    # n = datetime.datetime.now()
    # print(n)
    # n1 = n.strftime("%Y%m%d")
    # print(n1)
    # '{}-{}-{}'.format(n1[0:4], n1[4:6], n1[6:8])
    # print(n1[0:4])
    # print(n1[4:6])
    # print(n1[6:8])
    # n2 = '{}-{}-{}'.format(n1[0:4], n1[4:6], n1[6:8])
    # print(n2)
    # n3 = datetime.datetime.strptime(n2, '%Y-%m-%d')
    # print(n3)
    # n4 = n3 + datetime.timedelta(days=1)
    # print(n4)

    # n1 = n + datetime.timedelta(days=1)
    # print(n1.strftime("%Y%m%d"))

    # n = '2019-01-04 16:50:38'
    # # x = time.mktime(now_time.timetuple())
    # nn = datetime.datetime.strptime(n, '%Y-%m-%d %H:%M:%S')
    # print(nn)
    # nnn = time.mktime(nn.timetuple())
    # print(nnn)

    import os

    # if os.system('ps -ef | grep phantomjs') == 0:
    #     print('1')
    # else:
    #     print('2')
    # os.system("killall phantomjs")
    # print(os.system('ps -ef | grep phantomjs'))
    # print(os.system("killall phantomjs"))

    # x = '12345678'
    # print(x[-4:])
    # l = []
    # if l:
    #     print('1')
    # else:
    #     print("2")
    print()
