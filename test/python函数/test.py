#!/usr/bin/env python
# encoding: utf-8
'''
Python函数

1.是一个功能点
'''

def hello(canshu = 'canshu'):
    # print('输入内容是：', canshu)
    return '输入参数是：',canshu

if __name__ == '__main__':
    res = hello("参数")
    print(res)

