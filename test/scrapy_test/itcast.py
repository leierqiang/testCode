# -*- coding: utf-8 -*-
import scrapy


class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['http://www.itcast.cn/channel/teacher.shtml#ajavaee']
    start_urls = ['http://http://www.itcast.cn/channel/teacher.shtml#ajavaee/']

    def parse(self, response):
        pass
