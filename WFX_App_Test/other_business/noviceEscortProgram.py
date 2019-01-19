# -*- coding: utf-8 -*-
# @Time    : 2018/10/22 上午11:29
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : noviceEscortProgram.py
# @Software: PyCharm

import requests
import datetime
import time
import pymysql

now_time = datetime.datetime.now()  # 当前时间
delta = datetime.timedelta(days=8)  # 时间差
result_time = now_time - delta  # 需要使用的时间
print('当前时间:{}'.format(now_time))
print('结果时间:{}'.format(result_time))
un_time = time.mktime(result_time.timetuple())  # datetime转时间戳
print('转时间戳:{}'.format(un_time))

d = {
    'user_id': '',
    'income': '',
}

db = pymysql.connect(host="120.79.145.200", user="tiger_test",
                     password="123123", db="tiger_test", port=3306)


def func(acc, m):
    """
    1.设置跟随时间
    2.设置亏损金额
    """
    select_user = "select * from t_users where email='%s'" % acc
    select_users_follow = "select * from t_usersfollow where userid='%s'"
    set_income = "update t_usersfollow set income='%s' where userid = '%s' "
    update_follow_starttime = "update t_usersfollow set starttime = '%s' where userid = '%s'"

    c1 = db.cursor()
    c2 = db.cursor()
    c3 = db.cursor()
    c4 = db.cursor()
    db.ping(reconnect=True)
    try:

        """user"""
        c1.execute(select_user)
        results = c1.fetchall()
        print('======获取user_id:%s======' % results, '\n')
        for i in results:
            d['user_id'] = i[0]
            # print(d)

        """users_follow"""
        c2.execute(select_users_follow % (d['user_id']))
        results2 = c2.fetchall()
        print('======获取跟随记录:%s======' % results2, '\n')
        if results2:
            c3.execute(set_income % (m, d['user_id']))  # 设置亏损金额
            c4.execute(update_follow_starttime % (un_time, d['user_id']))  # 设置跟投时间
            db.commit()
            print('======设置亏损金额: income==%s======' % m)
            d['income'] = m
            print('set ok')

    except Exception as e:
        db.rollback()
    finally:
        pass


def start_task(base_url):
    """
    执行定时任务:https://ptest.wavehk.cn/task/crontab/safeguards
    """
    try:
        r = requests.get(base_url)
        return True
    except BaseException as e:
        print(e)
        return False


def select_rr():
    """
    检查数据是否正确
    """
    try:
        sql = "select * from t_users_activity where activity_id = '10'"
        c = db.cursor()
        c.execute(sql)
        results = c.fetchall()
        print('======检查数据:%s======' % results, '\n')
        for i in results:
            r_id = i[0]
            u_id = i[2]
            activity_info = i[5]
            return u_id, activity_info, r_id
    except Exception as e:
        db.rollback()
    finally:
        pass


def del_msg(i):
    try:
        sql = "delete from t_users_activity where id = '%s'" % i
        c = db.cursor()
        c.execute(sql)
        db.commit()
    except BaseException:
        db.rollback()


if __name__ == '__main__':
    func('c@126.com', '-10')
    start_task('https://ptest.wavehk.cn/task/crontab/safeguards')
    r = select_rr()
    # print(abs(float(r[1])))
    # print(abs(float(d['income'])))

    if r[0] == d['user_id']:
        print('checking...')

        if abs(float(d['income'])) <= 20:  # 亏损金额<=20
            print('亏损金额<=20')
            assert abs(float(r[1])) == abs(float(d['income']))
        else:
            print('亏损金额>20')
            assert abs(float(r[1])) == 20
        print('check success')

    # del_msg(r[2])
