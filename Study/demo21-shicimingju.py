import os.path
from threading import Thread
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import requests
import re

base_url = 'https://www.shicimingju.com'

headers = {
    'User-Agent': UserAgent.random.__str__(),
    'Cookie': 'Hm_lvt_649f268280b553df1f778477ee743752=1680683810; Hm_lpvt_649f268280b553df1f778477ee743752=1680683820'
}


def get_catalog():
    url = base_url + '/book/liangjinyanyi.html'
    content = requests.get(url, headers=headers).content
    soup = BeautifulSoup(content, 'lxml')
    parent = soup.find(class_="book-mulu").ul

    dire = 'book/'
    if not os.path.exists(dire):
        os.mkdir(dire)

    t_list = []
    for child in parent.children:
        a = child.find('a')
        if isinstance(a, int):
            continue

        t = Thread(target=get_and_save_content, args=[a.text, a['href'], dire + a.text + '.txt'])
        t_list.append(t)
        t.start()

    for t in t_list:
        t.join()


def get_and_save_content(title, url, filename):
    print('爬取', title)
    content = get_content(url)
    save_content(content, filename)


def get_content(sub_url):
    url = base_url + sub_url
    content = requests.get(url, headers=headers).content
    soup = BeautifulSoup(content, 'lxml')
    content = soup.find(class_='card bookmark-list').text
    return content


def save_content(content, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)


if __name__ == '__main__':
    get_catalog()
