# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import json

class Ep5Pipeline(object):
    def __init__(self):
        self.filename =open('imoocdata.json','w')
        
    def process_item(self, item, spider):
        imoocdata =json.dumps(dict(item),ensure_ascii=False)+'\n'
        self.filename.write(imoocdata)
        return item

    def process_close(self,spider):
        self.filename.close()