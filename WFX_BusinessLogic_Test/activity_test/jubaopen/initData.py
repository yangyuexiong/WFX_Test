# -*- coding: utf-8 -*-
# @Time    : 2019-08-07 10:04
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : initData.py
# @Software: PyCharm


from common.db_list import db
import time

"""修改活动 开始/结束 时间"""
db.update_data(sql="update t_activity set start_time={} where id ='{}' ".format(1565107200, 35))
db.update_data(sql="update t_activity set end_time={} where id ='{}' ".format(1565230500, 35))

"""获取所有测试账号的id"""
# id_list = []
# for i in db.read_data(sql="SELECT * FROM `tiger_test`.`t_users` WHERE `phone` LIKE '%150123456%'"):
#     id_list.append(i['id'])
# print(id_list)


"""添加队员"""
test_id = [16380, 16381, 16382, 16383, 16384, 16385, 16386, 16387, 16388, 16389, 16390, 16391, 16392,
           16393, 16394, 16395, 16396, 16397, 16398]

# for i in test_id:
#     db.create_data(
#         sql="insert into t_activity_team(activity_id, user_id,recommend_user_id,team_id,is_new,create_time,remark) values('{}', '{}', '{}', '{}', '{}', '{}', '{}')". \
#             format(35, i, 4294, 4294, 1, int(time.time()), 0))
if __name__ == '__main__':
    pass
