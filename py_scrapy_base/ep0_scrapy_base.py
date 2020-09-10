'''
    scrapy引擎，调度器，下载器，保存数组
    处理数据，爬虫需要自己写。
    爬虫发请求，请求给引擎，引擎给调度器，调度器把请求给下载器，之后得到响应给爬虫，响应如果是数据就给管道保存，
    如果是请求在给调度器。
    当调度器中不存在requests程序才会停止
    '''


    #第一步新建爬虫项目
    #scrapy startproject xxx  新建一个新的爬虫项目
    #明确目标，编写items.py
    #制作爬虫(spiders/xxspider.py):制作爬虫开始爬取网页
    #存储内容(pipelines.py)  设计管道爬取内容

    #scrapy.cfg  项目设置 settings文件，必须有，不能丢
    #__init__.py  不要删除，必须有不能写
    #items用来存储数据



    #scrapy genspider example example.com 
    #scrapy crawl  爬虫的名字     #爬虫的名字是在spiders文件夹里的使用scrapy genspider命令创建的 py文件的第一个类的name值 也是爬虫的名字
    #scrapy crawl  爬虫名字-o i文件 #将输出保存指定文件
    # yield  数据就会给管道  yield item    

    #使用管道文件，先设置好setting文件里的类
    #之后在pipelines定义类并写process_item方法
    #在spider文件里数据要用yield，yield会把数据会给pipelines文件，不能写return

'''
1.创建项目  scrapy startproject xxx
2.编写items.py文件 设置需要保存的数据字段
3.进入xxx/spiders  编写爬虫文件，文件里的name就是爬虫名
4.运行 scrapy crawl itcast   scrapy crawl -o json/csv/xml/


spider里面的start_urls只执行一次，parse方法用来处理，数据给管道 url给调度器，给下载器，再给parse，直到没有请求为止yield item把数据给管道，请求是给scrapy.request
每个url都有独一无二的指纹，请求进入队列前先做重复判断，分布式的话可以把请求队列存到数据库里，这样可以不重复的request的url
scrapy item spider pipelines setting
xpath 返回的是一个选择器对象，extract()返回的是对象下的值的列表

保存数据
scrapy crawl itcast -o xxxx.json
csv也可以
xml也可以

yield有两个数据 返回数据，并标记暂停
response.xpath（）
response.css()  === bs
解析用response.text 打印用body
pipeline 要return item
json.dumps() 若json文件中有中文，请ensure_ascii=False


CrawlSpiders  --一个新的类
scrapy genspider -t crawl xxx xxxx.com
CrawlSpidres 类里面 多了 LinkExtractor 和 rules
要导入from scrapy.spiders imports CrawlSpider 和 Rule
from scrapy.linkextractors import LinkExtractor

spider类做处理的时候，手动处理url
crawlspiders是自动处理url，不需要yeild requests 会从规则里面调用，不能写parse方法，要手动写解析方法
LinkExtractor 匹配链接
首先找到要匹配的东西


LinkExtractor 用法 ----- 提取链接
from scrapy.linkextractors import LinkExtractor
link_list =LinkExtractor(allow=("start=\d+"))   按照正则的规则 匹配respons里面所有的start数子，返回一个对象   allow符合规则拿下来 
link_list.extract_links(response)



rules是一个参数，可包含一个或多个 Rule对象，link_list就是Rule对象
CrawlSpider 必要回调时指向parse方法
follow为深度爬虫，从链接里提取链接。

link_extractor callbac  follow 为 Rule的参数

每个LinkExtractor都有一个公共方法 extract_links()
allow()  括号内为正则表达式，满足正则表达式会被提取，为空就全部匹配，无意义
deny() 不符合括号内的全部提取。
allowd_domains  会被提起链接的domains
deny_domains 一定不会被提取链接的domains
restrict_xpaths 作用与allow一样 但是用xpath
