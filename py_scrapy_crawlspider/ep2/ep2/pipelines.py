# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json
import codecs  #xxx =codecs.open('xxx.json','w',encoding='utf-8')   codecs.open  可以指定编码格式

class Ep2Pipeline(object):
    def __init__(self):
        self.filename =open('dg_complain.json','w')

    def process_item(self, item, spider):
        page =json.dumps(dict(item),ensure_ascii=False)+'\n'
        self.filename.write(page)
        return item

    def process_close(self):
        self.filename.close()