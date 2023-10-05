from urllib import request
from urllib import parse

url = 'http://www.baidu.com/s?wd={}'

word = input("请输入搜索内容：")
params = parse.quote(word)
full_url = url.format(params)

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0'}
req = request.Request(url=url, headers=headers)
resp = request.urlopen(req)
html = resp.read().decode('utf-8')

filename = word + '.html'
with open(filename, 'w', encoding='utf-8') as f:
    f.write(html)

