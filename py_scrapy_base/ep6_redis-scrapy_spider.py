from scrapy_redis.spiders import RedisSpider


class MySpider(RedisSpider):
    """Spider that reads urls from redis queue (myspider:start_urls)."""
    name = 'myspider_redis'

    #启动所有端爬虫的指令，不固定，默认为  爬虫类的名字：starturls  此格式为参考格式    l
    #lpush指令：往信息库里push信息 lpush redis_key start_urls  第一个url只有一个爬虫爬取  ---在master端发送这个指令
    redis_key = 'myspider:start_urls'

    #等效于allow_domains=["dmoz.org"]--指定获取域的范围
    #__init__的方法 是都动态获取请求域的范围，若要使用只需要改super里的子类的名字。改成自己的，也可以用指定的
    def __init__(self, *args, **kwargs):
        # Dynamically define the allowed domains list.
        domain = kwargs.pop('domain', '')
        self.allowed_domains = filter(None, domain.split(','))
        super(MySpider, self).__init__(*args, **kwargs)

    def parse(self, response):
        return {
            'name': response.css('title::text').extract_first(),
            'url': response.url,
        }


    #若父类为redisspider 则启动爬虫是scrapy runspider 文件名.py  
    #启动本爬虫 则是 scrapy runspider myspider_redis.py