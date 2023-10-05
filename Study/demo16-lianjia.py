from lxml import etree
import requests

url = 'https://bj.lianjia.com/ershoufang/pg{}'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.62'
}

r_list = []

for page in range(1, 2):
    full_url = url.format(page)
    resp = requests.get(full_url, headers=headers)

    html = etree.HTML(resp.text)
    results = html.xpath('//*[@id="content"]/div[1]/ul/li')
    for result in results:
        item = {
            '楼层': result.xpath('.//div[@class="houseInfo"]/text()')[0].strip(),
            '区域': result.xpath('./div[1]/div[2]/div')[0].xpath('string(.)').replace(' ', ''),
            '总价': result.xpath('./div[1]/div[6]/div[1]/span/text()')[0].strip(),
            '单价': result.xpath('./div[1]/div[6]/div[2]/span/text()')[0].strip()
        }
        r_list.append(item)
        print(item)
