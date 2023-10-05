import requests

url = 'https://pic4.zhimg.com/v2-8f51c35f5e8e48d3c8616a4353178689_1440w.jpg?source=172ae18b'
# 简单定义浏览器ua信息
headers = {'User-Agent': 'Mozilla/4.0'}
# 读取图片需要使用content属性
html = requests.get(url=url, headers=headers).content
# 以二进制的方式下载图片
with open('python_logo.jpg', 'wb') as f:
    f.write(html)
