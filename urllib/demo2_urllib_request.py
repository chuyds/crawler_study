# _*_ coding : utf-8 _*_
# @Time : 2022/11/21 15:50
# @Author : chuyds
# @File : demo2_urllib_request
# @Project : pythonProjectPc
import urllib.request

url = 'http://www.baidu.com'
response = urllib.request.urlopen(url)

# 一个类型和六个方法
# response 是HTTPResponse的类型
# print(type(response))

# 按照一个字节，一个字节的去读
# content = response.read()
# print(content)

# 返回多少字节
# content = response.read(5)

# 读取一行&多行
# content = response.readline()
# content = response.readlines()

# 返回状态码，如果是200，那么就证明逻辑没用错
# print(response.getcode())

# 返回url地址
# print(response.geturl())

# 获取一个状态信息
# printf(response.getheaders())
