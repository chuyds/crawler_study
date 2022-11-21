# _*_ coding : utf-8 _*_
# @Time : 2022/11/18 21:21
# @Author : chuyds
# @File : requests_get请求_使用
# @Project : pythonProjectPc
import requests

url = 'https://www.baidu.com'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}

data = {
    'wd':'北京'
}

response = requests.get(url=url, params=data, headers=headers)
content = response.text
print(content)