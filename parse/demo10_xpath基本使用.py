# _*_ coding : utf-8 _*_
# @Time : 2022/11/21 15:56
# @Author : chuyds
# @File : demo10_xpath基本使用
# @Project : pythonProjectPc
from lxml import etree

# xpath解析
# 1. 本地文件           etree.parse
# 2. 服务器响应的数据   etree.HTML()

# xpath解析本地文件
tree = etree.parse('Demo10_xpath使用.html')


# tree.xpath('xpath路径')

# 查找ul标签下的li标签
# li_list = tree.xpath('//body/ul/li')

# 查找所有有id的属性的li标签
# text()获取标签中的内容
# li_list = tree.xpath('//ul/li[@id]/text()')

# 找到id为l1的li标签  注意引号问题
# li_list = tree.xpath('//ul/li[@id="l1"]/text()')

# 查找到id为l1的li标签的class的属性值
# li = tree.xpath('//ul/li[@id="l1"]/@class')

# 查询id中包含l的li标签
# li_list = tree.xpah('//ul/li[contains(@id,"l")]/text()')

# 查询id的值以l开头的li标签
# li_list = tree.xpath('//ul/li[starts-with(@id,"c")]/text()')

# 查询id为l1和class为c1的li标签
li_list = tree.xpath('//ul/li[@id="l1" and @class="c1"]/text()')

# li_list = tree.xpath('//ul/li[@id="l1"/text() | //ul/li[@id="12"]/text()]')

print(li_list)
print(len(li_list))