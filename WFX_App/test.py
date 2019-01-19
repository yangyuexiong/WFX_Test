# -*- coding: utf-8 -*-
# @Time    : 2018/10/10 下午4:02
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : test.py
# @Software: PyCharm

from appium import webdriver
import yaml
import logging.config


# CON_LOG = '../config/log.conf'
# logging.config.fileConfig(CON_LOG)
# logging = logging.getLogger()
#
# with open('../config/app.yaml', 'r', encoding='utf-8') as file:
#     data = yaml.load(file)


def appium_android():
    config = {
        'platformName': 'Android',  # 平台
        'platformVersion': '6.0.1',  # 系统版本
        # 'deviceName': 'S25QBDPD22PLH',  # 测试设备ID S25QBDPD22PLH
        'deviceName': 'eceaa863',  # 测试设备ID 3452a8f4
        'appPackage': 'com.wavehk.android',  # 包名
        'appActivity': '.app.launch.LaunchActivity',  # 启动Activity
        'newCommandTimeout': 3600,
        'automationName': 'Appium',
        'unicodeKeyboard': True,  # 编码,可解决中文输入问题
        'resetKeyboard': True,
        'noReset': True  # 不重置应用状态
    }
    # logging.info('-开始启动app-')
    driver = webdriver.Remote('http://localhost:4723/wd/hub', config)
    driver.implicitly_wait(8)
    return driver


if __name__ == '__main__':
    # appium_android()
    driver = appium_android()
    print(driver)
    from time import sleep
    sleep(5)
    driver.find_elements_by_id('com.wavehk.android:id/butten1').click()
    driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout[1]").click()
