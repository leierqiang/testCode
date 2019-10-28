#!/usr/bin/env python
# encoding: utf-8
# 日志分debug、info、 warnning、error、critical默认是从warning开始记录的

# import logging
#
#
# logging.basicConfig(level=logging.INFO,
#                     # 从info级别开始打印日志
#                     # 日志格式
#                     format='%(asctime)s %(name)s %(levelname)s %(message)s',
#                     # 有上面的asctime就必须对应下面的日期格式
#                     datefmt='%Y-%m-%d %H:%M:%S',
#                     # 指定对应路径
#                     filename=r'.\test.log'
#                     )
#
# logging.debug('我是一个debug')
# logging.info('我是一个info')
# logging.warning('我是一个warning')
# logging.error('我是一个error')
# logging.critical('我是一个critical')



import logging

LOG_FORMAT = "%(asctime)s %(name)s %(levelname)s %(message)s"
LOG_DATEFMT = "%Y-%m-%d %H:%M:%S"

logging.basicConfig(level=logging.INFO,
                    # 从info级别开始打印日志
                    # 日志格式
                    format=LOG_FORMAT,
                    # 有上面的asctime就必须对应下面的日期格式
                    datefmt=LOG_DATEFMT,
                    # 指定对应路径
                    filename=r'.\test.log'
                    )

logging.debug('我是一个debug')
logging.info('我是一个info')
logging.warning('我是一个warning')
logging.error('我是一个error')
logging.critical('我是一个critical')