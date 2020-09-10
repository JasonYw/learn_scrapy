import scrapy 


#实在没办法的模拟登录策略案例，

class RenrenSpider(scrapy.Spider):
    name="renren"
    allowed_domains=["renren.com"]
    start_urls =(
        'http://www.renren.com/xxxxxx',
        'http://www.renren.com/x1',
        'http://www.renren.com/xxx',
    )

    cookies ={

    }