import requests
from bs4 import BeautifulSoup
#page2 url = https://ithelp.ithome.com.tw/articles?tab=tech&page=2
for page in range(1,11):
    titles=[]
    url='https://ithelp.ithome.com.tw/articles?tab=tech&page='+str(page)
    r = requests.get(url).text
    soup = BeautifulSoup(r,'lxml')

    print(url)
    articles = soup.find_all('div',class_="qa-list")
    if len(articles)==0:
        print("沒有文章了@@")
        break
    for article in articles:
        title  = article.find("a",class_="qa-list__title-link")
        titles.append(title.text)
  
    print("Page: ",page)
    print("Titles:",titles)
    print("==================================================") 