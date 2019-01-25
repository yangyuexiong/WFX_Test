# -*- coding: utf-8 -*-
# @Time    : 2019/1/7 5:10 PM
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : run.py
# @Software: PyCharm


import unittest
from common.HTMLTestReportCN import HTMLTestRunner
import time
import sys

path = '/Users/yangyuexiong/Desktop/WFX_BusinessLogic_Test'
sys.path.append(path)

# 报告路径
report_dir = './reports'
# 测试路径
test_dir = './case'

# 测试路径，匹配规则
discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')

# 时间拼接报告名称
now = time.strftime('%Y-%m-%d %H_%M_%S')
report_name = report_dir + '/' + now + '.html'

# 打开-生成测试报告
with open(report_name, 'wb') as f:
    print('f:', f)
    runner = HTMLTestRunner(stream=f, title='自动化测试报告', description='回归测试')
    runner.run(discover)
    f.close()

    # from common.public_func import latest_report, send_mail

    # print('查找最新报告')
    # latest_report = latest_report(report_dir)
    # print(latest_report)
    # print('发送报告到邮箱')
    # send_mail(latest_report)

if __name__ == '__main__':
    pass
