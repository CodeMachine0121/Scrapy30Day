import requests

res = requests.get("https://ithelp.ithome.com.tw/articles/10219024")

print("回應狀況: ",res.status_code)
print("回應標頭: ",res.headers['content-type'])
print("回應編碼: ",res.encoding)
print("回應內容:",res.text[:100])


