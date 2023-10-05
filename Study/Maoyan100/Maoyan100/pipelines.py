import csv

import pymysql
from Study.Maoyan100.Maoyan100.settings import *


class Maoyan100Pipeline(object):
    def process_item(self, item, spider):
        print(item['name'], item['star'], item['time'])
        return item  # 多个管道有体现


# 存入mysql数据库的管道
class Maoyan100CSVPipeline(object):
    # 开始
    def open_spider(self, spider):
        # 爬虫项目启动，执行连接数据操作
        # 以下常量需要定义在settings配置文件中
        self.f = open('1.csv', 'a', newline='')
        self.writer = csv.writer(self.f)

    # 向表中插入数据
    def process_item(self, item, spider):
        L = [
            item['name'], item['star'], item['time']
        ]
        self.writer.writerow(L)
        return item

    # 结束存放数据，在项目最后一步执行
    def close_spider(self, spider):
        # close_spider()函数只在所有数据抓取完毕后执行一次，
        self.f.close()
        print('执行了close_spider方法,项目已经关闭')
