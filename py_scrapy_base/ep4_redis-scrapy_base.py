'''
scrapy  是一个通用的爬虫框架，但是不支持分布式，scrapy_redis是为了更方便地实现scrapy分布式爬取，而提供了一些以redis为基础的组件(仅有组件)
数据会统一放在redis组里，开一个数据库
scrapy-redis提供了四个组件
调度器
去重在redis数据库里去除
管道文件，数据不在交给管道了，而是交给redis
爬虫类会被改变 crawlspider 还有 spider 也被修改

流程图 
请求给 给 引擎  
引擎给redis数据库  数据库里有三个库 存数据 存请求队列 存请求指纹 先做指纹比对，去重，若没有发过进队列
redis给调度器
调度器给下载器
下载器等到的响应文件给爬虫
管道文件可写可不写 分布式为了集中存储

scrapy框架 本身队列不支持共享，scrapy-redis 就是把队列换成数据库，数据库集合 set就可以去重
spider类在redis-scrpay中变成 redisspider   crawlspider变成 rediscrawlspider

Master：核心服务器端 搭建redis数据库 不负责爬取，但是它可以进行爬取，一般项目里 服务器端 是不负责爬取的，减少服务器的负载，负责指纹去重，request的分配，数据存储
               Master只有一个数据库


Slaver端：多台电脑 不限制系统，负责爬取，新的请求给master先做去重  Master对应多个Slaver端

任务调度，去重 scrapy-redis已经做好了 只需要继承redisspider或者rediscrawlspider指定一个redis_key就可以了，redis_key是开始的钥匙

缺点：scrapy-redis调度对象是request对象，里面信息比较大，不仅有url还有callback，可能降低爬虫速度，因为占用了redis大量的存储空间，要保证效率的话 需要一定硬件



第一步下载scrapy-redis库 
'''
'''
这里对Redis数据库的配置进行了详细说明，部分配置选项如下：

daemonize：是否以后台进程运行，默认为no。Windows下不支持修改 。Linux平台下可以改为yes，这样就不用为了启动Redis而单独保留一个shell窗口。
pidfile：如以后台进程运行，则需指定一个pid，默认为/var/run/redis.pid。Windows下不支持修改。
bind：绑定主机IP，默认值为127.0.0.1（注释）
protected-mode：以保护模式运行，默认yes
port： 监听端口，默认为6379
timeout： 超时时间，默认为300（秒）
loglevel： 日志记录等级，有4个可选值，debug，verbose（默认值），notice，warning
logfile： 日志记录方式，默认值为stdout
databases： 可用数据库数，默认值为16，默认数据库为0
save <seconds> <changes>： 指出在多长时间内，有多少次更新操作，就将数据同步到数据文件。这个可以多个条件配合，比如默认配置文件中的设置，就设置了三个条件。
save 900 1 900秒（15分钟）内至少有1个key被改变
save 300 10 300秒（5分钟）内至少有300个key被改变
save 60 10000 60秒内至少有10000个key被改变
rdbcompression： 存储至本地数据库时是否压缩数据，默认为yes
dbfilename： 本地数据库文件名，默认值为dump.rdb
dir： 本地数据库存放路径，默认值为 ./
slaveof： <masterip> <masterport> 当本机为从服务时，设置主服务的IP及端口（注释）
masterauth： <master-password> 当本机为从服务时，设置主服务的连接密码（注释）
requirepass 连接密码（注释）
maxclients： 最大客户端连接数，默认不限制（注释）
maxmemory <bytes>： 设置最大内存，达到最大内存设置后，Redis会先尝试清除已到期或即将到期的Key，当此方法处理后，任到达最大内存设置，将无法再进行写入操作。（注释）
appendonly： 是否在每次更新操作后进行日志记录，如果不开启，可能会在断电时导致一段时间内的数据丢失。因为redis本身同步数据文件是按上面save条件来同步的，所以有的数据会在一段时间内只存在于内存中。默认值为no
appendfilename： 更新日志文件名，默认值为appendonly.aof（注释）
appendfsync： 更新日志条件，共有3个可选值。no表示等操作系统进行数据缓存同步到磁盘，always表示每次更新操作后手动调用fsync()将数据写到磁盘，everysec表示每秒同步一次（默认值）。
vm-enabled： 是否使用虚拟内存，默认值为no
vm-swap-file： 虚拟内存文件路径，默认值为/tmp/redis.swap，不可多个Redis实例共享
vm-max-memory： 将所有大于vm-max-memory的数据存入虚拟内存,无论vm-max-memory设置多小,所有索引数据都是内存存储的(Redis的索引数据就是keys),也就是说,当vm-max-memory设置为0的时候,其实是所有value都存在于磁盘。默认值为0。

每个配置选项前都有详细的英文注释，如有需要可自行查阅配置

'''
#想要redis支持分布式，需要把配置文件里 bind 127.0.0.1注释掉即可，这样任何端都可以访问
#redis启动会占用终端窗口 port：6379
#若不喜欢占用一个terminal 就把daemonize no改成yes  变成守护行程
#windows执行的时候要用管理眼模式执行cmd   执行 redis-server 配置文件根目录 使用redis -cli 查看redis是否启动

#爬虫端不需要启动redis-server只要能ping通master端就行。

#redis-scrapy分布式 排查错误

#首先服务器 与电脑之间必须能相互ping通
#之后查看master的redis的配置，注释掉本机ip以及关掉保护模式
#之后查看master 的redis服务启动没有，并坚持客户端的redis服务。
#之后查看端口号


#远程发送项目到其他局域网的计算机
#先把项目打包
#tar -cvf  包的名字 目标文件绝对路径 
#sftp 目标计算机的用户名@ip地址
#如果需要密码 输入密码
#put bao.tar 文件
#之后解压缩
#tar -xvf  bao.tar

