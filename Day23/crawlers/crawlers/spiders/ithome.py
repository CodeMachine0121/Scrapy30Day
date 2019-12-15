# -*- coding: utf-8 -*-
import scrapy


class IthomeSpider(scrapy.Spider):
    name = 'ithome'
    allowed_domains = ['ithome.com']
    start_urls = ['http://ithome.com/']

    def parse(self, response):
        pass
