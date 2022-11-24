# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import urllib.request

class LolEquipmentImgPipeline:

    def open_spider(self, spider):
        self.fp = open('equipment_2.json', 'w', encoding = 'utf-8')

    def process_item(self, item, spider):
        self.fp.write(str(item))
        return item

    def close_spider(self, spider):
        self.fp.close()

class DangDangWangLoadPipeline:
    def process_item(self, item, spider):

        url = item.get('src')
        filename = './equipment_img/' + item.get('name') + '.jpg'
        urllib.request.urlretrieve(url = url, filename = filename)

        return item
