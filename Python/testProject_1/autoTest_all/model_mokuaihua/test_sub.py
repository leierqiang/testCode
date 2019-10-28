#!/usr/bin/env python
# encoding: utf-8
'''
减法测试用例
'''

from StartEnd import *
from calculator import *


class TestSub(Setup_TearDown):
    """
    用例 测试用例必须以test开头
    :return:
    """
    def test_sub(self):
        """
        用例
        :return:
        """
        j=Math_sub(5, 10)
        self.assertEqual(j.sub(), -5)
        # self.assertEqual(j.add_num(), 12)  #断言失败