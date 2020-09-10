# -*- coding: utf-8 -*-
import json
import time
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class Ep3Pipeline(object):
    def __init__(self):
        file =str(time.time())+'tencent.json'
        self.filename =open(file,'w')


    # #必须有process_item()方法，方法内必须有return item
    def process_item(self, item, spider): 
        text =json.dumps(dict(item),ensure_ascii=False)+'\n'
        self.filename.write(text)

        #return item  必须有
        return item 


    def close_spider(self,spider):
        self.filename.close()
