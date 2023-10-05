import csv
import os.path
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

base_url = 'https://www.jd.com/'
webdriver = webdriver.Edge()
filename = 'jd.csv'


def search(key):
    webdriver.get(base_url)
    webdriver.find_element(By.XPATH, '//*[@id="key"]').send_keys(key)
    webdriver.find_element(By.XPATH, '//*[@id="search"]/div/div[2]/button').click()


def get_data():
    time.sleep(3)
    webdriver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    r_list = webdriver.find_element(By.XPATH, '//*[@id="J_goodsList"]/ul')

    # 获取数据
    data_list = []
    for r in r_list.find_elements(By.XPATH, './li'):
        try:
            item = {
                'name': r.find_element(By.XPATH, './/div[contains(@class,"p-name") and contains(@class,"p-name-type-2")]').text,
                'price': r.find_element(By.XPATH, './/*[@class="p-price"]').text,
                'count': r.find_element(By.XPATH, './/*[@class="p-commit"]').text,
                'shop': r.find_element(By.XPATH, './/*[@class="J_im_icon"]').text,
            }
            data_list.append(item)
            print(item['name'])
        finally:
            pass

    # 保存数据
    save_data(data_list)


def save_data(data_list):
    if not data_list or len(data_list) == 0:
        return

    with open(filename, 'a', newline='') as f:
        writer = csv.DictWriter(f, data_list[0].keys())
        writer.writeheader()
        writer.writerows(data_list)


def next_page():
    if webdriver.page_source.find('pn-next disabled') == -1:
        webdriver.find_element(By.CLASS_NAME, 'pn-next').click()
        return True
    return False


if __name__ == '__main__':
    try:
        webdriver.implicitly_wait(10)
        search('python')

        if os.path.exists(filename):
            os.remove(filename)

        i = 0
        # 爬取数据
        while True:
            i += 1
            print('---第%d页---' % i)
            get_data()
            if not next_page() or i >= 10:
                break

        input('press enter to exit...')
    finally:
        webdriver.close()
        webdriver.quit()
