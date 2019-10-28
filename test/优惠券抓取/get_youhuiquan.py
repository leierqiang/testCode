#!/usr/bin/env python
# encoding: utf-8

'''
@author: Leq
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: leierqiang123@gmail.com
@software: Pycharm
@file: get_youhuiquan.py.py
@time: 2019/8/29 0029 上午 8:35
@desc:
'''

from selenium import webdriver
import datetime
import time

options = webdriver.ChromeOptions()
options.add_argument('--log-level=3')

# 创建浏览器对象
driver = webdriver.Chrome(chrome_options=options)
# 窗口最大化显示
driver.maximize_window()

url = "https://pro.jd.com/mall/active/u6gHEpQdnEZuJPf8ebCQqdJCs2V/index.html?jd_pop=c0123941-4a86-4dbd-8f86-1cd540cd261d&utm_source=chongzhi.jd.com&utm_medium=zssc&utm_campaign=t_0_&utm_term=c0123941-4a86-4dbd-8f86-1cd540cd261d-p_93455"
driver.get(url)
driver.implicitly_wait(10)
time.sleep(2)

# 找到并点击京东的登陆按钮
driver.find_element_by_link_text("你好，请登录").click()

print("请在30秒内完成登录")
# 用户扫码登陆
time.sleep(10)

# "立即领取40元优惠券"的css_selector
btn_buy = "[data-cpid='6F3BD5C7006031740B25BCBCF11343FC_babel']"
#“关闭按钮”的css_selector
btn_close = ".close-button"
#抢购时间，尽量设置的靠前一点，比如提前1分钟，如10：00开奖，那就设置为09：59
time = "2019-08-29 09:59:00"

a = 0
while True:
    print("领取还未开始")
    if datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') > buy_time:
        print("即将开始领取")
        # 找到“立即领取”，点击
        time.sleep(0.2)
        if driver.find_element_by_css_selector(btn_buy):
            while True:
                driver.find_element_by_css_selector(btn_buy).click()
                time.sleep(0.2)
                try:
                    if driver.find_element_by_css_selector(btn_close):
                        time.sleep(0.2)
                        driver.find_element_by_css_selector(btn_close).click()
                    time.sleep(0.2)
                except:
                    print("抢券成功")
                    a=1
                    break
            if a == 1:
                break

    time.sleep(0.5)
