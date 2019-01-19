# -*- coding: utf-8 -*-
# @Time    : 2018/10/23 下午4:00
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : public_func.py
# @Software: PyCharm


import pymysql
import requests
import time
import datetime

db = pymysql.connect(host="120.79.145.200", user="tiger_test",
                     password="123123", db="tiger_test", port=3306)


def set_time(days):
    time_dist = {
        '当前时间': '',
        '当前时间戳': '',
        '向前推移天数': '',
        '推移后时间': '',
        '推移后时间戳': '',
    }
    now_time = datetime.datetime.now()  # 当前时间
    now_time2 = time.mktime(now_time.timetuple())  # 当前时间戳

    delta = datetime.timedelta(days=days)  # 时间差
    result_time = now_time - delta  # 需要使用的时间

    un_time = time.mktime(result_time.timetuple())  # datetime转时间戳

    time_dist['当前时间'] = now_time
    time_dist['当前时间戳'] = now_time2
    time_dist['向前推移天数'] = delta
    time_dist['推移后时间'] = result_time
    time_dist['推移后时间戳'] = un_time
    return time_dist


# get user_id
def get_user_id(acc):
    c = db.cursor()
    select_user = "select * from t_users where email='%s'" % acc
    try:
        c.execute(select_user)
        r = c.fetchall()
        if r:
            for i in r:
                u = i[0]
                print(u)
                return u
    except BaseException as e:
        print(e)
        db.rollback()
    finally:
        pass


def register_user():
    base_url1 = 'https://ptest.wavehk.cn/v2/user/ruleCode'
    base_url2 = 'https://ptest.wavehk.cn/v2/user/setPwd'
    base_url3 = 'https://ptest.wavehk.cn/v2/user/uploadIdCard'
    base_url4 = 'https://ptest.wavehk.cn/v2/user/setTransactionPassWord'

    header = {
        "token": ""
    }

    param_data1 = {
        "sign": "5sCioY2cazwBz0aN\/Wa755izJuPHKOXbB1wY3KHwmasOqvCmlTeLyYRsD4Mr\/F8d",
        "mobile_fiex": "86",
        "version": "2.2.1",
        "code": "1111",
        "apptype": "ios",
        "phone": "e@126.com",
        "type": "login",
        "did": "12345dg"
    }

    param_data2 = {
        "version": "2.2.1",
        "apptype": "ios",
        "code_token": "125aa95be9808546c7fc1c71f5456f61",
        "did": "12345dg",
        "sign": "5sCioY2cazwBz0aN\/Wa756ddsUIR4M4jjgmjZo6nPS0bFLl7vmmTsa87IhgWvPRe",
        "pwd": "yyy333"
    }

    param_data3 = {
        "idcard": "13922129963",
        "surname": "跃",
        "sign": "5sCioY2cazwBz0aN\/Wa7535iCPBV\/J1uZCFx7tALW5q1qS5xIONiPg5\/GuVS9eGb",
        "name": "神",
        "idcard2": "7505fd9e-c384-47ba-b993-41d5477b6d29",
        "version": "2.2.1",
        "type": "2",
        "apptype": "ios",
        "idcard1": "7425560a-56e8-4575-919e-d4607876253a",
        "did": "12345dg"
    }

    param_data4 = {
        "apptype": "ios",
        "password": "666666",
        "did": "12345dg",
        "sign": "5sCioY2cazwBz0aN\/Wa758JSX+45Vzv5czGwlkFTvZawHrBugm1H9BDSMBFeNRVv",
        "version": "2.2.1"
    }

    r1 = requests.post(base_url1, json=param_data1)
    print(r1.json()['data']['code_token'])
    code_token = r1.json()['data']['code_token']
    print('===r1===')

    param_data2['code_token'] = code_token
    r2 = requests.post(base_url2, json=param_data2)
    print(r2.json()['data']['token'])
    print('===r2===')

    token = r2.json()['data']['token']
    header['token'] = token
    r3 = requests.post(base_url3, json=param_data3, headers=header)
    print(r3.json())
    print('===r3===')

    r4 = requests.post(base_url4, json=param_data4, headers=header)
    print(r4.json())
    print('===r4===')


def user_init(acc):
    c = db.cursor()
    del_user = "delete from t_users where id = '%s'"
    try:
        u = get_user_id(acc)
        c.execute(del_user % u)
        db.commit()
    except BaseException as e:
        print(e)
        db.rollback()

    print('===注册===')
    register_user()
    print('===done===')


if __name__ == '__main__':
    # user_init('e@126.com')
    # get_user_id('e@126.com')
    print(set_time(8)['推移后时间戳'])
