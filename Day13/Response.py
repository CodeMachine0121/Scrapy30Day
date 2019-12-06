import requests
from bs4 import BeautifulSoup
import pprint
from datetime import datetime

res = requests.get("https://ithelp.ithome.com.tw/questions/10196027")
soup = BeautifulSoup(res.text,'lxml')

left = soup.find("div",class_="leftside")

ans = left.find_all("div",class_="ans")
#抓回文者
author = []
time = []
for an in ans:
    content = an.find("div",class_="qa-panel__content")
    header = content.find("div",class_="ans-header")
    author.append(\
        header.find("a",class_="ans-header__person").get_text(strip=True)\
        )
for an in ans:
    content = an.find("div",class_="qa-panel__content")
    header = content.find("div",class_="ans-header")
    time_text = header.find("a",class_="ans-header__time").get_text(strip=True)        
    time.append(datetime.strptime(time_text, "%Y-%m-%d %H:%M:%S"))
text=[]
for an in ans:
    content = an.find("div",class_="qa-panel__content")
    markdown = content.find("div",class_="markdown__style")
    text.append(markdown.get_text(strip=True))
    
#pprint.pprint(author)
#pprint.pprint(time)
#pprint.pprint(text)

#結構化

results=[]
for an in ans:
    content = an.find("div",class_="qa-panel__content")
    header = content.find("div",class_="ans-header")

    result={}
    result["Author"] = header.find("a",class_="ans-header__person").get_text(strip=True)
    
    time_text = header.find("a",class_="ans-header__time").get_text(strip=True)
    result["Publish_Time"] = datetime.strptime(time_text, "%Y-%m-%d %H:%M:%S")

    markdown = content.find("div",class_="markdown__style")
    result["Content"] = markdown.get_text(strip=True)

    results.append(result)
pprint.pprint(results)