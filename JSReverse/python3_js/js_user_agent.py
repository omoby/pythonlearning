import requests
from parsel import Selector

url = "http://www.porters.vip/verify/uas/index.html"

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36",
    }

response = requests.request("GET", url, headers=headers)
print(response.status_code)
if response.status_code == 200:
    sel = Selector(response.text)
    res  = sel.css('.list-group-item::text').extract()
    print(type(res))
    print(res)
    for sub in res:
        print(sub)
else:
    print('This request is fail')
# print(response.text)