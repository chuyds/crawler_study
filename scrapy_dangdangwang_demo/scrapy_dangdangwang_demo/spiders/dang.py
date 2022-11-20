import scrapy
from scrapy_dangdangwang_demo.items import ScrapyDangdangwangDemoItem

class DangSpider(scrapy.Spider):
    name = 'dang'

#   如果要下载多页数据的话，那么必须要调整的是allowed_domains的范围一般情况下只写域名
    allowed_domains = ['category.dangdang.com']
    start_urls = ['http://category.dangdang.com/cp01.01.04.00.00.00.html']

    base_url = 'http://category.dangdang.com/pg'
    page = 1

    def parse(self, response):
#       piplines 管道 下载数据
#       items  用来定义数据结构
#       src = //ul[@id="component_59"]/li/a/img/@src
#       src = //ul[@id="component_59"]/li/a/img/@data-original  爬虫的时候要特别注意懒加载的问题
#       name = //ul[@id="component_59"]/li/a/img/@alt
#       price = //ul[@id="component_59"]/li//span[@class="search_now_price"]/text()

#       因为数据都在li标签下，所以可以使用这种方法。不过每一个分别xpath全路径查找也可以
        li_list = response.xpath('//ul[@id="component_59"]/li')
        for li in li_list:
            src = li.xpath('./a/img/@data-original').extract_first()
            if src:
                src = src
            else:
                src = li.xpath('a/img/@src').extract_first()
            name = li.xpath('./a/img/@alt').extract_first()
            price = li.xpath('.//span[@class="search_now_price"]/text()').extract_first()

#           定义items对象
            book = ScrapyDangdangwangDemoItem(src = src, name = name, price = price)
#           迭代器，获得一个对象就返回一个值（交给pipelines(管道)）
            yield book

#       爬取100页数据，每一页的爬取业务逻辑是一样的，所以我们只需要将执行的那个页的请求再次调用parse方法就可以了
#       http://category.dangdang.com/cp01.01.04.00.00.00.html
#       http://category.dangdang.com/pg1-cp01.01.04.00.00.00.html   可以发现第一页用这个url也可以
#       http://category.dangdang.com/pg2-cp01.01.04.00.00.00.html
#       http://category.dangdang.com/pg3-cp01.01.04.00.00.00.html

        if self.page < 5:
            self.page = self.page + 1
            url = self.base_url + str(self.page) + '-cp01.01.04.00.00.00.html'

#           怎么去调用parse方法
#           scrapy.Reuqset就是scrapy的get请求
#           url就是请求地址
#           callback是你要执行的那个函数，注意不要加（）
            yield scrapy.Request(url = url, callback = self.parse)


