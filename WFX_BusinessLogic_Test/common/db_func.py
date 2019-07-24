# -*- coding: utf-8 -*-
# @Time    : 2019-07-23 09:42
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : db_func.py
# @Software: PyCharm


import pymysql


class MyPyMysql:
    def __init__(self, host=None, port=None, user=None, password=None, db=None):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.db = db

    def db_obj(self):
        """
        返回db对象
        :return:
        """
        try:
            database_obj = pymysql.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password,
                db=self.db)
            return database_obj
        except BaseException as e:
            return '连接数据库参数异常{}'.format(str(e))

    def create_data(self, sql=None):
        """
        新增
        :return:
        """
        try:
            db = self.db_obj()
            with db.cursor() as cur:
                print(sql)
                cur.execute(sql)
                db.commit()
                return 'create success'
        except BaseException as e:
            db.rollback()
            return '出现错误:{}'.format(str(e))

    def read_data(self, sql=None):
        """
        查询
        :param sql:
        :return:
        """
        try:
            db = self.db_obj()
            with db.cursor() as cur:
                cur.execute(sql)  # 执行sql语句
                # sql = "select * from gambler where id='YfpgoLZtEGPfMXUvFPffCi'"

                '''
                获取表结构,并且取出字段,生成列表
                '''
                '''获取字段列表'''
                # print(cur.description)
                key_list = [i[0] for i in cur.description]
                # print(key_list)

                '''
                把查询结果集组装成列表
                '''
                results = cur.fetchall()
                # print(results)
                data_list = [i for i in results]
                # print(data_list)

                data_dict = []
                for field in cur.description:
                    data_dict.append(field[0])
                # print(data_dict)
                # print(len(data_dict))

                '''
                将字段与每一条查询数据合并成键值对,并且组装成新的列表
                new_list = []
                for i in data_list:
                    print(list(i))
                    new_list.append(dict(zip(key_list, list(i))))
                '''
                new_list = [dict(zip(key_list, list(i))) for i in data_list]
                # print(new_list)
                return new_list
        except BaseException as e:
            return '出现错误:{}'.format(str(e))

    def update_data(self, sql=None):
        """
        更新
        :param sql:
        :return:
        """
        try:
            db = self.db_obj()
            with db.cursor() as cur:
                cur.execute(sql)
                db.commit()
                return 'update success'
        except BaseException as e:
            db.rollback()
            return '出现错误:{}'.format(str(e))

    def del_data(self, sql=None):
        """
        删除
        :param sql:
        :return:
        """
        try:
            db = self.db_obj()
            with db.cursor() as cur:
                cur.execute(sql)
                db.commit()
                return 'del success'
        except BaseException as e:
            db.rollback()
            return '出现错误:{}'.format(str(e))


import random

l = ['11.3', '1', '2', '3']
ac = random.choice(l)
print(ac)
u1 = [11.5, 222222222, 11.6, 11.7, 11.4, 11.3, 333333333, 11.8, 11.9, 12, 12.1, 12.2, 12.3, 12.4, 999999999,
      11.2, 11.1, 11, 10.9, 10.8, 10.7, 10.6]

print(len(u1))
