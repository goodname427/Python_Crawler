import requests

data = {
    'name': '编程帮',
    'url': "www.biancheng.net"
}

response = requests.get('http://httpbin.org/get', params=data)
# 直接拼接参数也可以
# response = requests.get(http://httpbin.org/get?name=gemey&age=22)
# 调用响应对象text属性，获取文本信息
print(response.text)

# 百度翻译
url = 'https://fanyi.baidu.com'
# post请求体携带的参数，可通过开发者调试工具查看
# 查看步骤：NetWork选项->Headers选项->Form Data
data = {
    'from': 'zh',
    'to': 'en',
    'query': '编程帮www.biancheng.net你好'
}
response = requests.post(url, data=data)
print(response.text)
