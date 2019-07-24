# -*- coding: utf-8 -*-
# @Time    : 2019-07-23 09:38
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : dataReady.py
# @Software: PyCharm

from common.db_func import MyPyMysql

db = MyPyMysql(host="120.79.145.200", user="tiger_test", password="123123", db="tiger_test", port=3306)

activity_id = 39

if __name__ == '__main__':
    pass
    s = "SELECT * FROM t_activity WHERE id='{}'".format(activity_id)
    act = db.read_data(s)
    print(act)

    s1 = "SELECT * FROM t_users_activity WHERE activity_id='{}'".format(activity_id)
    act_user = db.read_data(s1)
    print(act_user)
