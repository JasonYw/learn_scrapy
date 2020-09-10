# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import json
import pymongo
from scrapy.utils.project import get_project_settings
class Ep7Pipeline(object):
    def __init__(self):
        settings = get_project_settings()

        #主机名
        host =settings['MONGODB_HOST']
      
        #端口号
        port =settings['MONGODB_PORT'] 

        #数据库名称
        dbname =settings['MONGODB_NAME'] 

        #数据表名称
        sheetname =settings['MONGODB_SHEETNAME']
        
        #创建mongodb数据库连接
        client =pymongo.MongoClient(host =host,port=port)  
        
        #指定数据库
        mydb =client[dbname]

        #指定存放数据库表明
        #mysheet =mydb[sheetname]
        self.post =mydb[sheetname]
        self.filename =open('db_250.json','w',encoding='utf-8')



    def process_item(self, item, spider):
        data =dict(item)  
        page =json.dumps(dict(item),ensure_ascii=False)+'\n'
        self.filename.write(page)
        
        #把数据插入到数据库
        #self.post.insert(data)

        return item

      









'''
class Ep7Pipeline(object):
    def __init__(self):
        self.filename =open('db_250.json','w')
        
    def process_item(self, item, spider):
        page =json.dumps(dict(item),ensure_ascii=False)+'\n'
        self.filename.write(page)
        return item
'''