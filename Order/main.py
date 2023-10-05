import bs4

from settings import *

# print(requests.get(TEST_GET_URL, headers=DEFAULT_HEADERS).text)

url = 'https://m.fx361.com/news/2021/0407/8073230.html'

text = requests.get(url, headers=DEFAULT_HEADERS).text
soup = bs4.BeautifulSoup(text)
print(soup.text)
print(soup.find(By.CLASS_NAME, 'wz_content').text)