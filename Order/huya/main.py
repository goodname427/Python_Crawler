import os
import random
import uuid
from Order.crawlerlib import *
import time
import pywinauto
from pywinauto.keyboard import send_keys

browser = webdriver.Edge()
browser.implicitly_wait(2)
first = True
config = {}


def load_config():
    with open('config.txt', 'r', encoding='UTF-8') as f:
        for line in f.readlines():
            if len(line) == 1 or line[0] == '#':
                continue
            splits = line.replace('\n', '').split('=')
            config[splits[0]] = splits[1]


def get_file():
    for _, _, files in os.walk(config['video_directory']):
        file = random.choice(files)
        extension = os.path.splitext(file)[-1]
        new_file = uuid.uuid4().hex + extension
        os.rename(config['video_directory'] + '\\' + file, config['video_directory'] + '\\' + new_file)
        return new_file


def upload_file():
    """
    上传文件
    :return:
    """
    browser.find_elements(By.XPATH,
                          '//*[@id="main_col"]/div/div[2]/div[2]/div/div[1]/div[2]/div/div[1]/div[2]/button')[0].click()
    time.sleep(1)
    # 使用pywinauto来选择文件
    app = pywinauto.Desktop()
    # 选择文件上传的窗口
    dlg = app["打开"]
    # 选择文件地址输入框，点击激活
    dlg.click_input()
    dlg["Toolbar3"].click()
    # 键盘输入上传文件的路径
    send_keys(config['video_directory'])
    # 键盘输入回车，打开该路径
    send_keys("{VK_RETURN}")
    # 选中文件名输入框，输入文件名
    dlg["文件名(&N):Edit"].type_keys(get_file())
    # 点击打开
    dlg["打开(&O)"].click()


def select_class():
    """
    选择分类
    :return:
    """
    # 点击分类按钮
    browser.find_element(By.XPATH, '//*[@id="main_col"]/div/div[2]/div/div/div[2]/div[2]/div[4]/div[2]/div/div').click()
    # 选择对应分类
    browser.find_element(By.XPATH,
                         '//*[@id="main_col"]/div/div[2]/div/div/div[2]/div[2]/div[4]/div[2]/div/div/div/div[3]/div[2]/div[1]').click()


def set_config():
    """
    设置视频参数
    :return:
    """
    # 设置视频分类
    select_class()
    # 设置用户协议
    global first
    if first:
        browser.find_element(By.XPATH,
                             '//*[@id="main_col"]/div/div[2]/div/div/div[2]/div[2]/div[9]/div[2]/div/img').click()
        first = False
    time.sleep(0.5)
    # 设置视频名称
    video_input_ele = browser.find_element(By.XPATH,
                                           '//*[@id="main_col"]/div/div[2]/div/div/div[2]/div[2]/div[2]/div[2]/input')
    video_input_ele.clear()
    time.sleep(0.5)
    video_input_ele.send_keys(config['video_name'])


def upload_video():
    """
    上传视频
    :return:
    """
    # 上传视频文件
    upload_file()
    time.sleep(2)
    # 设置视频参数
    set_config()
    # 等待文件上传成功
    state = browser.find_element(By.XPATH, '//*[@id="main_col"]/div/div[2]/div/div/div[2]/div[1]/div[1]/div[2]')
    while '上传成功' not in state.text:
        time.sleep(1)
    # 上传视频
    browser.find_element(By.XPATH, '//*[@id="main_col"]/div/div[2]/div/div/div[2]/div[2]/div[10]/div[1]').click()
    time.sleep(2)
    # 关闭通知
    browser.find_element(By.XPATH, '/html/body/div[5]/div/div[1]/button').click()

    time.sleep(int(config['interval']))


def main():
    load_config()
    browser.get('https://hd.huya.com/web/video-process/index.html#/home')
    input('请登录后按下回车键继续')
    while True:
        upload_video()


if __name__ == '__main__':
    start = time.time()
    main()
    print('爬取完毕,耗时', time.time() - start, 's')
