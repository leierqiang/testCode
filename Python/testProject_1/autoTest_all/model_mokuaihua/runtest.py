#!/usr/bin/env python
# encoding: utf-8

# 用例执行管理

import unittest

test_dir = './'
discover=unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')
if __name__ == '__main__':
    runner=unittest.TextTestRunner()
    runner.run(discover)