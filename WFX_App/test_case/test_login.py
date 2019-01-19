# -*- coding: utf-8 -*-
# @Time    : 2018/10/3 下午12:51
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : test_login.py
# @Software: PyCharm

from common.myunit import StartEnd
from common.common_fun import Common


class LoginTest(StartEnd, Common):
    def test_login1_normal(self):
        '''1.正确的用户名与密码'''
        self.getScreenShot('okc')
