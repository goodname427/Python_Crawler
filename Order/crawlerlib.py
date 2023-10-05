import json
from typing import Any, AnyStr

from Order.settings import *


def get_fake_useragent() -> UserAgent:
    """获取fake_useragent"""
    return UserAgent(cache_path="Order/fake_useragent.json")


def get_soup(url: str, headers: dict = None) -> BeautifulSoup:
    """获取指定url的soup
    :param url:访问的url
    :param headers:报头
    """
    return BeautifulSoup(requests.get(url, headers=headers).text, 'lxml')


def get_json(url: str, headers: dict = None) -> Any:
    """获取指定url的json文档
    :rtype: object
    :param url:
    :param headers:
    :return:
    """
    return json.loads(requests.get(url, headers=headers).text)


def save_list(data_list: list[dict], filename: str, encoding: str = 'utf-8') -> None:
    """存储list
    :param data_list:要存储的列表
    :param filename:文件名称
    :param encoding:编码方式
    """
    if not data_list or len(data_list) == 0:
        return

    with open(filename, 'w', newline='', encoding=encoding) as f:
        writer = csv.DictWriter(f, data_list[0].keys())
        writer.writeheader()
        writer.writerows(data_list)


def save_content(content: AnyStr, filename: str) -> None:
    """存储二进制内容
    :param content:要存储的内容
    :param filename:文件名称
    """
    with open(filename, 'wb') as f:
        f.write(content)
