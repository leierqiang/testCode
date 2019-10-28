#!/usr/bin/env python
# encoding: utf-8

# 开始与结束  setUp 与 tearDown

import unittest

class Setup_TearDown(unittest.TestCase):
    def setUP(self):
        print("环境监察，测试开始")

    def tearDown(self):
        print("测试结束，环境销毁")