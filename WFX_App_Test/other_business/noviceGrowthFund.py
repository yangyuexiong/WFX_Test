# -*- coding: utf-8 -*-
# @Time    : 2018/10/22 下午4:21
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : noviceGrowthFund.py
# @Software: PyCharm


from other_business.public_func import db, get_user_id, user_init, set_time


def set_follow(acc, days):
    d = set_time(days)
    u_id = get_user_id(acc)
    for i in d.items():
        print(i)

    c = db.cursor()
    c2 = db.cursor()

    insert_follow = """insert into t_usersfollow(userid,an_id,follow_price,stop_price,accounttype,starttime) values('%s','234','500','250','real','%s')"""
    update_follow_time = "update t_usersfollow set starttime = '%s' where userid = '%s'"

    print('insert the follow')
    try:
        c.execute(insert_follow % (u_id, d['当前时间戳']))
        db.commit()
    except BaseException as e:
        print(e)
        db.rollback()

    print('update follow starttime ')
    try:
        c2.execute(update_follow_time % (d['推移后时间戳'], u_id))
        db.commit()
    except BaseException as e:
        print(e)
        db.rollback()
    print('done')


if __name__ == '__main__':
    # user_init('e@126.com') # 创建帐号
    set_follow('e@126.com', 8)  # 添加跟随记录并且修改时间戳
