# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Ep1Item(scrapy.Item):
    title =scrapy.Field()
    num =scrapy.Field()
    price =scrapy.Field()
    text =scrapy.Field()
    link =scrapy.Field()