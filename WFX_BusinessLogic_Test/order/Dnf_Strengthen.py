# -*- coding: utf-8 -*-
# @Time    : 2019/2/22 5:01 PM
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : Dnf_Strengthen.py
# @Software: PyCharm


import random


def rx(lv=0):
    """

    :param lv:
    :return:
    """
    if lv == 4 or lv == 5 or lv == 6:
        x_90 = list('0' * 9)
        x_90.append('1')
        x = random.choice(x_90)
        return int(x)

    if lv == 7:
        x_75 = list('0' * 7)
        a = ['1', '1']
        x_75.extend(a)
        x = random.choice(x_75)
        return int(x)

    if lv == 8:
        x_50 = list('0' * 50)
        a = list('1' * 50)
        x_50.extend(a)
        x = random.choice(x_50)
        return int(x)

    if lv == 9:
        x_40 = list('0' * 40)
        a = list('1' * 60)
        x_40.extend(a)
        x = random.choice(x_40)
        return int(x)

    if lv == 10:
        x_30 = list('0' * 30)
        a = list('1' * 70)
        x_30.extend(a)
        x = random.choice(x_30)
        return int(x)

    if lv == 11:
        x_20 = list('0' * 20)
        a = list('1' * 80)
        x_20.extend(a)
        x = random.choice(x_20)
        return int(x)

    if lv == 12:
        x_10 = list('0' * 10)
        a = list('1' * 90)
        x_10.extend(a)
        x = random.choice(x_10)
        return int(x)

    if lv == 13:
        x_10 = list('0' * 5)
        a = list('1' * 95)
        x_10.extend(a)
        x = random.choice(x_10)
        return int(x)

    if lv == 14:
        x_10 = list('0' * 5)
        a = list('1' * 95)
        x_10.extend(a)
        x = random.choice(x_10)
        return int(x)

    if lv == 15:
        x_10 = list('0' * 5)
        a = list('1' * 95)
        x_10.extend(a)
        x = random.choice(x_10)
        return int(x)


def qf(lv=None, play_id='旭旭宝宝', wq_name='苍穹'):
    """
    0～4:  100%
    5~7:   90%
    8:     75%
    9:     50%
    10:    40%
    11:    30%:
    12:    20%:
    13:    10%:
    """
    if lv <= 3:
        print('玩家[{}]强化 +{} {} 成功'.format(play_id, lv + 1, wq_name))

    if lv > 3:
        if rx(lv) == 0:
            print('玩家[{}]强化 +{} {} 成功'.format(play_id, lv + 1, wq_name))
        else:
            print('玩家[{}]强化 +{} {} 失败'.format(play_id, lv + 1, wq_name))


if __name__ == '__main__':
    pass

    for i in range(0, 15):
        qf(14)
