import requests
import pprint
from bs4 import BeautifulSoup
import psycopg2
from datetime import datetime

hostname="localhost"
user="postgres"
db="Scrapy"
password="XXXX"

conn_String = f'host={hostname} user={user} dbname={db} password={password}'
conn = psycopg2.connect(conn_String)
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
    print("Finish Scrap Article.....")
    return articles

def ScrapContent(articles = ScrapArticle()):
    print("Start Scrap Content.....")
    data=[]
    for article in articles:
        contents={}
        res = requests.get(article["url"])
        soup = BeautifulSoup(res.text,'lxml')

        url = res.url

        header = soup.find("div",class_="qa-header")
        title = header.find("h2",class_="qa-header__title").get_text(strip=True)
        #標籤
        ts = header.find("div",class_="qa-header__tagGroup")    
        if ts != None:
            tags=[]
            ts = ts.find_all("a",class_="tag qa-header__tagList")
            for t in ts:
                tags.append(t.get_text(strip=True))



        try:
            #問題
            header_info = header.find("div",class_="qa-header__info")
            person = header_info.find("a",class_="qa-header__info-person").get_text(strip=True)
            time_text = header_info.find("a",class_="qa-header__info-time").get_text(strip=True)
            publish_time = datetime.strptime(time_text,"%Y-%m-%d %H:%M:%S")
        except:
            #鐵人賽
            header_info = header.find("div",class_="ir-article-info__content")
            person = header_info.find("a",class_="ir-article-info__name").get_text(strip=True)
            time_text = header_info.find("a",class_="qa-header__info-time ir-article-info__time").get_text(strip=True)
            publish_time = datetime.strptime(time_text,"%Y-%m-%d %H:%M:%S")


        #內文
        markdown = soup.find("div",class_="qa-panel__content")
        content = markdown.find("div",class_="markdown__style").get_text(strip=True)
        
        contents["title"] = title
        contents["url"]=url
        contents["author"] = person
        contents["publish_time"] = publish_time
        contents["tags"]=tags
        contents["content"] = content
        data.append(contents)

        Insertdb(contents)
    print("Finish Scrap Content.....")
    return data


    print("Finish Scrap Content.....")

def Insertdb(article):
    print("Start saving article to SQL.....")
    conn_cursor.execute('''
        INSERT INTO ithome_article (title,url,author,publish_time,tags,content)
        VALUES(%(title)s,%(url)s,%(author)s,%(publish_time)s,%(tags)s,%(content)s)
    ''', article)
    conn.commit()
    print("Finish saving article to SQL.....")

data = ScrapContent()

conn_cursor.close()
conn.close()
