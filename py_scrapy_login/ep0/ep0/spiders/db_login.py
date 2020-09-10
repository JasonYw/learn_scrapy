# -*- coding: utf-8 -*-
import scrapy


class DbLoginSpider(scrapy.Spider):
    name = 'db_login'
    allowed_domains = ['www.douban.com']
    #start_urls = ['https://www.douban.com/']
    start_urls=['https://accounts.douban.com/passport/login']
    data ={'username':'15801367721','password':'forstudy'}



    def parse(self,response):
        return scrapy.FormRequest(
            url='https://accounts.douban.com/j/mobile/login/basic',
            method='post',
            formdata=self.data,
            #meta={'cookiejar':response.meta['cookiejar']},
            # 如果需要多次提交表单，且url一样，那么就必须加此参数dont_filter，防止被当成重复网页过滤掉了
            dont_filter=True,
            callback=self.parse_page
        )


    def parse_page(self,response):
        
        print(response.xpath('//div[@class="stream-items"]//div[@class="text"]/a/text()').extract())
        #print(response.xpath('//iframe/@src').extract())
        #print(response.xpath('//div[@class="account-form-3rd-hd"]/text()').extract())
        #print(response.xpath('//iframe[@id="tcaptcha_popup"]/@src').extract())
        print('----------------------------')
        print(response.text)



    '''
    def start_requests(self):
        cookie ={
            'll':"108288",
            'bid':'MMMOR2TiEAA', 
            '__utmc':'30149280',
            '__utmz':'30149280.1584884369.1.1.utmcsr',
            'ap_v':'0,6.0', 
            '__gads':'ID=5d1d3bbea7bde805:T=1584885319:S=ALNI_MZTbpwGKh41Tupy71MEQNUlQgSkIA',
            '__yadk_uid':'Te2nsCVco1gJYekUNQVbuEO3OIeXRP5w',
            'push_noty_num':'0',
            'push_doumail_num':'0',
            '__utmv':'30149280.21411',
            'ps':'y', 
            '_pk_ref.100001.8cb4':'%5B%22%22%2C%22%22%2C1584892172%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3Dz9TeZBU9CdAEFfKV-N044Wb2hbie3iCPt57X47cdPUcWQr-F2fYD2mdJ_TcYcr6K%26wd%3D%26eqid%3Ddafba14300084605000000025e776a87%22%5D; _pk_ses.100001.8cb4=*', 
            '__utma':'30149280.1074766758.1584884369.1584884369.1584892172.2',
            '__utmt':'1',
            '_pk_id.100001.8cb4':'214a52194602e6a4.1584884367.2.1584893858.1584889523.',
            '_pk_ses.100001.8cb4':'*',
            'dbcl2':'"214112718:KpvvYkq0iJE"', 
            'ck':'nfn2',
            '__utmb':'30149280.16.10.1584892172'
        }
        urls ='https://www.douban.com/'
        yield scrapy.Request(urls,callback=self.parse,cookies=cookie)
        


    def parse(self,response):
        print(response.text)
        print(response.xpath('//div[@class="stream-items"]//div[@class="text"]/a/text()').extract())
    '''



    '''
    def parse(self,response):
        print('ttttttttttttttttttttttttttttttttttttttttttttttttttttttttt')
        password =response.xpath('//div[@class="account-form-field"]/input[@tabindex="3"]/@id').extract()
        username =response.xpath('//div[@class="account-form-field"]/input[@tabindex="1"]/@id').extract()
        data ={'username':'15801367721','password':'forstudy'}

        yield scrapy.FormRequest.from_response(
            response,
            method = 'POST',
            formdata =data,
            callback=self.parse_page
        )
        print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')

    def parse_page(self,response):
        
        print(response.xpath('//div[@class="stream-items"]//div[@class="text"]/a/text()').extract())
        #print(response.xpath('//iframe/@src').extract())
        #print(response.xpath('//div[@class="account-form-3rd-hd"]/text()').extract())
        #print(response.xpath('//iframe[@id="tcaptcha_popup"]/@src').extract())
        print('----------------------------')
        #print(response.text)

    '''
    '''
    def start_requests(self):
        url ='https://accounts.douban.com/j/mobile/login/basic HTTP/1.1'
        print('yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy')
        yield scrapy.FormRequest(
            url =url,
            formdata ={
                                'name':'15801367721',
                                'password':'forstudy',
                                'remember':'false',
                        
                            },
            callback=self.parse
        )
        print('lllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllll')

    def parse(self,response):
        print(response.xpath('//div[@class="stream-items"]//div[@class="text"]/a/text()').extract())
        print(response.xpath('//iframe/@src').extract())
        print(response.xpath('//div[@class="account-form-3rd-hd"]/text()').extract())
        print(response.xpath('//iframe[@id="tcaptcha_popup"]/@src').extract())
        print('----------------------------')
        #print(response.text)

    '''