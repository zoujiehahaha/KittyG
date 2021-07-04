import requests

res=requests.get('https://space.bilibili.com/18523100/video?tid=0&page=2&keyword=&order=pubdate')
res.encoding='utf-8'
print(res.text)