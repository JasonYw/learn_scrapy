# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Ep8Item(scrapy.Item):
    #大标题名字 用来创建文件夹
    TITLE =scrapy.Field()

    #小标题名字  用来创建文件夹
    title_title =scrapy.Field()

    #小标题链接，用来向下爬虫
    title_link =scrapy.Field()

    #文章题目，用来当文件名
    topic_topic =scrapy.Field()

    #文章链接，用来爬取内容
    topic_link =scrapy.Field()

    #文章内容
    text =scrapy.Field()

  