from scrapy import cmdline

# 执行爬虫文件 -o 指定输出文件的格式
cmdline.execute('scrapy crawl maoyan -o maoyan.csv'.split())  # 执行项目，并且将数据存csv文件格式
