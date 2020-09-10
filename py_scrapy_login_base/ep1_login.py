import scrapy 


#只需要提供post数据的，只要是需要提供post数据的就可以用这种方法做，这种方法适用于只需要账户密码的登陆方式
#下面示例只需要提供账户密码，重写start_request()，若重写start.request() 就不能有start_url

class RenrenSpider(scrapy.Spider):
    name="renren"
    allowed_domains=["renren.com"]

    def start_requests(self):
        url ='http://www.renren.com/PLogin.do'
        yield scrapy.FormRequest(
            url =url,
            formdata ={"email":"xxxxxxxxx","password":"xxxxxxxxxxx"}
            callback= self.parse_page
        )

    def parse_page(self,response):
        pass