import requests
from bs4 import BeautifulSoup

# 爬取新闻列表
def get_news_list(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'html.parser')
    news_list = []
    for item in soup.select('li.ztlb'):
        title = item.select_one('a').text.strip()
        link = item.select_one('a')['href']

        # 链接拼接处理，如果以.开头则将.替换为 url
        if link.startswith('.'):
            link = url + link[2:]  

        date = item.select_one('span').text.strip()
        news_list.append({'title': title, 'link': link, 'date': date})
    return news_list


print(get_news_list('http://www.moa.gov.cn/xw/bmdt/'))

