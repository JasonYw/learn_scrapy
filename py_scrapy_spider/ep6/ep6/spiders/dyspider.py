# -*- coding: utf-8 -*-
import scrapy
from ep6.items import Ep6Item
import re

class DyspiderSpider(scrapy.Spider):
    name = 'dyspider'
    allowed_domains = ['wz.sun0769.com']
    offset_page =1  #13603
    start ='http://wz.sun0769.com/political/index/politicsNewest?id=1&page='
    start_urls =[start+str(offset_page)]
    page_start='http://wz.sun0769.com'


    def parse(self, response): #response  是页的请求内容 
       #page_num =len(response.xpath('//li[@class="clear"]//a/text()'))
        for page in re.findall('.political.politics.index.id.\d+',response.text):
            yield scrapy.Request(self.page_start+page,callback=self.parse_item)
        if self.offset_page <13604:
            self.offset_page +=1
            yield scrapy.Request(self.start+str(self.offset_page),callback=self.parse)
        else:
            pass


    def parse_item(self,response): #response是每一个具体项的请求内容 两个response不一样！！！！！
        item =Ep6Item() 

        item['title'] =response.xpath('//div[@class="mr-three"]/p/text()').extract()
        item['number'] =response.xpath('//div[@class="mr-three"]//span[@class="fl"][3]/text()').extract()
        item['public_data'] =response.xpath('//div[@class="mr-three"]//span[@class="fl"][1]/text()').extract()
        item['state'] =re.findall('\w\w\w',str(response.xpath('//div[@class="mr-three"]//span[@class="fl"][2]/text()').extract()))
        item['deal_data'] =response.xpath('//div[@class="mr-three"]//div[@class="skillbar-title"]/span/text()').extract()
        item['text'] =str(response.xpath('//div[@class="mr-three"]//pre/text()').extract()).replace('\r','').replace('\n','').replace('\\','').strip().replace('r','').replace('n','')
        item['url'] =response.url

        yield item

    
