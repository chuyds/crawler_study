# _*_ coding : utf-8 _*_
# @Time : 2022/11/17 19:18
# @Author : chuyds
# @File : selenium_1_使用
# @Project : pythonProjectPc
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


path = Service('../chromedriver.exe')
browser = webdriver.Chrome(service=path)

url = 'https://www.baidu.com/'
browser.get(url)
input()

# 元素定位，根据id来找对象
# button = browser.find_element(value='su')
# print(button)

# 根据标签属性的属性值来获取对象
# button = browser.find_element('name', 'wd')
# print(button)

# 根据xpath语句来获取对象
# button = browser.find_elements(By.XPATH, '//input[@id="su"]')
# print(button)

# 根据标签的名字来获取对象
# button = browser.find_elements('tag name', 'input')
# print(button)

# 使用bs4的语法来获取对象
# button = browser.find_elements('css selector', '#su')
# print(button)

# 获取链接
# button = browser.find_elements('link text', '贴吧')
# print(button)

inputt = browser.find_element('id', 'su')
# 获取标签的属性
print(inputt.get_attribute('class'))
# 获取标签的名字
print(inputt.tag_name)

# 获取元素文本
a = browser.find_element('link text', '贴吧')
print(a.text)