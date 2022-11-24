import scrapy
from lol_equipment_img.items import LolEquipmentImgItem


class LolImgSpider(scrapy.Spider):
    name = 'lol_img'
    allowed_domains = ['www.wanplus.cn/lol/skill/item']
    start_urls = ['https://www.wanplus.cn/lol/skill/item']


    def parse(self, response):
        print('+++++++++++++++++++++++++++++++++++++++++')
        li_list = response.xpath('//div[@class="skill-itemlist"]//li')
        for li in li_list:
            name = li.xpath('.//img/@title').extract_first()
            src = li.xpath('.//img/@src').extract_first()
            ans = LolEquipmentImgItem(name = name, src = src)
            yield ans
