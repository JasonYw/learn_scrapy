# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ep2.items import Ep2Item
import re


class DgspydierSpider(CrawlSpider):
    name = 'dgspydier'
    allowed_domains = ['wz.sun0769.com']
    start_urls = ['http://wz.sun0769.com/political/index/politicsNewest?id=1&page=1']

    rules = (
        #Rule(LinkExtractor(allow=r'politics.index.id=\d+'),process_links ="deal_links"),
        Rule(LinkExtractor(allow=r'politics.index.id=\d+'),callback='parse_item',follow=False),
        Rule(LinkExtractor(allow=r'id=1.page.\d+')),
    )


    #重新处理每个response里提取的链接
    #links就是LinkExtractor提取出来的链接链表
    def deal_links(self,links):
        for link in links:
            print(link.url) #link.url要处理的url
        
        return links #一定要返回

    def parse_item(self, response):
        item =Ep2Item()

        item['title'] =response.xpath('//div[@class="mr-three"]/p/text()').extract()
        item['number'] =response.xpath('//div[@class="mr-three"]//span[@class="fl"][3]/text()').extract()
        item['public_data'] =response.xpath('//div[@class="mr-three"]//span[@class="fl"][1]/text()').extract()
        item['state'] =re.findall('\w\w\w',str(response.xpath('//div[@class="mr-three"]//span[@class="fl"][2]/text()').extract()))
        item['deal_data'] =response.xpath('//div[@class="mr-three"]//div[@class="skillbar-title"]/span/text()').extract()
        item['text'] =str(response.xpath('//div[@class="mr-three"]//pre/text()').extract()).replace('\r','').replace('\n','').replace('\\','').strip().replace('r','').replace('n','')
        item['url'] =response.url

        yield item

    