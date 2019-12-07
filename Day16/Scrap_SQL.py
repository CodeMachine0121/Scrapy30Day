from bs4 import BeautifulSoup
import requests
from datetime import datetime
import pprint
import psycopg2

hostname = "localhost"
dbname = "Scrapy"
password ="James.2019"
user="postgres"

conn_string = f'host={hostname} user={user} dbname={dbname} password={password}'
conn = psycopg2.connect(conn_string)
conn_cursor = conn.cursor()

def ScrapArticle():
    print("Start Scrap Article.....")
    articles=[]
    for i in range(1,11):
        url = f"https://ithelp.ithome.com.tw/articles?tab=tech&page={i}"
        res = requests.get(url).text
        soup = BeautifulSoup(res,"lxml")
        
        lists = soup.find_all("div",class_="qa-list")
        
        if len(lists) == 0:
            print("沒文章了")
            break
        
        for article in lists:
            Tags = {}
            art = article.find("a",class_="qa-list__title-link")
            Tags["title"] = art.get_text(strip=True)
            Tags["url"] = art["href"]

            articles.append(Tags)
        #print(articles)
    print("Finish Scrap Article.....")
    return articles

def ScrapResponse(articles=ScrapArticle()):
    print("Start Scrap article response.....")
    
    for article in articles:
        res = requests.get(article["url"])
        soup = BeautifulSoup(res.text,'lxml')

        left = soup.find("div",class_="leftside")
        panels = left.find_all("div",class_="qa-panel response clearfix")
        if len(panels)==0:
            print("文章:{",article["title"],"} 底下無留言")
            continue
        
        for panel in panels:
            header = panel.find("div",class_="ans-header")
            
            author = header.find("a",class_="response-header__person").get_text(strip=True)
            
            level = header.find("div",class_="ans-header__leveltime").get_text(strip=True).split("‧")[0]
            
            time_text = header.find("a",class_="ans-header__time").get_text(strip=True)
            publish_time = datetime.strptime(time_text, "%Y-%m-%d %H:%M:%S")

            response_markdown = panel.find("div", class_="response-markdown")
            content = response_markdown.find("div", class_="markdown__style").get_text(strip=True)
            #print(article["title"])
            response_Info = {
                'author':author,
                'level': level,
                'publish_time': publish_time,
                'content': content,
                'title':article["title"]
            }
            Insertdb(response_Info)
    print("Finish Scrap article response.....")



def Insertdb(article):
    print("Inserting data")
    conn_cursor.execute('''INSERT INTO ithome_response(author,level,publish_time,content,title) 
        VALUES(%(author)s,%(level)s,%(publish_time)s,%(content)s,%(title)s)
    ''', article)
    conn.commit()

ScrapResponse()
conn_cursor.close()
conn.close()