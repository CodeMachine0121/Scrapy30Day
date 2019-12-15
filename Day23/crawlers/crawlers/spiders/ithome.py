# -*- coding: utf-8 -*-
import scrapy


class IthomeSpider(scrapy.Spider):
    name = 'ithome'
    allowed_domains = ['ithome.com']
    start_urls = ['https://ithelp.ithome.com.tw/articles?tab=tech']

    def parse(self, response):
        with open('ithom.html','wb') as f:
            f.write(response.body)
