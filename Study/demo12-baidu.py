import os
from urllib import parse
import requests
import re

word = input('请输入你想下载的图片名称：')

url = 'https://image.baidu.com/search/flip?tn=baiduimage&word=' + parse.quote(word)
headers = {
    'User-Agent': 'Mozilla/4.0'
}
pattern = re.compile(r'"hoverURL":"(.*?)"', re.S)

resp = requests.get(url, headers=headers)
directory = 'baidu images/' + word
if not os.path.exists(directory):
    os.makedirs(directory)

i = 1
for img_url in pattern.findall(resp.text):
    try:
        filename = '{}/{}_{}.jpg'.format(directory, word, i)
        content = requests.get(img_url, headers=headers).content
        with open(filename, 'wb') as f:
            f.write(content)
        print(filename, '下载成功')
        i += 1
    except:
        pass
