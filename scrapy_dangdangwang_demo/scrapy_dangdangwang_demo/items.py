# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyDangdangwangDemoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 通常的说就是要下载的数据都有什么

    # 图片
    src = scrapy.Field()
    # 名字
    name = scrapy.Field()
    # 价格
    price = scrapy.Field()


