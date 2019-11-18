# -*- coding: utf-8 -*-
import scrapy


class SecondSpiderSpider(scrapy.Spider):
    name = 'second_spider'
    allowed_domains = ['renren.com']
    start_urls = ['http://renren.com/']

    def parse(self, response):
        pass
