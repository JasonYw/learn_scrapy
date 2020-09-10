# -*- coding: utf-8 -*-
import scrapy
import json
from ep4.items import Ep4Item


class SpyblibliSpider(scrapy.Spider):
    name = 'spyblibli'
    allowed_domains = ['api.live.bilibili.com']
 
    url_1 ='http://api.live.bilibili.com/room/v3/Area/getRoomList?page='
    #url_1 ='/room/v3/Area/getRoomList?page='
    offset =2
    url_2 ='&actionKey=appkey&appkey=27eb53fc9058f8c3&area_id=0&build=8910&cate_id=0&device=phone&device_name=iPhone%205S&mobi_app=iphone&page_size=20&parent_area_id=0&platform=ios&qn=0&sign=6d0c9ac7d8c490c26bb6935402cc9804&sort_type=online&statistics=%7B%22appId%22%3A1%2C%22version%22%3A%225.48.2%22%2C%22abtest%22%3A%22890%22%2C%22platform%22%3A1%7D&tag_version=1&ts=1584600466'
    start_urls = [url_1+str(offset)+url_2]

    #start_urls =['http://api.live.bilibili.com/room/v3/Area/getRoomList?actionKey=appkey&appkey=27eb53fc9058f8c3&area_id=0&build=8910&cate_id=0&device=phone&device_name=iPhone%205S&mobi_app=iphone&page=1000&&parent_area_id=0&platform=ios&qn=0&sign=b2ee714e93e4d6df2e28eac282a45f39&sort_type=online&statistics=%7B%22appId%22%3A1%2C%22version%22%3A%225.48.2%22%2C%22abtest%22%3A%22890%22%2C%22platform%22%3A1%7D&tag_version=1&ts=1584627391 HTTP/1.1']

    def parse(self, response):
        py_data =json.loads(response.text,encoding='utf-8')["data"]["list"]

        if len(py_data) !=0:
            for each in py_data:
                items =Ep4Item()
                items['uid'] =each['uid']
                #item['up_name'] =each['uname']
                #item['room_name'] =each['title']
                #item['onling_num'] =each['online']
                items['cover_img'] =each['cover']
                yield(items)
            self.offset =self.offset+1
            yield(scrapy.Request(self.url_1+str(self.offset)+self.url_2,callback=self.parse))
        else:
            pass
        