from Order.crawlerlib import *
import time


def login():
    """登录"""
    browser.get('https://www.bilibili.com/')
    browser.find_element(By.CLASS_NAME, 'right-entry__outside go-login-btn').click()
    input('手工登录...')
    pass


def get_dynamic(uid):
    url = 'https://space.bilibili.com/{}/dynamic'.format(uid)


def follow():

    print()


def main():
    login()
    follow()


if __name__ == '__main__':
    start = time.time()
    browser = webdriver.Edge()
    browser.implicitly_wait(20)
    main()
    print('爬取完毕,耗时', time.time() - start, 's')
