# _*_ coding : utf-8 _*_
# @Time : 2022/11/19 10:00
# @Author : chuyds
# @File : cookie登录古诗文网
# @Project : pythonProjectPc
# 通过登录，进入主页面

# 通过查看登录接口，发现登录时需要很多参数
# __VIEWSTATE:CN/FWQifjpBL7o3FC9v7SoMGt/Os35sa7hIn6H+y0MekpBaksj/Hy5IDVD301sGGthpEhIKcpOeOkzXwWacO+akBkgDiFRE0iwgb8RELULj3LQ3Pgr2Gmj1EMCB8SP5Cx6jaUycNjioNMFCsPz2IIsCeU0w=
# __VIEWSTATEGENERATOR:C93BE1AE
# from:http://so.gushiwen.cn/user/collect.aspx
# email:364203330@qq.com
# pwd:123344
# code: 71GU
# denglu: 登录

# 我们观察到__VIEWSTATE和__VIEWSTATEGENERATOR  code  是变化的量
# （1）__VIEWSTATE和__VIEWSTATEGENERATOR  一般情况下看不到的数据  都是在页面的源码中
#   这两个数据在页面源码中，所以我们需要获取页面的源码，然后进行解析就可以获取到
# （2）验证码

import requests
from bs4 import BeautifulSoup

# 登录页面的url
url = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}
# 获取页面源码
response = requests.get(url = url, headers = headers)
content = response.text

# 解析页面源码，然后获取__VIEWSTATE和__VIEWSTATEGENERATOR
# 用bs4和xpath都可以
soup = BeautifulSoup(content, 'lxml')

# 获取__VIEWSTATE
viewstate = soup.select('#__VIEWSTATE')[0].attrs.get('value')

# 获取__VIEWSTATEGENERATOR
viewstategenerator = soup.select('#__VIEWSTATEGENERATOR')[0].attrs.get('value')

# 获取验证码图片
code = soup.select('#imgCode')[0].attrs.get('src')
code_url = 'https://so.gushiwen.cn' + code

# 有坑，下载验证码图片后会导致下次访问时更新，导致不是一个图片
# import urllib.request
# urllib.request.urlretrieve(url = code_url, filename = 'code.jpg')

# 使用session解决这个问题
session = requests.session()
response_code = session.get(code_url)
# 注意此时要使用的是二进制数据，因为要使用图片的下载
content_code = response_code.content
# wb的模式就是将二进制数据写入到文件
with open('code.jpg', 'wb') as fp:
    fp.write(content_code)

# 获取了验证码的图片之后，下载到本地，然后观察验证码，将验证码输入到控制台
# 有插件可以自动识别图片上的验证码，比如超级鹰等
code_name = input('请输入你的验证码')

data_post = {
    '__VIEWSTATE':viewstate,
    '__VIEWSTATEGENERATOR':viewstategenerator,
    'from':'http://so.gushiwen.cn/user/collect.aspx',
    'email':'364203330@qq.com',
    'pwd':'yushui123',
    'code':code_name,
    'denglu': '登录',
}

response_post = session.post(url = url, headers = headers, data = data_post)
content_post = response_post.text
with open('gushiwen.html', 'w', encoding='utf-8') as fp:
    fp.write(content_post)
