

import requests
from lxml import etree

url = "http://www.porters.vip/verify/cookie/content.html"

headers = {
    'Cookie': 'isfirst=789kq7uc1pp4c'
    }

response = requests.request("GET", url, headers=headers)
response.encoding = 'utf-8'
# print(response.text)
print(response.status_code)
if response.status_code == 200:
    html = etree.HTML(response.text)
    res = html.cssselect('.page-header h1')[0].text
    print(res)
else:
    print('This request is fail.')
# print(response.text)