# _*_ coding : utf-8 _*_
# @Time : 2022/11/21 15:54
# @Author : chuyds
# @File : demo8_hanlder基本使用
# @Project : pythonProjectPc
import urllib.request

url = 'http://www.baidu.com'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}


request = urllib.request.Request(url=url, headers=headers)

# 1. 获取handler对象   2. build_opener  3. open
# 可以动态配置cooke，可以使用代理

handler = urllib.request.HTTPHandler()
opener = urllib.request.build_opener(handler)
response = opener.open(request)

content = response.read().decode('utf-8')

print(content)