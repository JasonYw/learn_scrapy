# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


import json
import codecs

class Ep6Pipeline(object):
    def __init__(self):
        self.filename =codecs.open('dg_complain.json','w',encoding='utf-8')

    def process_item(self, item, spider):
        page =json.dumps(dict(item),ensure_ascii=False)+'\n'
        self.filename.write(page)
        return item

    def process_close(self):
        self.filename.close()