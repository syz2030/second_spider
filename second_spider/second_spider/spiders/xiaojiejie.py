# -*- coding: utf-8 -*-
import scrapy


class XiaojiejieSpider(scrapy.Spider):
    name = 'xiaojiejie'
    allowed_domains = ['renren.com']
    start_urls = ['http://renren.com/']

    def parse(self, response):
        pass
