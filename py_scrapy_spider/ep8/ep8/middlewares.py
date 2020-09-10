#coding:utf-8
from scrapy import signals
import random
from scrapy.utils.project import get_project_settings



class Ep8SpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.
    def process_request(self, request, spider):
        setting =get_project_settings()
        user_agent =setting['USER_AGENTS']
        useragent =random.choice(user_agent)
        request.headers.setdefault('User-Agent',useragent)

class Ep8DownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.
    def process_request(self, request, spider):
        setting =get_project_settings()
        user_agent =setting['USER_AGENTS']
        useragent =random.choice(user_agent)
        request.headers.setdefault('User-Agent',useragent)
