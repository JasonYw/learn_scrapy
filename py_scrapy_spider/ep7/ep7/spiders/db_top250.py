# -*- coding: utf-8 -*-
import scrapy
from ep7.items import Ep7Item


class DbTop250Spider(scrapy.Spider):
    name = 'db_top250'
    allowed_domains = ['movie.douban.com']
    offset =0
    start_urls = ['https://movie.douban.com/top250?start=0&filter=']

    def parse(self, response):
        
        dot_list =response.xpath('//div[@class="item"]')
        for each in dot_list:
            item =Ep7Item()
            item['title'] =each.xpath('.//span[@class="title"][1]/text()')[0].extract().strip()
            item['rating_num'] =each.xpath('.//span[@class="rating_num"]/text()')[0].extract().strip()
            item['people_num'] =each.xpath('.//span[4]/text()')[0].extract().strip()
            if len(each.xpath('.//p/span[contains(@class,"inq")]/text()').extract()) !=0:
                item['command'] =each.xpath('.//p/span[contains(@class,"inq")]/text()')[0].extract().strip()
            else:
                item['command'] =None
            item['text'] =str(each.xpath('.//div[@class="bd"]/p[1]')[0].extract()).replace(' ','').replace('/','').replace('<br>','').replace('</p>','').replace('<pclass="">','').strip().replace('\xa0','').replace('\n','').replace('<p>','')
        
            yield item
        
        
        if self.offset<12:
            self.offset+=1
            yield(scrapy.Request('https://movie.douban.com/top250?start='+str(self.offset*25)+'&filter=',callback=self.parse))
        else:
            pass
        
    


        '''
            item['contury'] =text[-15:-10]
            item['kind'] =text[-13:]
            item['actor'] =re.findall(r'主演: [\u4e00-\u9fa5]+.[\u4e00-\u9fa5]+',text)
            item['dirctor'] =re.findall(r'导演: [\u4e00-\u9fa5]+.[\u4e00-\u9fa5]+',text)
            item['year'] =re.findall(r'\d+',text)
        '''