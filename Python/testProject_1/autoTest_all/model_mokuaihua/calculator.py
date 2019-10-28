#!/usr/bin/env python
# encoding: utf-8
'''
这里写具体的功能，指的是加减的方法
'''

class Math_add(object):
    def __init__(self, a, b):
        # print("求和得：", a+b)
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b


class Math_sub(object):
    def __init__(self, a, b):
        # print("相减得：", a+b)
        self.a = a
        self.b = b

    def sub(self):
        return self.a - self.b