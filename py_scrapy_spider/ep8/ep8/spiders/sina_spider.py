# -*- coding: utf-8 -*-
import scrapy
import os
#import time
from ep8.items import Ep8Item
import re 

def make_file(filename):
    if not os.path.exists(filename):
        os.mkdir(filename)   

class SinaSpiderSpider(scrapy.Spider):
    name = 'sina_spider'
    allowed_domains = ['www.sina.com']
    start_urls = ['http://news.sina.com.cn/guide/']
    
    file_locat ='D://py/py_scrapy_spider/ep8/sina_spy'
    i=0
    title_titlepath=[]
    title_link=[]
    
    make_file(file_locat)
    def parse(self,response):

        #大标题的标题
        TITLE =response.xpath('//h3/a/text()').extract()[0:19]

        #小标题
        title_title_gen =response.xpath('//div[@id="tab01"]/div[@class="clearfix"]')[0:19]
        
        #小标题的link
        self.title_link =response.xpath('//div[@class="section"]//ul[@class="list01"]/li/a/@href').extract()[0:273]
        
    

        #创建大标题文件夹
        for filename in TITLE:
            filename =self.file_locat + '/' +str(filename)
           
            make_file(filename)



        #创建小标题文件夹
        self.i=0
        
        for title_title in title_title_gen:
            for filename in title_title.xpath('.//ul[@class="list01"]//a/text()').extract():
        
                filename = self.file_locat + '/' +TITLE[self.i] + '/' + str(filename)
                self.title_titlepath.append(filename)
                make_file(filename)
                self.title_titlepath.append(filename)
            self.i =self.i+1
        
        #item =Ep8Item()
        #item['title_link'] =self.title_link
        #item['title_title'] =self.title_titlepath
        #yield item
        temp_li=[]
        for i in self.title_titlepath:
            if not i in temp_li:
                temp_li.append(i)

        self.title_titlepath = temp_li
        #print(len(self.title_titlepath))
        #print(len(self.title_link))
        
        #通过小标题链接得到页面信息
        for topic in self.title_link:
           yield scrapy.Request(topic,callback=self.parse_topic,dont_filter=True)
        

    def parse_topic(self,response):
        
        topic_link= re.findall(r'https://\D+\Dsina\Dcom\Dcn/\D+/\d\d\d\d-\d\d-\d\d/\D+-\D+\d+\Dshtml+',str(response.xpath('//@href').extract()))
        #print(topic_link)
    
        for filename in topic_link:
            yield scrapy.Request(filename,callback=self.parse_text,dont_filter=True)
            
        


    def parse_text(self,response):
        item =Ep8Item()
        #拿到标题
        text_topic =response.xpath('//h1[@class="main-title"]/text()').extract()

        #拿到正文
        text_text =response.xpath('//div[@id="article"]/p/text()').extract()
        

       
        item['topic_topic'] =text_topic  #标题

        item['topic_link']=response.url #文章url
        
        i=0
        for path in self.title_link:
            if str(path) in  str(response.url).replace('https:','http:'):
                filename =self.title_titlepath[i]+'/'+str(item['topic_link']).strip()[-10:]+'.txt'
                with open(filename,'wb') as f:
                    f.write(str(response.text).encode('utf-8'))
                print(filename)
                break
            else:
                #print('no')
                i=i+1
        
        

        
