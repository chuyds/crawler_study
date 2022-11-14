# https://sc.chinaz.com/tupian/qinglvtupian.html
# https://sc.chinaz.com/tupian/qinglvtupian_2.html
import urllib.request
import urllib.parse
from lxml import etree
from bs4 import BeautifulSoup

def creat_request(page):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
    }

    if (page == 1):
        url = 'https://sc.chinaz.com/tupian/qinglvtupian.html'
    else:
        url = 'https://sc.chinaz.com/tupian/qinglvtupian_' + str(page) + '.html'

    request = urllib.request.Request(url=url, headers=headers)
    return request

def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content

def down_load(content):
    tree = etree.HTML(content)
    name_list = tree.xpath('//div[@class="container"]//img/@alt')
    # //div[@class="container"]//img/@data-original
    src_list = tree.xpath('//div[@class="container"]//img/@data-original')
    for i in range(len(name_list)):
        name = name_list[i]
        src = src_list[i]
        url = 'https:' + src
        urllib.request.urlretrieve(url=url, filename= './img/' + name + '.jpg')

if __name__ == '__main__':
    start_page = int(input('开始页：'))
    end_page = int(input('结束页：'))

    for page in range(start_page, end_page + 1):
        request = creat_request(page)
        content = get_content(request)
        down_load(content)