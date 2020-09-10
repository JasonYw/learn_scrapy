import scrapy 


#正统模拟登录案例，跟据respnse响应文件登录
#首先发送登录页面get请求，获取到页面里的登录必须参数，比如知乎的_xsrf
#然后和账户密码一起post到服务器，登陆成功，get请求，获取页面的登录所需参数

class RenrenSpider(scrapy.Spider):
    name="renren"
    allowed_domains=["renren.com"]
    start_urls =('http://www.renren.com/PLogin.do',)



    #先get到页面
    def parse(self,response):  
        _xsrf =response.xpath().extartct()  #取出想要的数据，比如取xsrf
        yield scrapy.FormRequest.from_response(
            response,
            formdata ={"email":"xxxxxxxxx","password":"xxxxxxxxxxx","_xsrf"=_xsrf},
            callback= self.parse_page
        )


    def parse_page(self,response):
        pass