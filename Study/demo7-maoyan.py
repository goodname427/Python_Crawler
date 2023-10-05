from urllib import request
import re
import time
import random
import csv

url = 'https://www.maoyan.com/board/4?offset={}'
pattern = re.compile(r'<div class="movie-item-info">.*?title="(.*?)".*?class="star">(.*?)</p>.*?releasetime">(.*?)</p>',
                     re.S)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.62',
    'Cookie': '__mta=256661812.1680609870098.1680612029282.1680612245997.8; uuid_n_v=v1; uuid=DC41CB00D2E011ED83DDF5FAAAD1D78DABDD5C4B4DCA4FED989D152FB6B1F214; _csrf=aabc36bd6ea2ceb329b194222d17b7d9df14f99c5e83679a92f7ccce74c81795; _lxsdk_cuid=1874c278060c8-0e3387fe20d6f-7a545474-1fa400-1874c278060c8; _lxsdk=DC41CB00D2E011ED83DDF5FAAAD1D78DABDD5C4B4DCA4FED989D152FB6B1F214; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1680609870; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1680612246; _lxsdk_s=1874c278061-300-f09-b8c%7C%7C28'
}

result = []

# 获取数据
for offset in range(0, 5):
    print('第%s页' % (offset + 1))
    full_url = url.format(offset * 10)
    req = request.Request(url=full_url, headers=headers)
    resp = request.urlopen(req)
    html = resp.read().decode()
    # print(html)
    # 存储对应数据
    new = pattern.findall(html)
    print('爬取数据',len(new))
    result += new
    time.sleep(random.randint(1, 2))

# 存储数据
with open('maoyan.csv', 'w', newline='', encoding="utf-8") as f:
    # 生成csv操作对象
    writer = csv.writer(f)
    # 整理数据
    for r in result:
        name = r[0].strip()
        star = r[1].strip()[3:]
        # 上映时间：2018-07-05
        # 切片截取时间
        time = r[2].strip()[5:15]
        L = [name, star, time]
        # 写入csv文件
        writer.writerow(L)
        print(name, time, star)

