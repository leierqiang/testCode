#!/usr/bin/env python
# encoding: utf-8

import unittest
from calculator import *

class TestMath(unittest.TestCase):
    def setUP(self):
        print("环境监察，测试开始")

    def test_add(self):
        """
        用例1 测试用例必须以test开头
        :return:
        """
        j=Math_add(5, 10)
        self.assertEqual(j.add(), 15)
        # self.assertEqual(j.add_num(), 12)  #断言失败

    def test_sub(self):
        """
        用例2
        :return:
        """
        j=Math_sub(5, 10)
        self.assertEqual(j.sub(), -5)
        # self.assertEqual(j.add_num(), 12)  #断言失败


    def tearDown(self):
        print("测试结束，环境销毁")

# 改进  将通用部分提取出来----------------------------------------
class TestMath_2(unittest.TestCase):
    def setUP(self):
        print("环境监察，测试开始")

    def tearDown(self):
        print("测试结束，环境销毁")

class TestAdd(TestMath_2):
    """
    用例1 测试用例必须以test开头
    :return:
    """
    def test_add(self):
        j=Math_add(5, 10)
        self.assertEqual(j.add(), 15)
        # self.assertEqual(j.add_num(), 12)  #断言失败

class TestSub(TestMath_2):
    """
    用例2 测试用例必须以test开头
    :return:
    """
    def test_sub(self):
        """
        用例2
        :return:
        """
        j=Math_sub(5, 10)
        self.assertEqual(j.sub(), -5)
        # self.assertEqual(j.add_num(), 12)  #断言失败



if __name__ == "__main__":
    suite=unittest.TestSuite()
    suite.addTest(TestMath("test_add"))
    suite.addTest(TestMath("test_sub"))
    runer=unittest.TextTestRunner()
    runer.run(suite)

    # 或者如下格式
    # unittest.TextTestRunner(verbosity=2).run(suite)