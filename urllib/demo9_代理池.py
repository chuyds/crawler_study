# _*_ coding : utf-8 _*_
# @Time : 2022/11/21 15:56
# @Author : chuyds
# @File : demo9_代理池
# @Project : pythonProjectPc
import urllib.request
import urllib.parse
import random

proxies_pool = {
    {'http':'118.24.219.151:16817'},
    {'http':'118.24.219.151:16817'},
}

proxies = random.choice(proxies_pool)

url = 'http://www.baidu.com/s?wd=ip'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}

request = urllib.request.Request(url=url, headers=headers)

handler = urllib.request.ProxyHandler(proxies=proxies)

opener = urllib.request.build_opener(handler)

response = opener.open(request)

content = response.read().decode('utf-8')

with open('daili.html', 'w', encoding='utf-8') as fp:
    fp.write(content)