# -*- coding: utf-8 -*-
# @Time    : 2019-07-23 14:43
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : test_01.py
# @Software: PyCharm

import time
import unittest

from activity_test.feinong.dataReady import db, activity_id

start_time = int(time.time()) + 1
end_time = start_time + 864000

u1 = [11.5, 222222222, 11.6, 11.7, 11.4, 11.3, 333333333, 11.8, 11.9, 12, 12.1, 12.2, 12.3, 12.4, 999999999,
      11.2, 11.1, 11, 10.9, 10.8, 10.7, 10.6]

u2 = [222222222, 11.6, 11.7, 11.4, 11.3, 333333333, 11.8, 11.9, 12, 12.1, 12.2, 12.3, 12.4, 999999999,
      11.2, 11.1, 11, 10.9, 10.8, 10.7, 10.6]

u3 = [333333333, 11.8, 11.9, 12, 12.1, 12.2, 12.3, 12.4, 999999999,
      11.2, 11.1, 11, 10.9, 10.8, 10.7, 10.6]

u4 = [12345678, 87654321]


class CheckNumber(unittest.TestCase):
    """
    t_order 删除记录
    """
    @unittest.skip('pass')
    def test_01(self):
        """充值次数"""
        sql = "SELECT * FROM t_users WHERE id = '{}'".format(activity_id)
        print(db.read_data(sql))
        print(db.read_data(sql)[0]['total_lottery_num'])


class ResetTestData(unittest.TestCase):
    """
    开奖后执行此类,然后继续进行开奖。
    """

    def test_01(self):
        """重置开奖"""
        sql = "update t_activity set remark2 = '',start_time={},end_time={} where id ='{}' ".format(start_time,
                                                                                                    end_time,
                                                                                                    activity_id)
        db.update_data(sql)

    def test_02(self):
        """清空测试用户"""
        sql = "DELETE FROM t_users_activity WHERE activity_id = '{}'".format(activity_id)
        db.del_data(sql)

    def test_03(self):
        """设置测试用户"""
        """
        34, 4294, 0, 0, '11.3', 1557110042, 0, NULL, 0, 'real', 0.00, ''
        """
        user_list = ['4294']

        time = start_time - 100
        for i in range(0, 22):
            # 开奖号码: 11.5

            global u1
            global u2
            global u3
            global u4

            """同时获得 一二三等奖 各一次 且不能获得参与奖"""
            sql = "insert into t_users_activity(activity_id, user_id, an_id, follow_id, activity_info, create_time, update_time, remark, type, accounttype, lock_money, remark2) values('{}', '{}', 0, 0, '{}', '{}', 0, NULL, 0, 'real', 0.00, '')".format(
                activity_id, 4294, u1[0], time)
            db.create_data(sql)
            u1.pop(0)

            if len(u2) != 0:
                """同时获得 二三等奖 各一次 且不能获得参与奖"""
                sql = "insert into t_users_activity(activity_id, user_id, an_id, follow_id, activity_info, create_time, update_time, remark, type, accounttype, lock_money, remark2) values('{}', '{}', 0, 0, '{}', '{}', 0, NULL, 0, 'real', 0.00, '')".format(
                    activity_id, 8855, u2[0], time)
                db.create_data(sql)
                u2.pop(0)

            if len(u3) != 0:
                """获得 三等奖 且不能获得参与奖"""
                sql = "insert into t_users_activity(activity_id, user_id, an_id, follow_id, activity_info, create_time, update_time, remark, type, accounttype, lock_money, remark2) values('{}', '{}', 0, 0, '{}', '{}', 0, NULL, 0, 'real', 0.00, '')".format(
                    activity_id, 8866, u3[0], time)
                db.create_data(sql)
                u3.pop(0)

            if len(u4) != 0:
                """获得 参与奖 一次 且不能获得 一二三等奖"""
                sql = "insert into t_users_activity(activity_id, user_id, an_id, follow_id, activity_info, create_time, update_time, remark, type, accounttype, lock_money, remark2) values('{}', '{}', 0, 0, '{}', '{}', 0, NULL, 0, 'real', 0.00, '')".format(
                    activity_id, 8877, u4[0], time)
                db.create_data(sql)
                u4.pop(0)


if __name__ == '__main__':
    pass
    unittest.main()
