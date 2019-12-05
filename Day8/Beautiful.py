from bs4 import BeautifulSoup
import requests

html = requests.get("https://ithelp.ithome.com.tw/articles?tab=tech").text
soup = BeautifulSoup(html,'lxml')
#print(soup.prettify())

titles = soup.select_one("body > div.container.index-top > div > div > div.leftside > div.board.tabs-content > div:nth-child(2) > div.qa-list__content > h3 > a")
#print(title.text)


'''
titles =soup.select("html> body> div> div.row> div.col-md-12.clearfix> "+
                "div.leftside> div.board.tabs-content> div.qa-list> div.qa-list__content>"+
                " h3.qa-list__title>  a.qa-list__title-link")
'''
titles = soup.select("body > div.container.index-top > div > div > div.leftside > div.board.tabs-content > div > div.qa-list__content > h3 > a")
for title in titles:
    print(title.text)