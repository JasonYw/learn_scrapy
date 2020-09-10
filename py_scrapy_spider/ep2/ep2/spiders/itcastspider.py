import scrapy
from ep2.items import ITcastItem
#http://www.itcast.cn/channel/teacher.shtml#aandroid



'''
teacher_list =response.xpath('//div[@class="li_txt"]') 
for each in teacher_list:                      #根,迭代
    each.xpath('./h3/text()')  #名字
    each.xpath('./h4/text()')  #职位
    each.xpath('/p/text()')    # 简介
'''
#常见一个爬虫类
class ItcastSpider(scrapy.Spider):
    name ='itcast' #爬虫名
    allowd_domains =['http://www.itcast.cn/']#允许爬虫作用的范围
    start_urls =['http://www.itcast.cn/channel/teacher.shtml#'] #爬虫起始url


    def parse(self,response):
        #with open('teacher.html','wb') as f:
        #    f.write(response.body)
        # 通过scrapy自带的xpath匹配出老师自带的根节点
        #/home/rico/Desktop/py/py_Scrapy/ep2/ep2/spiders
        teacher_list =response.xpath('//div[@class="li_txt"]') 
        #所有老师信息集合
        #teacher_item=[]
        for each in teacher_list:                      #根,迭代 遍历根节点列表集合

            #实例化对象，存储对象，用来保存数据
            item =ITcastItem()

            #name =each.xpath('./h3/text()').extract()[0].encode('gbk') #名字   extract()   把返回的对象转化为unicode字符串
            #title =each.xpath('./h4/text()').extract()[0].encode('gbk')  #职位
            #info =each.xpath('./p/text()').extract()[0].encode('gbk')  # 简介
            name =each.xpath('./h3/text()').extract()[0] #名字   extract()   把返回的对象转化为unicode字符串
            title =each.xpath('./h4/text()').extract()[0] #职位
            info =each.xpath('./p/text()').extract()[0]  # 简介




            item['name'] =name
            item['title'] =title
            item['info'] =info
            #teacher_item.append(item)
            yield item


