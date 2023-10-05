import os
import time
from Order.crawlerlib import *
import re
from PyPDF2 import PdfReader

base_url = 'http://www.cninfo.com.cn/new'
query_url = base_url + '/hisAnnouncement/query'
download_url = base_url + '/announcement/download?bulletinId={}&announceTime='
json_url = base_url + '/data/szse_stock.json'
code_js = {}
headers = DEFAULT_HEADERS
headers[
    'Cookie'] = 'JSESSIONID=AAE1453F630AA6B1F4210E5A63AD86BF; insert_cookie=45380249; routeId=.uc2; _sp_id.2141=955470fa-166f-45ce-a836-4e520160c2fa.1680709622.4.1680754154.1680751410.50bbd71e-33f7-4cd6-8226-77da9289e460'
headers['Referer'] = 'http://www.cninfo.com.cn/new/commonUrl/pageOfSearch?url=disclosure/list/search&lastPage=index'
patterns = {
    '人工智能技术': re.compile(r'人工智能技术'),
    '区块链技术': re.compile(r'区块链技术'),
    '云计算技术': re.compile(r'云计算技术'),
    '大数据技术': re.compile(r'大数据技术'),
    '数字技术运用': re.compile(r'数字技术运用')
}


def get_request_data(page, year, start, code):
    return {
        'pageNum': page,
        'pageSize': '30',
        'column': 'szse',
        'tabName': 'fulltext',
        'plate': 'szcy',
        'stock': code,
        'searchkey': '{}年'.format(year),
        'secid': '',
        'category': 'category_ndbg_szsh',
        'trade': '',
        'seDate': '{}-01-01~{}-01-01'.format(start, start + 3),
        'sortName': '',
        'sortType': '',
        'isHLtitle': 'true'
    }


def get_all_code():
    global code_js
    code_js = json.loads(requests.get(json_url, headers=headers).text)
    # print(len(code_js['stockList']))


def get_code(_id):
    for stock in code_js['stockList']:
        if stock['code'] == _id:
            return stock['code'] + ',' + stock['orgId']


def get_data(code, year):
    # 判断是否已经下载
    filename = code + year.__str__() + '.pdf'

    # 搜索年报
    announcements = search_pdf(code, year, int(year))

    # 下载年报
    if announcements:
        for announcement in announcements:
            if '摘要' in announcement['announcementTitle']:
                continue

            download_pdf(announcement, filename)
            break

    # 提取关键字
    return get_key(filename)


def search_pdf(code, year, start=2010):
    if os.path.exists(code + year.__str__() + '.pdf'):
        return

    print('从{}年到{}年查询{}的{}年报'.format(start, start + 3, code, year))
    js = json.loads(requests.post(query_url, headers=headers, data=get_request_data(1, year, start, code)).text)
    if not js or not js['announcements']:
        if start <= 2018:
            return search_pdf(code, year, start + 3)
        else:
            print('没有找到数据')
            return None

    return js['announcements']


def download_pdf(announcement, filename):
    if os.path.exists(filename):
        return

    print('下载', announcement['secName'], announcement['shortTitle'])
    save_content(requests.get(download_url.format(announcement['announcementId'])).content, filename)


def get_key(filename):
    if not os.path.exists(filename):
        return {key: '' for key in patterns}

    print('获取 {} 关键字'.format(filename))
    with open(filename, "rb") as f:
        pdf = PdfReader(f)
        content = ''
        for page in pdf.pages:
            page_content = page.extract_text()
            if page_content:
                content += page_content

        counts = {key: len(patterns[key].findall(content)) for key in patterns}
        print(counts)
        return counts


def handle_data(_row):
    if 'id' in _row[0]:
        return

    _code = get_code(_row[0])

    if not _code:
        print('未查询到代码')
        return

    data = {'id': _row[0], 'year': _row[1]}
    new = get_data(_code, _row[1])
    if new:
        data = dict(**data, **new)
    writer.writerow(data)


if __name__ == '__main__':
    begin = time.time()

    # 获取所有代码
    get_all_code()

    with open('data.csv', 'r', newline='', encoding='utf-8') as rf:
        with open('1.csv', 'w', newline='') as wf:
            writer = csv.DictWriter(wf, ['id', 'year'] + [key for key in patterns])
            writer.writeheader()
            reader = csv.reader(rf)

            for row in reader:
                handle_data(row)

    print('爬取完毕,耗时', time.time() - begin, 's')
