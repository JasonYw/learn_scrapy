# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Ep2Item(scrapy.Item):
    
    title =scrapy.Field()
    number =scrapy.Field()
    public_data =scrapy.Field()
    state =scrapy.Field()
    deal_data =scrapy.Field()
    text =scrapy.Field()
    url =scrapy.Field()
