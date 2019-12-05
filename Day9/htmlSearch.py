import requests
from bs4 import BeautifulSoup

res = requests.get("https://ithelp.ithome.com.tw/articles?tab=tech").text
soup = BeautifulSoup(res,'lxml')


articles = soup.find_all('div',class_='qa-list')

for article in articles:
    title = article.find('a',class_='qa-list__title-link')
    print(title.text)


