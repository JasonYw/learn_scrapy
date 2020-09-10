# Scrapy settings for example project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#
SPIDER_MODULES = ['example.spiders']
NEWSPIDER_MODULE = 'example.spiders'

USER_AGENT = 'scrapy-redis (+https://github.com/rolando/scrapy-redis)'

DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter" #去重类换成redis里的组件里的去重

SCHEDULER = "scrapy_redis.scheduler.Scheduler"  #调度器换成srcapy-redis调度器

SCHEDULER_PERSIST = True   #我的项目可以暂停 ，暂停后 reids不会情况数据，允许暂停，如果是False，暂停之后就是重写爬了

#默认的scrapy-redis请求集合，按优先级排序

#以下三个选项，可选择一个默认的scrapy-redis请求集合，第一个按顺序出队列
#SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderPriorityQueue"

#队列形式，队列形式的规则是先进先出
#SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderQueue"

#栈的格式，请求先进后出
#SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderStack"

#scrapy-redis.pipelines.RedisPipeline  支持将数据到存储到数据库里，必须启动
ITEM_PIPELINES = {
    'example.pipelines.ExamplePipeline': 300,
    'scrapy_redis.pipelines.RedisPipeline': 900,   #若有很多管道数据库，redis数据库的优先级一定是最低的，redis数据库不会进行return item
}

LOG_LEVEL = 'DEBUG'


#指定数据库的ip和端口，如果不写 就是默认的本地数据路
REDIS_HOST ="192.168.1.44"  #如果不写 就是默认的本地数据路
REDIS_PORT=6379


# Introduce an artifical delay to make use of parallelism. to speed up the
# crawl.
DOWNLOAD_DELAY = 1
