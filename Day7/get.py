import requests

payload = {
    'search':"python",
    'tab':"question"
}
r = requests.get('https://ithelp.ithome.com.tw/search',params=payload)
print(r.url)

