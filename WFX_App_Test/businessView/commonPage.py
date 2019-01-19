# -*- coding: utf-8 -*-
# @Time    : 2018/10/12 下午4:13
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : commonPage.py
# @Software: PyCharm

from common.common_func import Common, NoSuchElementException, By
from businessView.loginView import LoginView
import logging
from time import sleep


class CommonPage(LoginView):
    index = (By.ID, 'com.wavehk.android:id/foot_a')  # 首页
    follow = (By.ID, 'com.wavehk.android:id/foot_b')  # 跟TA赚
    quotation = (By.ID, 'com.wavehk.android:id/foot_c')  # 行情

    guide = (By.ID, 'com.wavehk.android:id/butten1')  # 新手指南
    guide_nei = (By.ID, 'com.wavehk.android:id/view_action_bar_title')  # 新手指南-内页

    rankings = (By.ID, 'com.wavehk.android:id/butten2')  # 收益排行
    rankings_nei = (By.ID, 'com.wavehk.android:id/view_top_change_btn1')  # 收益排行-内页
    rankings_nei2 = (By.ID, 'com.wavehk.android:id/view_top_change_btn2')  # 收益排行-内页

    capital = (By.ID, 'com.wavehk.android:id/butten3')  # 资金服务
    capital_b = (By.ID, 'com.wavehk.android:id/cancel_btn')  # 资金服务-取消
    capital_l = (By.ID, 'com.wavehk.android:id/go_btn')  # 资金服务-跳登录
    capital_nei = (By.ID, 'com.wavehk.android:id/view_action_bar_title')  # 资金服务-内页

    rt = (By.ID, 'com.wavehk.android:id/view_action_bar_back')  # 返回
    rt1 = (By.ID, 'com.wavehk.android:id/back_icon')  # 返回
    rt2 = (By.ID, 'com.wavehk.android:id/view_action_bar_back')  # 返回

    shi_chang = (By.XPATH,
                 '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ViewFlipper/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout[1]/android.widget.RelativeLayout')
    price = (By.ID, 'com.wavehk.android:id/text2')  # 报价

    zuo_ri = (By.XPATH,
              '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ViewFlipper/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[3]/android.widget.LinearLayout[1]/android.widget.RelativeLayout')

    transaction = (By.ID, 'com.wavehk.android:id/text2')  # 自主交易

    p_activities = (By.XPATH,
                    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ViewFlipper/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[4]/android.widget.LinearLayout/android.widget.RelativeLayout')

    def check_banner(self):
        """banner测试"""
        pass

    def check_index(self, username, password):
        """首页入口"""
        logging.info('===首页===')
        self.find_element(*self.index).click()

        logging.info('===新手指南===')
        self.find_element(*self.guide).click()
        sleep(0.8)
        self.check_into_status('新手指南')
        self.find_element(*self.rt).click()

        logging.info('===收益排行===')
        self.find_element(*self.rankings).click()
        sleep(0.8)
        self.check_into_status('收益排行')
        self.find_element(*self.rt1).click()

        logging.info('===资金服务===')
        self.find_element(*self.capital).click()
        sleep(0.8)
        try:
            self.find_element(*self.capital_b).click()  # 取消
            self.find_element(*self.capital).click()
            self.find_element(*self.capital_l).click()
            logging.info('===执行登录===')
            self.pwd_login(username, password)
            self.find_element(*self.index).click()
            self.find_element(*self.capital).click()
            self.check_into_status('资金服务')
            self.find_element(*self.rt2).click()
        except BaseException:
            self.find_element(*self.capital_nei).click()
            self.check_into_status('资金服务')
            self.find_element(*self.rt2).click()

    def check_quotation(self):
        """市场行情"""
        logging.info('===市场行情===')
        self.find_element(*self.shi_chang).click()
        self.check_into_status('市场行情')

    def check_zr(self):
        """昨日排行榜"""
        logging.info('===昨日排行榜===')
        self.find_element(*self.zuo_ri).click()
        self.check_into_status('昨日排行榜')

    def check_p_activities(self):
        """优惠活动"""
        logging.info('===优惠活动===')
        # self.swipe(535, 979, 524, 605, 0.3)
        self.driver.swipe(535, 979, 524, 605, 0.3)
        self.find_element(*self.p_activities).click()
        self.check_into_status('优惠活动')

    def check_into_status(self, case):
        """断言入口结果"""
        logging.info('=====check_into_status:%s====' % case)
        try:
            if self.driver.find_element(*self.guide_nei) or self.driver.find_element(
                    *self.rankings_nei) or self.driver.find_element(*self.capital_nei) or self.driver.find_element(
                *self.price) or self.driver.find_element(*self.transaction):
                return True
        except NoSuchElementException:
            return False
