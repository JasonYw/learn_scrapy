'''
对于爬取普通网站，不需要验证码，不需要登入的界面，我们一般用scrapy.Request类直接去爬取信息就行，下面是Request类的定义：


class Request(object_ref):

    def __init__(self, url, callback=None, method='GET', headers=None, body=None,
                 cookies=None, meta=None, encoding='utf-8', priority=0,
                 dont_filter=False, errback=None, flags=None):
                 # url是要爬取的网址
                 # callback是回调函数
                 # method是请求的方式post还是get
                 # headers是浏览器伪装的头信息
                 # body是网页源代码信息
                 # cookies是登入某网站后，网站在你电脑上保留的信息
                 # meta要携带或者传递的信息
                 # encoding是编码方式
                 # priority用来设置访问网站的优先级
                 # dont_filter是否允许重复爬取网站

可以看见，其中url，即要爬取的目标网站是必填的，其他的是选填的，method=‘GET’，说明此类是get请求，实例化该对象后，会得到一个response。


例子：
def start_requests(self):
        # 首先爬一次登陆页，看是否有验证码。回调函数为parse()，'cookiejar'的值为1表示开启状态
        # 这里要返回一个可迭代对象，用yield本身就是可迭代对象，但是，这里是return，所以用[]将其构造成一个可迭代对象
        return [Request("https://accounts.douban.com/passport/login", meta={'cookiejar': 1}, headers=self.header, callback=self.parse)]




二、scrapy.FormRequest与scrapy.http.FormRequest


（1）普通请求使用scrapy.Request类就可以实现，但是遇到模拟表单或Ajax提交post请求的时候，Request类就不如 子类 FormRequest类方便了，因为他自带 formdata ，专门用来设置表单字段数据，即填写账号、密码，实现登入，默认method也是POST。
（2）FormRequest相当于是手动指定post。
（3）事实上，scrapy.FormRequest()与scrapy.http.FormRequest()使用起来的区别不大，你可以将两种方法等价互换。



例子
def start_requests(self):
    form_data = {'f1':'1', 'f2':'100'}  # 表单数据，字典格式，注意数字也要用引号引起来，否则报错。
    yield scrapy.FormRequest(url, formdata=form_data) # 还可以通过callback修改回调函数等 也可以


def start_requests(self):
    form_data = {'f1':'1', 'f2':'100'}  # 表单数据，字典格式，注意数字也要用引号引起来，否则报错。
    yield scrapy.http.FormRequest(url, formdata=form_data) # 还可以通过callback修改回调函数等


三、FormRequest.from_response()
（1）FormRequest.from_response也可以进行设置 formdata，用来填写并提交表单，实现模拟登入。
（2）FormRequest.from_response相当于是自动识别post。
（3）FormRequest.from_response与FormRequest.http.from_response也没有区别。


def parse(self, response):
        return scrapy.FormRequest.from_response(
            response,
            formdata={'username': 'john', 'password': 'secret'},
            callback=self.after_login
        )


！！！！！！！！三、scrapy.FormRequest与FormRequest.from_response 的区别##
1.什么情况下分别使用什么

先找到填写表单时发送的post请求的地址，下面以豆瓣登入为例子：
可以看见其post的地址为：https://accounts.douban.com/j/mobile/login/basic
然后用浏览器访问https://accounts.douban.com/j/mobile/login/basic
发现页面没有表单信息（也就是没有填写账号、密码的地方），所以，我们只能采用scrapy.FormRequest，手动的去发送post请求。
如果浏览器访问某post网址时，里面有表单信息，这时候你可以用FormRequest.from_response也可以用scrapy.FormRequest实现模拟登入


scrapy.FormRequest的必填参数是目标网址，而FormRequest.from_response的必填参数是response