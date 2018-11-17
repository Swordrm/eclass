from datetime import datetime
import requests
from bs4 import BeautifulSoup
from home.models import News
import django.utils.timezone
url = "http://jwc.shmtu.edu.cn/"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
# find = soup.find('p')
# print(type(find), find, find.name, find['class'])
# 数据库操作示例
# models.News.objects.create()
all_li = soup.find('div', id='marquee1').find('ul').find_all('li')
for li in all_li:
    a = li.find('a')
    if a is not None:
        new = {
            'title': a['title'],
            'source': url + a['href'],
            'public': 'jwc',
            'text': "待获取",
            'type': '教务新闻',
        }
        News.objects.create(**new)
        # print('标题：' + a['title'])
