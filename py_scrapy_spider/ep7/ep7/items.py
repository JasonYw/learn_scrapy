# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Ep7Item(scrapy.Item):
    title =scrapy.Field()
    rating_num =scrapy.Field()
    people_num =scrapy.Field()
    command =scrapy.Field()
    '''
    contury =scrapy.Field()
    kind =scrapy.Field()
    actor =scrapy.Field()
    dirctor =scrapy.Field()
    year =scrapy.Field()
    '''
    text =scrapy.Field()