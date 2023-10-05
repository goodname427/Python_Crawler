import re

from Order.crawlerlib import *
import time

base_url = 'https://www.okcis.cn'
search_url = base_url + '/searched_old_iframe/'
headers = DEFAULT_HEADERS
headers[
    'Cookie'] = 'et4321=2023-04-06+20%3A14%3A14COOKIEITEMn13762871259COOKIEITEM119.39.96.41COOKIEITEM192.168.0.87COOKIEFIELD2023-04-06+20%3A07%3A38COOKIEITEMCOOKIEITEM119.39.96.41COOKIEITEM192.168.0.87; HMF_CI=5bf1abcc6abe3b555072f5dbb300bbe488243fca7277c5d4a5bc63ceeef38562896d85ca86884f4c22769463916e3655b6761cf3deb6c3ac04e00e4cf0a2bb430e; sessionInfoKey=bbd4be618b7feedf8682ef0878e43a42; PHPSESSID=im8oi7tbn37d9uae6cacpa6f02; et4321=2023-04-06+20%3A07%3A38COOKIEITEMCOOKIEITEM119.39.96.41COOKIEITEM192.168.0.87; cookieId=7DS4IGT1680782859000; Hm_lvt_b6ff6d574fb1848824f05f0662e8a0fc=1680769033,1680782859; EEAkIjcBEarJg=n13762871259; infopass=%2A11FBB914CE6914F90EE6FA4140D4F454A9FAD25B; Hm_lpvt_b6ff6d574fb1848824f05f0662e8a0fc=1680783242'
headers['Referer'] = 'https://www.okcis.cn/search/'
headers['Host'] = 'www.okcis.cn'
headers['Origin'] = 'https://www.okcis.cn'


def get_request_data(search_token, page):
    return {
        'result-search-type-input': 'jingdian',
        'result-class-type-form': 'old_net',
        'search-token': search_token,
        'result-keyword-and-include - type': 'part',
        'result-keyword-and-form': '%B1%B1%BE%A9',
        'result-keyword-or-include-type': 'part',
        'result-keyword-or-form': '',
        'result-content-type-form': '1',
        'result-auto-type-form': '1',
        'notKeyword': '',
        'search-time-type': '4',
        'search-start-time-input': '2023-01-06',
        'search-end-time-input': '2023-04-06',
        'page': page
    }


def get_search_token():
    # 获取search token
    text = requests.get('https://www.okcis.cn/search/', headers=headers).text
    return re.search(r'<input type="hidden" name="search-token" value="(.+?)"/>', text).group(1)


def search(page):
    text = requests.post(search_url, headers=headers, data=get_request_data(get_search_token(), page)).text
    soup = BeautifulSoup(text, 'lxml')
    tbody_tag = soup.find(class_='zblis_con_c_20160113').tbody
    i = 0
    for child in tbody_tag('tr'):
        print(child.find('a')['title'])
        break
        #get_data(child.find('a')['href'])



def get_data(url):
    url = base_url + url
    text = requests.get(url, headers=headers).text
    soup = BeautifulSoup(text, 'lxml')
    table_tag = soup.find(id='tables').table

    for child in table_tag.children:
        print(child.text)



def main():
    for i in range(1, 15):
        print(i)
        search(i)
    # /20230406-n3-20230406202427862323.html
    # /20230406-n2-20230406202422864842.html

if __name__ == '__main__':
    start = time.time()
    main()
    print('爬取完毕,耗时', time.time() - start, 's')
