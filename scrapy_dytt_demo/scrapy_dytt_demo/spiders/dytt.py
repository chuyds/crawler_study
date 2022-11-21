import scrapy
from scrapy_dytt_demo.items import ScrapyDyttDemoItem

# dytt主要练习二级页面跳转，用来熟悉多级页面的跳转，要熟悉这种写法
# 特别注意xpath的写法，有的不能返回值，写完以后要立即测试


class DyttSpider(scrapy.Spider):
    name = 'dytt'
    # allowed_domains = ['https://dy.dytt8.net/index2.htm']
    start_urls = ['https://dy.dytt8.net/index2.htm']
    # https://dy.dytt8.net/index2.htm

    def parse(self, response):

# //div[@class="co_area2"][1]/div[@class="co_content8"]//tbody/tr//a[2]/@href
# //div[@class="co_area2"][1]/div[@class="co_content8"]//tbody/tr//a[2]/text()
        print('_________________________________')
# //div[@class="co_content8"]//td[1]//a[2]/text()
        li_list = response.xpath('//div[@class="co_content8"]//td[1]')
        for li in li_list:
            name = li.xpath('.//a[2]/text()').extract_first()
            src = li.xpath('.//a[2]/@href').extract_first()

#           https://dy.dytt8.net/html/gndy/dyzz/20221105/63123.html
#           /html/newgame/20180124/56181.html
            url = 'https://dy.dytt8.net' + str(src)
            #   self.dyttFun注意不要添加（），如self.dyttFun()是错误形式
            yield scrapy.Request(url = url, callback = self.dyttFun, meta = {'name' : name})

    def dyttFun(self, response):

        src = response.xpath('//div[@id="Zoom"]//img/@src').extract_first()
        name = response.meta['name']

        item = ScrapyDyttDemoItem(name = name, src = src)

        yield item




