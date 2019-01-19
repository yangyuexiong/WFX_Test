# -*- coding: utf-8 -*-
# @Time    : 2019/1/2 4:48 PM
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : test_db.py
# @Software: PyCharm

import pymysql

db = pymysql.connect(host="120.79.145.200", user="tiger_test",
                     password="123123", db="tiger_test", port=3306)
