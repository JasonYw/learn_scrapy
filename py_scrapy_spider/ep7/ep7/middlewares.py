import random
from scrapy.utils.project import get_project_settings
import base64

#spider????yeild ????????user-agent
class RandomUserAgent(object):

    def process_request(self,request,spider):
        settings =get_project_settings()
        user_agent =settings['USER_AGENTS']
        useragent =random.choice(user_agent)
        request.headers.setdefault('User-Agent',user_agent)
        #print(useragent)


#???useragent???
class RandomProxy(object):
    def process_request(self,request,spider):
        settings=get_project_settings()
        proxy =settings['PROXYIES_PRA']
        proxy_one =random.choice(proxy)


        if proxy_one['USR_PASSWD'] is None:  #?????????????????

            request.meta['proxy'] ='http://'+proxy_one['IP_PORT']    #request.meta['proxy']????

        else: #????????? base64   base64????ascii?? ???????????
            
            #???????base64????
            #??????USR_PASSWD,??base64.b64encode???????????utf-8??
            base64_userpasswd =base64.b64encode(proxy_one['USR_PASSWD'].encode('utf-8')) 

            request.meta['proxy'] ='http://'+proxy_one['IP_PORT']

           #headers['Proxy-Authorization']??????????????Basic??
            request.headers['Proxy-Authorization'] ='Basic '+str(base64_userpasswd)


            



