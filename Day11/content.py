from bs4 import BeautifulSoup
import requests

res = requests.get("https://ithelp.ithome.com.tw/articles/10229260")
soup = BeautifulSoup(res.text,'lxml')

content = soup.find("div",class_="markdown__style")

#print(content.text)

#官方推薦使用 get_text() 方便抓特殊字元 strip:把空白去掉
#print(content.get_text(strip=True))

#取得html標籤
print(content.decode_contents())
