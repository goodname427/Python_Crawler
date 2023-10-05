import requests
import re
import time
import random
import csv
from lxml import etree

url = 'https://www.maoyan.com/board/4?offset={}'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.62',
    'Cookie': '__mta=256661812.1680609870098.1680613737934.1680624370403.15; uuid_n_v=v1; uuid=DC41CB00D2E011ED83DDF5FAAAD1D78DABDD5C4B4DCA4FED989D152FB6B1F214; _lxsdk_cuid=1874c278060c8-0e3387fe20d6f-7a545474-1fa400-1874c278060c8; _lxsdk=DC41CB00D2E011ED83DDF5FAAAD1D78DABDD5C4B4DCA4FED989D152FB6B1F214; _csrf=25ccb8d4ad5f6dcf30d759ffc6d615549a6eb87a5cb97630ce27e999b76e882e; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1680609870,1680624370; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1680624370; _lxsdk_s=1874d04c28e-5b0-a91-8ad%7C%7C2'
}

result = []

# 获取数据
for offset in range(0, 5):
    print('第%s页' % (offset + 1))
    full_url = url.format(offset * 10)
    resp = requests.get(url=full_url, headers=headers)
    html = etree.HTML(resp.text)
    # 存储对应数据
    new = html.xpath('//dl[@class="board-wrapper"]/dd')
    for node in new:
        item = {
            'name': node.xpath('.//p[@class="name"]/a/text()')[0].strip(),
            'star': node.xpath('.//p[@class="star"]/text()')[0].strip(),
            'time': node.xpath('.//p[@class="releasetime"]/text()')[0].strip()
        }
        result.append(item)
        print(item)

    time.sleep(random.randint(1, 2))

# 存储数据
with open('maoyan2.csv', 'w', newline='', encoding="utf-8") as f:
    # 生成csv操作对象
    writer = csv.DictWriter(f,fieldnames=['name', 'star', 'time'])
    writer.writeheader()
    writer.writerows(result)
