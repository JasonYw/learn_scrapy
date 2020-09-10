# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Ep3Item(scrapy.Item):
    # define the fields for your item here like:
    postionName = scrapy.Field() #职位名称
    postionWork =scrapy.Field() #工作地点
    postionTime =scrapy.Field() #工作时间
    postionText =scrapy.Field()  #职位简
    postionLink =scrapy.Field()  #类别
     

