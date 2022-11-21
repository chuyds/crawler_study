# _*_ coding : utf-8 _*_
# @Time : 2022/11/21 15:49
# @Author : chuyds
# @File : demo1_获取网页源码
# @Project : pythonProjectPc
# 使用urllib来获取百度首页源码
import urllib.request

# 1. 定义一个url
url = "http://www.baidu.com"

# 2. 模拟浏览器向服务器发送请求
response = urllib.request.urlopen(url)

# 3. 获取响应中的页面源码
# read 返回的是字节形式二进制数据
# 解码：将二进制数据转化为字符串  decode（'编码格式'）
content = response.read().decode('utf-8')

print(content)