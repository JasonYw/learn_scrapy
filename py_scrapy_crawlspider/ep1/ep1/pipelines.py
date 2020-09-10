# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json

class Ep1Pipeline(object):

    def __init__(self):
        self.filename =open('imooc.json','w')

    def process_item(self, item, spider):
        page =json.dumps(dict(item),ensure_ascii=False)+'\n'
        self.filename.write(page)
        return(item)
'''
    def  close_spider(self,spider):
        self.filename.close()
'''