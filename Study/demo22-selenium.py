from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 创建Chrome浏览器对象
browser = webdriver.Edge()
# 访问百度网站
browser.get('http://www.baidu.com/')
# 通过id定义输入框
browser.find_element('id', "kw")
browser.find_element(By.ID, "kw")
# 通过class定义
browser.find_element('class name', "s_ipt_wr")
# 通过name定位
browser.find_element(By.NAME, "wd")
# 通过tag name定位:
browser.find_element(By.TAG_NAME, "input")
# 通过xpath定位
browser.find_element(By.XPATH, "//*[@id='kw']")
# 通过css选择器定位
browser.find_element(By.CSS_SELECTOR, "#kw")

# 自动退出浏览器
input('press enter to exit...')
browser.quit()
