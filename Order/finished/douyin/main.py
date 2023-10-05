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


def get_main_page():
    """
    访问抖音主界面
    :return:
    """
    driver.get("https://www.douyin.com/")
    try_close_verify()


def search(title):
    """
    进行搜索
    :return:
    """
    driver.find_element(By.XPATH,
                        '//*[@id="douyin-header"]/div[1]/header/div/div/div[1]/div/div[2]/div/div[1]/form/input[1]').send_keys(
        title + Keys.ENTER)


def get_search_result(max_count=100):
    """
    获取搜索结果
    :return:
    """
    driver.switch_to.window(driver.window_handles[-1])
    parent = driver.find_elements(By.XPATH, '//*[@id="douyin-right-container"]/div[2]/div/div[3]/div[1]/ul')

    if not parent:
        print("搜索失败！")
        return

    parent = parent[0]

    i = 2
    while i < max_count:
        nodes = parent.find_elements(By.XPATH, './li[position()>=%d]' % i)

        if not nodes:
            print("搜索失败！")
            return

        for node in nodes:
            i += 1
            get_images(node)


def get_images(node):
    """
    下载图片
    :return:
    """
    # 定位元素
    driver.execute_script("arguments[0].scrollIntoView();", node)
    time.sleep(0.5)

    # 获取图片合计
    imgs = node.find_elements(By.XPATH, './/img[contains(@class, "LrgYn5wq") and contains(@class, "yWm90O3y")]')

    for img in imgs:
        download_image(img.get_attribute('src'))


def download_image(url):
    """
    下载当前图片
    :return:
    """
    print('下载图片', url)
    global image_index
    image_index += 1
    with open('E:/CGL/Assets/Images/Temp/%d.png' % image_index, 'wb') as f:
        f.write(requests.get(url, headers=DEFAULT_HEADERS).content)


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


def main():
    get_main_page()
    time.sleep(2)
    search('哆啦A梦表情包')
    time.sleep(5)
    get_search_result(100)


if __name__ == '__main__':
    input("press enter to start")
    start = time.time()
    main()
    print('爬取完毕,耗时', time.time() - start, 's')
    input("press enter to exit...")
