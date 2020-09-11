# -*- coding: utf-8 -*-
import scrapy
from ep0 import settings


class DbLoginSpider(scrapy.Spider):
    name = 'db_login'
    allowed_domains = ['www.douban.com']
    start_urls = ['https://www.douban.com/']
    
  

    def parse(self,response):
        self.headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36',
        }
        cookies =response.headers.getlist('Set-Cookie')
        cookie =','.join(i.decode('utf-8') for i in cookies)
        # print('cookie =%s'%(cookie))
        self.headers['Cookie'] =cookie
        print('headers: ',self.headers)
        data ={'name':'15801367721','password':'forstudy','remember': 'false','ck':''}
        yield scrapy.FormRequest(
            url ='https://accounts.douban.com/j/mobile/login/basic',
            headers =self.headers,
            formdata =data,
            callback =self.parse_page,
            dont_filter =True,
        )
        # yield scrapy.FormRequest.from_response(
        #     response,
        #     method='POST',
        #     headers =self.headers,
        #     formdata =data,
        #     callback =self.parse_page,
        #     dont_filter =True,
        # )

        
    def parse_page(self,response):
        cookies =response.headers.getlist('Set-Cookie')
        print("cookie = ",cookies)
        # print(response.body)
        self.headers['Cookie'] =','.join(i.decode('utf-8') for i in cookies)
        print('headers: ',self.headers)
        yield scrapy.Request('https://www.douban.com/',headers=self.headers,callback=self.parse_loginpage)

    def parse_loginpage(self,response):
        pass
       
    