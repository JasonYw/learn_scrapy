# -*- coding: utf-8 -*-
import scrapy
from ep3.items import Ep3Item
import re
import json



class TecentSpider(scrapy.Spider):
    name = 'tecent'
    allowed_domains = ['careers.tencent.com']
    urls = 'https://careers.tencent.com/tencentcareer/api/post/Query?pageSize=10&pageIndex='
    offset =1
    start_urls =[urls+str(offset)]
    '''
    start_urls =[]
    for i in range(1,460):
        start_urls.append(urls+str(i))
    '''
    

    def parse(self, response):
        text =response.text
        num =json.loads(text)["Data"]["Posts"]
        for each in num:
            item =Ep3Item()
            item['postionName'] =each["RecruitPostName"]                           #职位名称
            item['postionWork'] =each["CountryName"] 
            item['postionTime'] =each["LastUpdateTime"]
            item['postionText'] =each["Responsibility"]                                       #简介
            item['postionLink'] =each["PostURL"]                        #link                   #地点                      #时间

            yield(item)

        if self.offset>459:
            print('done! deal with: ',self.offset)
        else:
            self.offset +=1
            yield(scrapy.Request(self.urls+str(self.offset),callback=self.parse))






        #text_re =text.replace("\n",' ')
        
        '''
        for positionName,positionText,positionLink,postionWork,positionTime in zip(temp['positionName'], temp['positionText'], temp['positionLink'],temp['postionWork'],temp['positionTime']):
            items =Ep3Item()
            items['positionWork'] =positionName
            items['positionLink'] =positionText
            items['positionText'] =positionLink
            items['postionName'] =postionWork
            items['positionTime'] =positionTime
            return(items)
       
  
        num =re.findall(r'"PostURL.+?"."',text_re)
        print(len(num))
        for i in range(0,len(num)):

            items=Ep3Item()
            items['postionName'] =re.findall(r'(RecruitPostName\D\D.+?")',text_re)[i].replace('"','').replace('RecruitPostName:','').strip()      
            items['positionWork'] =re.findall(r'("CountryName.+?".")+',text_re)[i].replace('"','').replace('CountryName:','').replace(',','').strip()
            items['positionTime'] =re.findall(r'(LastUpdateTime\D\D.+?")',text_re)[i].replace('"','').replace('LastUpdateTime:','').strip()
            items['positionText'] =re.findall(r'(Responsibility\D\D.+?")',text_re)[i].replace('"','').replace('Responsibility:','').replace('\\',' ').replace('n','').strip()
            items['positionLink'] =re.findall(r'"PostURL.+?"."',text_re)[i].replace('"','').replace('PostURL:','').replace(',','').strip()
            yield(items)
        
        if self.offset>459:
            print('done! deal with: ',self.offset)
        else:
            self.offset +=1
            yield(scrapy.Request(self.urls+str(self.offset),callback=self.parse))
     




     
         for each in response.xpath('//div[@class="recruit-wrap recruit-margin"]/div/a'):
            item =Ep3Item()  #初始化模型对象,为字典
            
            item['positionName'] =each.xpath('./h4/text()')                                                   #职位名称
            item['positionText'] =each.xpath('./p[@class="recruit-text"]/text()')             #简介
            item['positionLink'] =each.xpath('./p/span[3]/text()')                                        #类别
            item['postionWork'] =each.xpath('./p/span[2]/text()')                                         #地点
            item['positionTime'] =each.xpath('./p/span[4]/text()')                                         #时间
            
        #将数据交给管道文件处理
        yield(item) 

        #自增1，每次处理完一页的数据之后，重新发送下一页的页面请求
        if self.offset >459:
            print('done! deal with: ',self.offset)
        else:
            self.offset =self.offset+1                  
            #将请求重新交给调度器入队列，出对列，交给下载器下载,
            #scrapy.Request第一个参数为url，第二个是回调函数，回调函数指向处理url的方法
            #回调函数就是触发条件，之后交给具体方法去处理，若没有响应文件就不会调用方法
        yield(scrapy.Request(self.urls+str(self.offset),callback=self.parse))
    


        items['postionWork'] =re.findall(r'("CountryName.+?".")+',text_re).replace('"','').replace('CountryName:','').replace(',','').strip()
        items['positionLink'] =re.findall(r'"PostURL.+?"."',text_re).replace('"','').replace('PostURL:','').replace(',','').strip()
        items['positionText'] =re.findall(r'(Responsibility\D\D.+?")',text_re).replace('"','').replace('Responsibility:','').strip()
        items['positionName'] =re.findall(r'(RecruitPostName\D\D.+?")',text_re).replace('"','').replace('RecruitPostName:','').strip()
        items['positionTime'] =re.findall(r'(LastUpdateTime\D\D.+?")',text_re).replace('"','').replace('LastUpdateTime:','').strip()
    
        '''