from urllib import request

resp = request.urlopen("http://www.baidu.com")
html_text = resp.read().decode('utf-8')
print(html_text)


