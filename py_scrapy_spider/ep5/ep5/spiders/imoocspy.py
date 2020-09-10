# -*- coding: utf-8 -*-
import scrapy
from ep5.items import Ep5Item


class ImoocspySpider(scrapy.Spider):
    name = 'imoocspy'
    allowed_domains = ['www.imooc.com']
    urls ='http://www.imooc.com/course/list?page='
    offset =1
    start_urls = [urls+str(offset)]
    
    def parse(self, response):
        for each in response.xpath('//div[@class="clearfix"]/div[@class="course-card-container"]'):
            items =Ep5Item()

            items['title'] =each.xpath('.//h3/text()').extract()[0]
            items['num'] =each.xpath('.//div[@class="course-card-info"]/span[2]/text()').extract()[0]
            items['price'] =each.xpath('.//span[starts-with(@class,"price")]/text()').extract()[0]
            items['text'] =each.xpath('.//p/text()').extract()[0]

            yield items

        if self.offset>30:
            pass
        else:
            self.offset +=1
            yield scrapy.Request(self.urls+str(self.offset),callback=self.parse)