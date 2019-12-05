import requests
import pprint
payload ={
    'name':'Rex',
    'topic':'python'
}

response = requests.post("https://httpbin.org/post",data=payload)

pprint.pprint(response.json())