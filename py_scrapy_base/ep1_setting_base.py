# -*- coding: utf-8 -*-
#程序启动时首先检查settings值

# Scrapy settings for ep1 project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'ep1' #爬虫名字

SPIDER_MODULES = ['ep1.spiders']  #爬虫的位置
NEWSPIDER_MODULE = 'ep1.spiders'  

LOG_FILE ='xxxxxxx.log'   定义日志的名字


LOG_LEVEL='INFO' #显示此等级以下的信息


'''
CRITICAL
ERROR
WARNING
INFO
DEBUG
'''
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'ep1 (+http://www.yourdomain.com)'

# Obey robots.txt rules
#ROBOTSTXT_OBEY = True  #是否遵循ROBOTS协议，不遵守

#CONCURRENT_ITEMS #管道同时处理每个response的ITEM的最大值 ，默认为100
# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32 #爬虫的并发量，默认是16个 一般不用改

#DEPTH_LIMIT #爬取网站最大深度，如果为0则没有限制
#DOWNLOAD_TIMEOUT #设置超时时间


#LOG_ENCODING  #是否启用log信息
# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3  #下载延迟为3s

# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16   
#CONCURRENT_REQUESTS_PER_IP = 16  

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False #是否启动cookies，模拟登录之后用cookie，不需要登录尽量关闭cookie，cookie会留下痕迹。默认为开启

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {       #默认的请求报头，在这里写其他的地方就不需要写了
   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
   'User-Agent':'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 2.0.50727; SLCC2; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; Tablet PC 2.0; .NET4.0E)',
   'Accept-Language': 'en',
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {        #爬虫的中间件，很少写，下载中间件有时会用到
#    'ep1.middlewares.Ep1SpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {   #下载中间件
   'ep1.middlewares.Ep1DownloaderMiddleware': 543,  #优先级，数字越小，优先级越高  点代表文件夹，这个值一般在1-1000之间
   'ep2.middlewares.download_EP1':500,   #若有多个中间件 看优先级
}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {           #管道文件，决定下载好的数据如何作处理，经常写
#    'ep1.pipelines.mypipeline':100,  #优先级为100，
#   'ep1.pipelines.Ep1Pipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
