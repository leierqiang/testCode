#!/usr/bin/env python
# encoding: utf-8
'''
@author: Leq
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: leierqiang123@gmail.com
@software: Pycharm
@file: unittest_test.py.py
@time: 2019/9/7 0007 下午 4:37
@desc:
'''


# 1.Python中 assert 断言 的概念
assert 3<=5, 'not True'

# 2. unittest的3个概念
# Test Fixture  测试环境搭建
# Test Case 测试用例
# Test Suit 测试用例集合

# 3.Python unittest简单框架demo
import unittest

class MyTestCase(unittest.TestCase):
    def setUP(self):
        print("环境预测")

    def test_something(self):
        """
        测试用例
        :return:
        """
        print("测试用例")
    #     断言
        self.assertEquals(True, True)

    def tearDown(self):
        print("环境销毁")

if __name__ == "__main__":
    unittest.main()

# 4.Python unittest框架demo2
import unittest


class TestCase1(unittest.TestCase):
    """
    用例集合1
    """
    def testCase1(self):
        print("这是第一个测试用例")

    def testCase2(self):
        print("这是第2个测试用例")

    def testCase3(self):
        print("这是第3个测试用例")

class TestCase2(unittest.TestCase):
    """
    用例集合2
    """
    def testCase1(self):
        print("这是第一个测试用例")

    def testCase2(self):
        print("这是第2个测试用例")

    def testCase3(self):
        print("这是第3个测试用例")

if __name__ == '__main__':
    # 执行各个测试集合
    suitel = unittest.TestLoader().loadTestsFromTestCase(TestCase1)
    suite2 = unittest.TestLoader().loadTestsFromTestCase(TestCase2)
    suite = unittest.TestSuite([suitel, suite2])
    unittest.TextTestRunner(verbosity=2).run(suite)
