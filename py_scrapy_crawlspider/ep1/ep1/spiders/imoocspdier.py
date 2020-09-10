# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider
from scrapy.spiders import Rule
from ep1.items import Ep1Item 
import re


class ImoocspdierSpider(CrawlSpider):
    name = 'imoocspdier'
    allowed_domains = ['www.imooc.com']
    start_urls = ['http://www.imooc.com/course/list?page=1']   #首先执行，parse里处理这个请求

    #response里链接的提取规则，返回的是符合匹配的规则的链接匹配对象的list
    page_kind=LinkExtractor(allow=r'http://www.imooc.com/course/list?c=\w+')
    pagelink =LinkExtractor(allow=(r'http://www.imooc.com/course/list.page.\d+'))
    titlelink =LinkExtractor(allow=(r'http://www.imooc.com/learn.\d+'))    #sort=0&unlearn=0&page=href="/learn/9"

    rules = (
    #    #符合列表里的链接，以此发送请求，如果继续跟进，调用指定的回调函数处理
        Rule(page_kind,callback='parse_pagekind',follow=True),
        Rule(pagelink, callback="parseimooc", follow = True),
        Rule(titlelink,callback="parseimooc_page",follow=True),   #callback="parseimooc_page"
          
    )
   
    def parse_pagekind(self,response):
        print(response.url)

    def parseimooc(self,response):
        print(response.url)

        for each in response.xpath('//div[@class="clearfix"]/div[@class="course-card-container"]'):
            items =Ep1Item()
            
            items['title'] =each.xpath('.//h3/text()').extract()[0]
            items['num'] =each.xpath('.//div[@class="course-card-info"]/span[2]/text()').extract()[0]
            items['price'] =each.xpath('.//span[starts-with(@class,"price")]/text()').extract()[0]
            items['text'] =str(each.xpath('.//p/text()').extract()[0]).replace('\r','').replace('\n','')
            yield items


    def parseimooc_page(self,response):
        pass
        #print(response.url)
        #print ('-------------------',response.text)
      
