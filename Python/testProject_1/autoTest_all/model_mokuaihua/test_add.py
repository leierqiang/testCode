#!/usr/bin/env python
# encoding: utf-8

'''
加法测试
'''

from StartEnd import *
from calculator import *

class TestAdd(Setup_TearDown):
    """
    用例1 测试用例必须以test开头
    :return:
    """
    def test_add(self):
        j=Math_add(5, 10)
        self.assertEqual(j.add(), 15)
        # self.assertEqual(j.add_num(), 12)  #断言失败