# -*- coding: utf-8 -*-
import scrapy


class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['itcast.cn'] #允许爬的范围
    # start_urls = ['http://itcast.cn/'] #最开始请求的url
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml#ajavaee'] #最开始请求的url

    def parse(self, response):
        # 这里写start_url对应的响应
        res = response.xpath("/html/body/div[1]/div[5]/div/div[2]/div[1]")
        print(res)