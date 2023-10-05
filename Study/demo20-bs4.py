from bs4 import BeautifulSoup

from bs4 import BeautifulSoup

html_doc = """
<html><head><title>"c语言中文网"</title></head>
<body>
<p class="title"><b>c.biancheng.net</b></p>
<p class="website">一个学习编程的网站
<a href="http://c.biancheng.net/python/" id="link1">python教程</a>
<a href="http://c.biancheng.net/c/" id="link2">c语言教程</a>
"""

# 创建beautifulsoup解析对象
soup = BeautifulSoup(html_doc, 'html.parser')
# soup = BeautifulSoup(open('html_doc.html', encoding='utf8'), 'lxml')
print(soup.prettify())

print(soup.html)
# 获取整个p标签的html代码
print(soup.p)
# 获取b标签
print(soup.p.b)
# 获取p标签内容，使用NavigableString类中的string、text、get_text()
print(soup.p.text)
# 返回一个字典，里面是多有属性和值
print(soup.p.attrs)
# 查看返回的数据类型
print(type(soup.p))
# 根据属性，获取标签的属性值，返回值为列表
print(soup.p['class'])
# 给class属性赋值,此时属性值由列表转换为字符串
soup.p['class'] = ['Web', 'Site']
print(soup.p)

body_tag=soup.body
print(body_tag)
# 以列表的形式输出，所有子节点
print(body_tag.contents)
for child in body_tag.children:
    print(child)

# 查找所有a标签并返回
print(soup.find_all("a"))
# 查找前两条a标签并返回
print(soup.find_all("a", limit=2))
# 只返回两条a标签
print(soup.find_all("p",class_="website"))
print(soup.find_all(id="link4"))