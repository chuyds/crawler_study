# _*_ coding : utf-8 _*_
# @Time : 2022/11/18 10:29
# @Author : chuyds
# @File : selenium_3_Chrome_handless
# @Project : pythonProjectPc
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
#
#
# chrome_options = Options()
# chrome_options.add_argument('‐‐headless')
# chrome_options.add_argument('‐‐disable‐gpu')
#
# # path是自己的chrome浏览器的文件路径
# path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
# chrome_options.binary_location = path
# browser = webdriver.Chrome(chrome_options=chrome_options)
# url = 'http://www.baidu.com/'
# browser.get(url)
# browser.save_screenshot('baidu.png')

# 配置封装
from selenium import webdriver
# 浏览器自带的，不需要额外的操作
from selenium.webdriver.chrome.options import Options

def share_browser():
# 初始化
    chrome_options = Options()
    chrome_options.add_argument('‐‐headless')
    chrome_options.add_argument('‐‐disable‐gpu')
    path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
    chrome_options.binary_location = path
    browser = webdriver.Chrome(chrome_options=chrome_options)
    return browser

browser = share_browser()
url = 'http://www.baidu.com/'
browser.get(url)
browser.save_screenshot('baidu2.png')



