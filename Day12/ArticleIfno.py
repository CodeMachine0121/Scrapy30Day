from bs4 import BeautifulSoup
import requests
from datetime import datetime

r = requests.get("https://ithelp.ithome.com.tw/articles/10229275").text
soup = BeautifulSoup(r,'lxml')


header = soup.find('div',class_="qa-header")
article_info = header.find("div",class_="ir-article-info__content")

author = article_info.find("a",class_="ir-article-info__name").get_text(strip=True)
print("Author: ",author)
"""
team = article_info.find("a",class_="ir-article-info__team").get_text(strip=True)
print("Team: ",team)
"""
time = article_info.find("a",class_="qa-header__info-time ir-article-info__time").get_text(strip=True)
publish_time = datetime.strptime(time, '%Y-%m-%d %H:%M:%S')
print("Publish time: ",publish_time)

tags=[]
elements = header.find('div',class_="qa-header__tagGroup")
tags_element = elements.find_all("a",class_="tag qa-header__tagList")
for tag_element in tags_element:
    tags.append(tag_element.get_text(strip=True))
print("Tags: ",tags)


viewnum = article_info.find("div",class_="ir-article-info__view")
print("瀏覽人數: ",viewnum.get_text(strip=True))