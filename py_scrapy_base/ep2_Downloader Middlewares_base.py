'''
反爬措施
动态切换User-Agent
如果不需要cookie，在setting里禁用cookie  COOKIES_ENABLED=False
设置延迟下载  ，在setting里 DOWNLOAD_DELAY=xx秒  默认为3s
使用搜索引擎 服务器页面的缓存，使用百度快照，通过搜索引擎缓存
使用IP地址池
使用crawllera 需要花钱买。这个服务




setting中设置DOWNLOADER_MIDDLEWARES={
    '目录.文件名.类名’：优先级
}
下载中间件写在setting目录同级里面

process_request(request,spider) 这个必须写 request当前要处理的请求，spider爬虫

HTTP代理原理就是用http协议 与代理服务器建立链接，协议包含主机ip和端口，如果需要身份验证就是账户密码，就需要加上验证信息

setting文件中变量名字一律大写

