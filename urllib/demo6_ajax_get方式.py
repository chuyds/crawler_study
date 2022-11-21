# _*_ coding : utf-8 _*_
# @Time : 2022/11/21 15:53
# @Author : chuyds
# @File : demo6_ajax_get方式
# @Project : pythonProjectPc
import urllib.request
import urllib.parse

def creat_request(page):
    base_url = 'https://movie.douban.com/j/chart/top_list?type=24&interval_id=100%3A90&action=&'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
    }
    data = {
        'start':(page - 1) * 20,
        'limit':20
    }
    data = urllib.parse.urlencode(data)
    url = base_url + data
    request = urllib.request.Request(url=url, headers=headers)
    return request

def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content

def down_load(content, page):
    with open('douban_' + str(page) + '.json', 'w', encoding='utf-8') as fp:
        fp.write(content)

if __name__ == '__main__':
    start_page = int(input('输入起始页: '))
    end_page = int(input('输入结束页: '))


#https://movie.douban.com/j/chart/top_list?type=24&interval_id=100%3A90&action=&start=0&limit=20
    for page in range(start_page, end_page + 1):
        request = creat_request(page)
        content = get_content(request)
        down_load(content, page)