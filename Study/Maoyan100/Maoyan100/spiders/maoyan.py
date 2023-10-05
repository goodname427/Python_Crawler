import scrapy
from Study.Maoyan100.Maoyan100.items import Maoyan100Item


class Maoyan100Spider(scrapy.Spider):
    # name 指定爬虫文件名字
    name = 'maoyan'
    allowed_domains = ['maoyan.com']  # 网站域名
    start_urls = ['https://maoyan.com/board/4?offset=0']  # 第一个要抓取的url
    offset = 0  # 查询字符串参数

    # response 为 start_urls中影响对象
    def parse(self, response, **kwargs):
        # 基准xpath，匹配电影信息的dd节点对象列表
        dd_list = response.xpath('//dl[@class="board-wrapper"]/dd')
        # 给items.py 中的类：Maoyan100Item（）实例化
        item = Maoyan100Item()
        for dd in dd_list:
            item['name'] = dd.xpath('./a/@title').get().strip()  # 1.6以后版本使用   原来用 extract_first()
            item['star'] = dd.xpath('.//p[@class="star"]/text()').get().strip()
            item['time'] = dd.xpath('.//p[@class="releasetime"]/text()').get().strip()
            yield item
        if self.offset < 90:  # 判断条件
            self.offset += 10
            url = 'https://maoyan.com/board/4?offset=' + str(self.offset)
            # 把url交给secheduer入队列
            # response会自动传给 callback 回调的 parse()函数
            # Scrapy.request()向url发起请求，并将响应结果交给回调的解析函数
            yield scrapy.Request(url=url, callback=self.parse)
