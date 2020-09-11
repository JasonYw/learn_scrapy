import requests

session =requests.session()
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36',
}
response =session.get('https://www.douban.com/',headers=headers)
print(response.cookies)
data ={'name':'15801367721','password':'forstudy','remember': 'false','ck':''}
response =session.post('https://accounts.douban.com/j/mobile/login/basic',data=data,headers=headers)
print(response.cookies)
print(response.text)
response =session.get('https://www.douban.com/',headers=headers)
print(response.text)