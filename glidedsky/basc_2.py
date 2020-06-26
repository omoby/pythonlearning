import re

import requests

def get_data(page_num):

    url = "http://www.glidedsky.com/level/web/crawler-basic-2"

    querystring = {"page": page_num}

    headers = {
        'Connection': "keep-alive",
        'Pragma': "no-cache",
        'Cache-Control': "no-cache",
        'Upgrade-Insecure-Requests': "1",
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36",
        'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        'Referer': "http://www.glidedsky.com/level/web/crawler-basic-2",
        'Accept-Encoding': "gzip, deflate",
        'Accept-Language': "zh-CN,zh;q=0.9",
        'Cookie': "_ga=GA1.2.2067547305.1590482611; _gid=GA1.2.389776157.1590482611; footprints=eyJpdiI6IlZ3WktUYlRveEJUWW51Q1BDUWxNeEE9PSIsInZhbHVlIjoiQ0ZMankrNmFFQm9EU0JqblFnK2krRCt1TUhxeE9qTTNSNnVmWDZPZzZ2cjhrSjN6dXA4dTB6anRpNE5OZXladCIsIm1hYyI6ImZjNjFhN2ZmMDM1ZWM5MzVmYmJiMjU5ZWI1NTk5ZjdiZmE1MTMxMDAyZTllYWRjNDk1NjE5Nzk2N2Y5ZDZkNjMifQ%3D%3D; Hm_lvt_020fbaad6104bcddd1db12d6b78812f6=1590482611,1590482694; _gat_gtag_UA_75859356_3=1; XSRF-TOKEN=eyJpdiI6Ikw1OWI2YlpFVDdNUkczWE0wR3IrdGc9PSIsInZhbHVlIjoiZ3BpWThTRkZ4c0N2dUNLeDA3OWF0S1wvNElMOGFmOUt6WDNhcWlXUWJSYzdtZWRTb1wvdm5VWWJDVmsyc0NxWHRpIiwibWFjIjoiODY0YTgwMDZjZTQzZjA4MjhlY2ExMjQxMjUxYmY2NTc1ZTQ0YTNmNzQ3ODY0NjA0NDlmMGIxNzBiMWViMDU4ZSJ9; glidedsky_session=eyJpdiI6InNwclQyTXNpd0lSQThoc2JrOG9cL1RRPT0iLCJ2YWx1ZSI6Ilh5Qk5sd2krODAyRHFGRXV2NFVMb0p4SmE0NVk4enBkNXRhOWowcWdGOVRMSDM2XC9Sb2k4NTgyT2dRdXNOc1Y1IiwibWFjIjoiNWM1Zjg1NDQ3Nzc2YTA3YmY4OWI4YTkxOWEwMmZiN2YwMWM0NWU2ZmE4OTNiM2IxMmJhMzcxMWIyYjY5MmZjOCJ9; Hm_lpvt_020fbaad6104bcddd1db12d6b78812f6=1590484123",
        'cache-control': "no-cache",
        'Postman-Token': "5893c593-526e-4ae9-a9b0-578deee115f7"
    }
    if page_num == 1:
        response = requests.request("GET", url, headers=headers)
    else:
        response = requests.request("GET", url, headers=headers, params=querystring)

    data_text = response.text
    pat = r'<div class="col-md-1">\s*(\d+)\s*</div>'
    re_data = re.compile(pat).findall(data_text)
    return re_data



def main():
    index = 1
    total = 0
    while index <= 1000:
        data = get_data(index)
        for sub in data:
            sub_int = int(sub)
            total += sub_int
        index += 1
    print(total)
if __name__ == '__main__':
    main()