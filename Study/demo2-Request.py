from urllib import request

# 定义变量：URL 与 headers
url = 'http://httpbin.org/get'  # 向测试网站发送请求
# 重构请求头，伪装成 Mac火狐浏览器访问，可以使用上表中任意浏览器的UA信息
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:65.0) Gecko/20100101 Firefox/65.0'
}
# 1、创建请求对象，包装ua信息
req = request.Request(url=url, headers=headers)
# 2、发送请求，获取响应对象
res = request.urlopen(req)
# 3、提取响应内容
html = res.read().decode('utf-8')
print(html)
