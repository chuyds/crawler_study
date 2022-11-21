# _*_ coding : utf-8 _*_
# @Time : 2022/11/21 16:00
# @Author : chuyds
# @File : demo12_xpath下载图片
# @Project : pythonProjectPc
# _*_ coding : utf-8 _*_
# @Time : 2022/11/13 11:15
# @Author : chuyds
# @File : demo
# @Project : pythonProjectPc
import urllib.request
import urllib.parse
from lxml import etree


# //body//div[@class="new-two-page-box container"]/a/@href
# https://sc.chinaz.com/tupian/chouxiangtupian.html
# javascript:;
# chouxiangtupian_2.html
# chouxiangtupian_3.html
# chouxiangtupian_4.html
# chouxiangtupian_5.html
# chouxiangtupian_6.html
# chouxiangtupian_262.html
# chouxiangtupian_2.html

def creat_request(page):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
    }

    if (page == 1):
        url = 'https://sc.chinaz.com/tupian/chouxiangtupian.html'
    else:
        url = 'https://sc.chinaz.com/tupian/' + 'chouxiangtupian_' + str(page) + '.html'

    request = urllib.request.Request(url=url, headers=headers)
    return request


def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content


def down_load(content):
    tree = etree.HTML(content)
    # //body//div[@class="tupian-list com-img-txt-list masonry"]//img/@alt
    # //body/div[@class="container"]//img/@alt
    name_list = tree.xpath('//body/div[@class="container"]//img/@alt')
    src_list = tree.xpath('//body/div[@class="container"]//img/@src')

    # "//scpic.chinaz.net/files/default/imgs/2022-11-01/80dc1cbc8aef7846_s.jpg"
    # https://scpic.chinaz.net/files/default/imgs/2022-11-01/80dc1cbc8aef7846_s.jpg
    for i in range(len(name_list)):
        name = name_list[i]
        src = src_list[i]
        url = 'https:' + src
        urllib.request.urlretrieve(url=url, filename='./img/' + name + '.jpg')


if __name__ == '__main__':
    start_page = int(input('输入起始页面：'))
    end_page = int(input('输入结束页面：'))

    for page in range(start_page, end_page + 1):
        request = creat_request(page)
        content = get_content(request)
        down_load(content)
