# _*_ coding : utf-8 _*_
# @Time : 2022/11/21 15:53
# @Author : chuyds
# @File : demo5_post请求
# @Project : pythonProjectPc
import urllib.request
import urllib.parse

url = 'https://fanyi.baidu.com/sug'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}

data = {
    'kw':'spider'
}

# post请求的参数 必须要进行编码  encode变为字节流
data = urllib.parse.urlencode(data).encode('utf-8')

# post请求的参数不能拼接在url的后面，而是需要放在请求对象定制的参数中
request = urllib.request.Request(url=url, headers=headers, data=data)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

# 字符串 -> json对象
import json
obj = json.loads(content)
print(obj)