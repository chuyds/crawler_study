# _*_ coding : utf-8 _*_
# @Time : 2022/11/21 15:52
# @Author : chuyds
# @File : demo4_请求对象定制_get访问
# @Project : pythonProjectPc
import urllib.request

url = 'https://www.baidu.com/s?wd='

# url的组成
# https://     www.baidu.com/       80/443     s        wd=周杰伦         #
#   协议 +            主机      +   端口号  +  路径   +     参数      +   锚点

# UA代理，模拟真的浏览器
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}

# 将周杰伦三个字变成unicode编码的格式
# 使用parse.quote()方法
# name = urllib.parse.quote('周杰伦')
# url = url + name

# 因为urlopen方法中不能存储字典，所以要请求对象的定制

data = {
    'wd' : '周杰伦',
    'sex' : '男',
    'location' : '中国台湾省'
}

new_data = urllib.parse.urlencode(data)

url = url + new_data
# print(url)

request = urllib.request.Request(url = url, headers = headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

print(content)