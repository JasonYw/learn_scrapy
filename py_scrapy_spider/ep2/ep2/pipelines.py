# -*- coding: utf-8 -*-
import json
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html



class ItcastPipeline(object):
    #__init__方法是可选的
    def __init__(self): 
        self.filename =open('teacher.json','wb') #创建了一个文件

    #process_item必须有的方法
    def process_item(self,item,spider):    #必须有这个方法，处理数据用的
        jsontext =json.dumps(dict(item),ensure_ascii=False)+'\n'
        self.filename.write(jsontext.encode('utf-8'))
        return item

    #可选的方法，最后执行的方法，结束时调用
    def close_spider(self,spider): #可选方法
        self.filename.close() 

        
