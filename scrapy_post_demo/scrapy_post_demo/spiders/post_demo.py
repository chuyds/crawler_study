import scrapy
import json

class PostDemoSpider(scrapy.Spider):
    name = 'post_demo'
    allowed_domains = ['https://fanyi.baidu.com/sug']
    # post请求，如果没有参数，那么这个请求将没有任何意义
    # 所以start_urls 也没有用了
    # parse方法也没有用了
    # start_urls = ['http://fanyi.baidu.com/']

    # def parse(self, response):
    #     pass

    # get 请求用parse方法，框架封装好的
    # post请求用start_requests，框架封装好的

    def start_requests(self):
        url = 'https://fanyi.baidu.com/sug'

        data = {
            'kw':'final'
        }

        yield scrapy.FormRequest(url = url, formdata = data, callback = self.parse_second)

    def parse_second(self, response):

        content = response.text
        obj = json.loads(content)
        print(obj)
