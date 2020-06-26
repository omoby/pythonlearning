import requests
import re

def get_data():
    url = "http://www.glidedsky.com/level/web/crawler-basic-1"

    headers = {
        'Connection': "keep-alive",
        'Pragma': "no-cache",
        'Cache-Control': "no-cache",
        'Upgrade-Insecure-Requests': "1",
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36",
        'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        'Referer': "http://www.glidedsky.com/level/crawler-basic-1",
        'Accept-Encoding': "gzip, deflate",
        'Accept-Language': "zh-CN,zh;q=0.9",
        'Cookie': "_ga=GA1.2.2067547305.1590482611; _gid=GA1.2.389776157.1590482611; footprints=eyJpdiI6IlZ3WktUYlRveEJUWW51Q1BDUWxNeEE9PSIsInZhbHVlIjoiQ0ZMankrNmFFQm9EU0JqblFnK2krRCt1TUhxeE9qTTNSNnVmWDZPZzZ2cjhrSjN6dXA4dTB6anRpNE5OZXladCIsIm1hYyI6ImZjNjFhN2ZmMDM1ZWM5MzVmYmJiMjU5ZWI1NTk5ZjdiZmE1MTMxMDAyZTllYWRjNDk1NjE5Nzk2N2Y5ZDZkNjMifQ%3D%3D; Hm_lvt_020fbaad6104bcddd1db12d6b78812f6=1590482611,1590482694; XSRF-TOKEN=eyJpdiI6ImY2Z2JJejdpK2dxWXd3dXVpY1dLZnc9PSIsInZhbHVlIjoiMmREWjd0d2FXVDNqc0pqSE5cLzE2ajZTUDExWm5ObTVHUnF3WVRcL0ZHbmlxaGpVVDVKeEtBOWhieXVcL3RMUmFYciIsIm1hYyI6IjY4YmI1Y2Q2NzNiODIwZDRhMmY2MTU1YjY2NDg5YWRmMjBmODRlNGE4NDVlYTI2ZmU5MzlhNjRiMTVjZTk5NjkifQ%3D%3D; glidedsky_session=eyJpdiI6IjNOdUk3RThIY1BnUGFxd1drdndLTFE9PSIsInZhbHVlIjoiSFRFXC9OZzJlZXRodGx6Wll1TzdoV0wxYllyQW1Cdm1zeGFLaFwvWGt6SkRCeEpKa1R1bDZpRlZsN1dZemE3YUtHIiwibWFjIjoiZDYyYTlhOTk5NTk2YTQwYTM5OGQ1YWU5NzAyNzJiODBlZTI2MjE2MjU5ZTg3ZjE3ZDIxMjI0YmFmNTQ1ZTY3NyJ9; Hm_lpvt_020fbaad6104bcddd1db12d6b78812f6=1590483041; _gat_gtag_UA_75859356_3=1",
        'cache-control': "no-cache",
        'Postman-Token': "b1a2e146-c4b7-4692-ace2-aa305ccdda3c"
        }

    response = requests.request("GET", url, headers=headers)

    data_text = response.text
    pat = r'<div class="col-md-1">\s*(\d+)\s*</div>'
    re_data = re.compile(pat).findall(data_text)
    total = 0
    for data in re_data:
        data = int(data)
        total += data
    print(total)


def main():
    get_data()
if __name__ == '__main__':
    main()