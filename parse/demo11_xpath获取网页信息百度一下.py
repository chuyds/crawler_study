# _*_ coding : utf-8 _*_
# @Time : 2022/11/21 15:59
# @Author : chuyds
# @File : demo11_xpath获取网页信息百度一下
# @Project : pythonProjectPc
import urllib.request
import urllib.parse
from lxml import etree

url = "https://www.baidu.com/"

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}

request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)

contnet =  response.read().decode('utf-8')

tree = etree.HTML(contnet)

ans = tree.xpath('//input[@id="su"]/@value')[0]

print(ans)
