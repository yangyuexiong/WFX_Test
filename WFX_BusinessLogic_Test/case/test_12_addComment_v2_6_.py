# -*- coding: utf-8 -*-
# @Time    : 2019/2/19 5:46 PM
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : test_12_addComment_v2_6_.py
# @Software: PyCharm


from common.ban_warning import *
from common.public_func import *
from common.capital_func import *
from common.myunit import StartEnd
import unittest
import requests
from time import sleep

header = {
    'token': token()
}

url1 = 'https://ptest.wavehk.cn/v2/quotation/addQuotationComment'

historical_order = []

p1 = {
    "sign": "5sCioY2cazwBz0aN\/Wa75xb07vUddrbQMmX3aq28E\/9uGGM2FzzByx\/HUhp3\/nzp",
    "position_id": "37435,27247,27104",
    "quotation_id": "2",
    "content": "all comments",
    "audio_length": "",
    "image": "a4d06d76-67b2-4cfc-8726-63daf0482729",
    "did": "12345dg",
    "version": "2.5.1",
    "apptype": "ios"
}


# 评论
class AddCommentMain(StartEnd):

    def test_04(self):
        """文字+图片+订单"""
        lo = requests.post(url1, json=p1, headers=header, verify=False)
        # print(lo.json())
        assert_json(lo.json(), 'code', 0)
        assert_json(lo.json(), 'message', '评论成功!')

    def test_05(self):
        """只有内容"""
        sleep(4)
        p1['content'] = 't1'
        p1['image'] = ''
        p1['position_id'] = ''
        lo = requests.post(url1, json=p1, headers=header, verify=False)
        # print(lo.json())
        assert_json(lo.json(), 'code', 0)
        assert_json(lo.json(), 'message', '评论成功!')

    def test_06(self):
        """文字+订单"""
        sleep(4)
        p1['content'] = 't2'
        p1['image'] = ''
        p1['position_id'] = '37435,27247,27104'
        lo = requests.post(url1, json=p1, headers=header, verify=False)
        # print(lo.json())
        assert_json(lo.json(), 'code', 0)
        assert_json(lo.json(), 'message', '评论成功!')

    def test_07(self):
        """文字+图片"""
        sleep(5)
        p1['content'] = 't3'
        p1['image'] = 'a4d06d76-67b2-4cfc-8726-63daf0482729'
        p1['position_id'] = ''
        lo = requests.post(url1, json=p1, headers=header, verify=False)
        # print(lo.json())
        assert_json(lo.json(), 'code', 0)
        assert_json(lo.json(), 'message', '评论成功!')


class AddCommentVice(StartEnd):
    n = 10
    image_list = 'a4d06d76-67b2-4cfc-8726-63daf0482729,' * n
    image_list1 = image_list[:-1]
    position_id = '37435,27247,27104,27086,26468,25242'
    content = 'ok' * 200

    def test_01(self):
        """图片超出9张"""
        p1['content'] = '图片超出9张'
        p1['image'] = self.image_list1
        p1['position_id'] = ''
        lo = requests.post(url1, json=p1, headers=header, verify=False)
        # print(lo.json())
        assert_json(lo.json(), 'code', 5001)
        assert_json(lo.json(), 'message', '图片超出上传限制!')

    def test_02(self):
        """订单超过3条"""
        p1['content'] = '订单超过3条'
        p1['image'] = ''
        p1['position_id'] = self.position_id
        lo = requests.post(url1, json=p1, headers=header, verify=False)
        # print(lo.json())
        assert_json(lo.json(), 'code', 5001)
        assert_json(lo.json(), 'message', '订单分享超出限制!')

    def test_03(self):
        """内容超过200个字符串"""
        p1['content'] = self.content
        p1['image'] = ''
        p1['position_id'] = ''
        lo = requests.post(url1, json=p1, headers=header, verify=False)
        # print(lo.json())

    def test_04(self):
        """内容为空"""
        p1['content'] = ''
        lo = requests.post(url1, json=p1, headers=header, verify=False)
        # print(lo.json())
        assert_json(lo.json(), 'code', 5002)
        assert_json(lo.json(), 'message', '请输入评论内容')


# 回复评论
class ReplyToComments(StartEnd):

    def test_01(self):
        """回复内容为空"""

    def test_02(self):
        """回复内容超过200字符"""

    def test_03(self):
        """回复语音"""

    def test_04(self):
        """回复内容符合规则"""


# 审核评论后显示
class ExamineComments(StartEnd):

    def test_01(self):
        """未审核"""

    def test_02(self):
        """审核不通过"""

    def test_03(self):
        """审核通过"""

    def test_04(self):
        """"""


if __name__ == '__main__':
    unittest.main()
