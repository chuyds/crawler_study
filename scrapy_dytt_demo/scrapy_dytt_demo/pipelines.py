# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class ScrapyDyttDemoPipeline:
    def open_spider(self, spider):
        self.fp = open('movie.json', 'w', encoding='utf-8')

        #   item的值就是yield后面的book对象

    def process_item(self, item, spider):
        #       以下这种模式不推荐，因为每传递过来一个对象，就要打开一次文件，对文件的操作过于频繁
        #       1. write方法必须要写一个字符串，而不是其它的对象
        #       2. w模式会对每一个对象都打开一次文件，会覆盖掉之前的内容
        #         with open('book.json', 'a', encoding = 'utf-8')as fp:
        #             fp.write(str(item))
        self.fp.write(str(item))
        return item

        # 在爬虫文件执行之后执行的方法

    def close_spider(self, spider):
        self.fp.close()

