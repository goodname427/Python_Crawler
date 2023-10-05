import os

from Order.settings import *
from Order.crawlerlib import *
import json

nana_path = "E:/CGL/Assets/Images/NaNa/"
base_url = "https://m.weibo.cn/api/container/getIndex?type=uid&value=2687827715&containerid=1076032687827715&page="
download_url = 'https://weibo.com/'
headers = DEFAULT_HEADERS
headers['referer'] = "https://weibo.com/"


def get_image(page):
    print('爬取第%d页' % page)
    js = get_json(base_url + page.__str__(), headers)
    try:
        for ele in js['data']['cards']:
            if 'pics' not in ele['mblog']:
                continue

            for pic in ele['mblog']['pics']:
                url = pic['large']['url']
                filename = '{}/{}.png'.format(nana_path, pic["pid"])

                if os.path.exists(filename) or not url:
                    continue

                print('下载', filename)
                save_content(requests.get(url, headers=headers).content, filename)
    except Exception as ex:
        print(ex)


if __name__ == '__main__':
    for i in range(0, 10):
        get_image(i)
    print('爬取完毕')
