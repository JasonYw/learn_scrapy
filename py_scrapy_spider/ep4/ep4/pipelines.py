# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
'''
def get_media_requests(self, item, info):
        return [Request(x) for x in item.get(self.images_urls_field, [])]

    def item_completed(self, results, item, info):
        if isinstance(item, dict) or self.images_result_field in item.fields:
            item[self.images_result_field] = [x for ok, x in results if ok]
        return item
    '''
#获取项目setting文件
from scrapy.utils.project import get_project_settings  

#专门处理下载文件
from scrapy.pipelines.images import ImagesPipeline

import os
import scrapy



class Ep4Pipeline(ImagesPipeline):
    #def process_item(self, item, spider):
    #    return item  
    #获取settings文件里设置的变量值
    IMAGES_STORE =get_project_settings().get('IMAGES_STORE')

    
    #获取图片链接，发送requests请求，之后让item_completed类做处理
    def get_media_requests(self,item,info):
    
        image_url =item['cover_img']
    
        yield(scrapy.Request(image_url))
  

    def item_completed(self,results,item,info):


        image_path =[x['path'] for ok, x in results if ok]
        os.rename(self.IMAGES_STORE+"/"+image_path[0],self.IMAGES_STORE+"/"+str(item["uid"])+".jpg")
        
        item["imagePath"] =self.IMAGES_STORE+"/full/"+str(item['uid'])

        return item
    
    def close_spider(self):
        path =self.IMAGES_STORE+'/full'
        if os.path.exists(path):
            os.rmdir(path)
