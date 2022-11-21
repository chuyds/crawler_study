# _*_ coding : utf-8 _*_
# @Time : 2022/11/21 15:51
# @Author : chuyds
# @File : demo3_下载
# @Project : pythonProjectPc
import urllib.request

# 下载网页
# url_page = "http://www.baidu.com"
# urllib.request.urlretrieve(url_page, 'baidu.html')

# 下载图片
url_img = "https://tse1-mm.cn.bing.net/th/id/OIP-C.WFna_OH7VeEbKyg9L6ncawHaHa?w=182&h=182&c=7&r=0&o=5&dpr=1.25&pid=1.7"
urllib.request.urlretrieve(url_img, "lisa.jpg")

# 下载视频同理
# 获取视频地址
# 下载内容
