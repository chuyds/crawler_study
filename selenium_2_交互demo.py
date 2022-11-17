# _*_ coding : utf-8 _*_
# @Time : 2022/11/17 21:33
# @Author : chuyds
# @File : selenium_2_交互demo
# @Project : pythonProjectPc
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

path = Service('chromedriver.exe')
browser = webdriver.Chrome(service=path)

url = 'https://www.baidu.com/'
browser.get(url)

import time
# 睡两秒
time.sleep(2)

# 获取文本框的对象
inputt = browser.find_element(value='kw')

# 在文本框中输入周杰伦
inputt.send_keys("周杰伦")

time.sleep(2)

# 获取百度一下按键
button = browser.find_element('id', 'su')
# 点击按钮
button.click()
time.sleep(2)

# 滑到底部
js_bottom = 'document.documentElement.scrollTop=100000'
browser.execute_script(js_bottom)
time.sleep(2)

# 可以全部都用xpath
next = browser.find_element('xpath', '//a[@class="n"]')
next.click()
time.sleep(2)

# 回到上一页
browser.back()
time.sleep(2)

# 再回去
browser.forward()
time.sleep(3)

# 退出
browser.quit()