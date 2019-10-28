#!/usr/bin/env python
# encoding: utf-8
'''
@author: Leq
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: leierqiang123@gmail.com
@software: Pycharm
@file: get_youhuiquan_test.py.py
@time: 2019/8/29 0029 上午 9:02
@desc:
'''


import requests

r = requests.get('https://github.com/timeline.json')
print(r.text)
