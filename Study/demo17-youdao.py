import requests
import time
import math
import hashlib
import base64
from urllib import parse


def getsign(t):
    e = 'client=fanyideskweb&mysticTime={}&product=webfanyi&key=fsdsogkndfokasodnaso'.format(t)
    md5 = hashlib.md5()
    md5.update(e.encode('utf-8'))
    return md5.hexdigest()


url = 'https://dict.youdao.com/webtranslate'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.62'
}
data = {
    'i': '你好',
    'from': 'zh-CHS',
    'to': 'en',
    'domain': '1',
    'dictResult': 'true',
    'keyid': 'webfanyi',
    'client': 'fanyideskweb',
    'product': 'webfanyi',
    'appVersion': '1.0.0',
    'vendor': 'web',
    'pointParam': 'client,mysticTime,product',
    'mysticTime': math.floor(time.time() * 1000),
    'keyfrom': 'fanyi.web',
}

data['sign'] = getsign(data['mysticTime'])
# print(data)

# resp = requests.post(url, headers=headers, data=data)
# print(resp.text)
# eh6zVNeFZ0TD1ei8mSABcQ==
result = 'eh6zVNeFZ0TD1ei8mSABcQ=='
result = base64.b64decode(result)
result = result.decode('utf-8')

print(result)
