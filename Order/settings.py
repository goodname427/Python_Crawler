# 导入爬虫所需模块
import csv
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

# 默认报头
DEFAULT_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.62'
}

# 测试URL
TEST_URL = 'http://httpbin.org'
TEST_GET_URL = TEST_URL + '/get'

# 存储路径
SPIDER_PATH = 'E:/Spider/'
ORDER_PATH = SPIDER_PATH + 'Order/'
