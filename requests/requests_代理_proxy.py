# _*_ coding : utf-8 _*_
# @Time : 2022/11/19 9:30
# @Author : chuyds
# @File : requests_代理_proxy
# @Project : pythonProjectPc
import requests

url = 'https://baidu.com/s?'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}

data = {
    'wd':'ip'
}

proxy = {
    # 看可以使用的ip代理
    'http':'121.230.210.31:3256'
}

response = requests.get(url = url,params = data, headers = headers, proxies = proxy )
content = response.text
with open('daili.html', 'w', encoding='utf-8') as fp:
    fp.write(content)
