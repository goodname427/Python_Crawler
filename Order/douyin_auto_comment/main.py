import io
import random

from selenium.webdriver import Keys
from selenium.webdriver.common.action_chains import ActionChains

from Order.crawlerlib import *
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
driver.implicitly_wait(2)
image_index = 1
main_page_url = "https://www.douyin.com/"


def get_main_page():
    """
    访问抖音主界面
    :return:
    """
    driver.get(main_page_url)
    input("please login!")
    try_close_verify()


def try_close_verify():
    """
    尝试关闭验证界面
    :return:
    """
    # 验证
    ele = driver.find_elements(By.ID, 'verify-bar-close')
    if ele:
        ele[0].click()

    # 登录
    ele = driver.find_elements(By.CLASS_NAME, 'dy-account-close')
    if ele:
        ele[0].click()


def comment():
    ele = driver.find_elements(By.XPATH, "//*[@id=\"sliderVideo\"]/div[1]/div[1]/div/div[1]/div/div/div[3]/div/div[1]")
    if ele:
        ele[0].click()


def main():
    get_main_page()
    comment()


if __name__ == '__main__':
    # main_page_url = input("please enter main page url\n")
    main_page_url = "https://www.douyin.com/?recommend=1"  # input("please enter main page url\n")
    start = time.time()
    main()
    print('爬取完毕,耗时', time.time() - start, 's')
    input("press enter to exit...")

# https://www.douyin.com/?recommend=1
