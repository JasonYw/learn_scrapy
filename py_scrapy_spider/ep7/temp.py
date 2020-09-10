import re
'''
.//span[@class="title"][1]/text()   标题

.//p/span[contains(@class,"inq")]/text()  评论

.//div[@class="bd"]/p[1] 简介

.//span[@class="rating_num"]/text() 评分

.//span[4]/text()人数

//div[@class="item"]


https://movie.douban.com/top250?start=0&filter=  1
https://movie.douban.com/top250?start=25&filter=    2
https://movie.douban.com/top250?start=50&filter=    3

 'text': '<p class="">\n'
         '                            导演: 奥利维·那卡什 Olivier Nakache / 艾力克·托兰达 '
         'Eric Toledano\xa0\xa0\xa0主...<br>\n'
         '                            2011\xa0/\xa0法国\xa0/\xa0剧情 喜剧\n'
         '                        </p>',
 'title': '触不可及'}
'''
bb ='\n导演: 罗伯·莱纳 Rob Reiner\xa0\xa0\xa0主演:玛德琳·卡罗尔 Madeline Carroll / 卡...<br>\n" 2010\xa0/\xa0美国\xa0/\xa0剧情 喜剧 爱情\n'
a =re.findall(r'导演.[\u4e00-\u9fa5]+.[\u4e00-\u9fa5]+',bb)
b =re.findall(r'主演.[\u4e00-\u9fa5]+.[\u4e00-\u9fa5]+',bb)
c =re.findall(r'\d+',bb)
d=bb[-10:]
e =bb[-15:-10].replace('/','')
print(e)

