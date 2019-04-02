# -*- coding: utf-8 -*-
# @Time    : 2019/3/26 2:01 PM
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : h.py
# @Software: PyCharm

import datetime


def h(g_name, start_time, end_time):
    t_str1 = start_time
    t_str2 = end_time
    d1 = datetime.datetime.strptime(t_str1, '%Y-%m-%d')
    d2 = datetime.datetime.strptime(t_str2, '%Y-%m-%d')
    d3 = d2 - d1
    a1 = '{} ~ {}:一共:{}天'.format(start_time, end_time, d3.days)
    j_dict = {
        g_name: a1
    }
    return j_dict


if __name__ == '__main__':
    pass
    print(h('工作', '2011-11-17', datetime.datetime.now().strftime('%Y-%m-%d')))
    print(h('鸿粤', '2011-11-17', '2012-06-17'))
    print(h('安骅', '2012-09-13', '2014-03-01'))
    print(h('锦龙', '2014-03-03', '2015-03-03'))
    print(h('安捷', '2015-04-01', '2016-05-30'))
    print(h('中软', '2016-05-31', '2016-09-01'))
    print(h('V-态', '2016-09-08', '2017-07-28'))
    print(h('云美', '2017-08-08', '2018-08-20'))
    print(h('波浪', '2018-08-28', datetime.datetime.now().strftime('%Y-%m-%d')))
