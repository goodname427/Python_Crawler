# 导入parse模块
from urllib import parse

# 构建查询字符串字典
query_string = {
    'wd': '爬虫'
}

# 调用parse模块的urlencode()进行编码
result = parse.urlencode(query_string)
# 使用format函数格式化字符串，拼接url地址
url = 'http://www.baidu.com/s?{}'.format(result)
print(url)


