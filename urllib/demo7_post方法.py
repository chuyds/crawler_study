# _*_ coding : utf-8 _*_
# @Time : 2022/11/21 15:54
# @Author : chuyds
# @File : demo7_post方法
# @Project : pythonProjectPc
import urllib.request
import urllib.parse

# http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname
# cname: 芜湖
# pid:
# pageIndex: 2
# pageSize: 10

def get_request(page):
    url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
    }
    data = {
        'cname': '芜湖',
        'pid': '' ,
        'pageIndex': page,
        'pageSize': '10'
    }

    data = urllib.parse.urlencode(data).encode('utf-8')
    request = urllib.request.Request(url=url, headers=headers, data=data)
    return request

def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content

def down_load(content, page):
    with open('kfc_address' + str(page) + '.json', 'w', encoding='utf-8') as fp:
        fp.write(content)


if __name__ == '__main__':
    start_page = int(input('输入起始页面：'))
    end_page = int(input('输入结束页面：'))
    for page in range(start_page, end_page + 1):
        request = get_request(page)
        content = get_content(request)
        down_load(content, page)
