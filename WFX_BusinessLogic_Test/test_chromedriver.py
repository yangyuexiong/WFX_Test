# -*- coding: utf-8 -*-
# @Time    : 2019-05-27 09:45
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : test_chromedriver.py
# @Software: PyCharm

'''http://chromedriver.storage.googleapis.com/index.html'''

import requests

u = 'https://www.google.com'
lo = requests.get(u)
print(lo.text)
