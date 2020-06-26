import requests

def get_data():
    url = "http://www.glidedsky.com/level/web/crawler-font-puzzle-1"

    querystring = {"page":"1"}

    headers = {
        'Connection': "keep-alive",
        'Pragma': "no-cache",
        'Cache-Control': "no-cache",
        'Upgrade-Insecure-Requests': "1",
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36",
        'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        'Referer': "http://www.glidedsky.com/level/web/crawler-font-puzzle-1?page=1000",
        'Accept-Encoding': "gzip, deflate",
        'Accept-Language': "zh-CN,zh;q=0.9",
        'Cookie': "_ga=GA1.2.2067547305.1590482611; _gid=GA1.2.389776157.1590482611; Hm_lvt_020fbaad6104bcddd1db12d6b78812f6=1590482611,1590482694; footprints=eyJpdiI6Ik53OVhDRFwvSXhpWHFLNVFSd0pRcjZRPT0iLCJ2YWx1ZSI6InZmRVhyTlVsYlwvZGZwZGJyZWtta1lDWDBEVjQxeExCVUN5Zm0ybzFaalFlenRxOUhnVUQ5N1BTNUdUMXVUZ1BpIiwibWFjIjoiYWE5M2U1NmQxMzUxNDhiZWUwZDE4ZDEzN2I2OTY3NzdhNGFmZGFjMGMwZDAyYjQzOThjYmEyMjJlODJiNWQ2YyJ9; remember_web_59ba36addc2b2f9401580f014c7f58ea4e30989d=eyJpdiI6IjRST0tyY01XY1NLVHEwbnVxWXdCdVE9PSIsInZhbHVlIjoieXVzMldzNTAzdmcyZFdFSUlucWNLWEFQeE9MZUQwcFVLMXRLbzdicTRcL0c1VXlmSitWZkxNeTdqY2dCc2lGZkxXamU1b0hET0xnVG1zZENZTXBUZ2xzVVhzVzZqMnNVU0graTgwNXl6bVBjRVwvb2FxblhRVXN5N0l3UWlBK1VnMnVwcWM1Q3h6M1wvR01pM2RcL3hSeFRuZWVQR2lSaThIdlBMMzBtblhWYmJRVT0iLCJtYWMiOiJjZjc5MmY3NDkxMjBkY2UwYWQ1MWU1Mjc2ZTE1OWVhZGIxNjQ4M2E4OWM4MTg1OTQ4MWFjMjgyZGYwY2M0ZTIzIn0%3D; XSRF-TOKEN=eyJpdiI6IjVZdUs4ZFJYZE1ZSTBvVXI3UE1ZaFE9PSIsInZhbHVlIjoiWnlpM3MySzJEUk1iSldwS2EwV3lUTlhGbm14VUdDY2F1dTA1THhETjdGZzdESW5RYnpKMnJZcjhYbkQ1MnNYTyIsIm1hYyI6IjczYzA3OTY3NzYxOGE0YmVmNTU2YzlmMDRkZDg2MGYxYzQ0ZDhlZTFkMDZiMWU0MzA2Mjg5NjE0Y2U0ZjcyMTgifQ%3D%3D; glidedsky_session=eyJpdiI6Im5haFBHTUR5c0M1MHdQRXZWQTlraXc9PSIsInZhbHVlIjoiSjJOZ05WaSt0Um1SS05VWDVhK2YwTzVFeEJQXC9TMzRCWEgyaUhTU3pYdURkZ2RTRllKcE9Cdmc4Mm9PU3VCcHgiLCJtYWMiOiJjOWI1MTA0ZGRlN2E5MGJiNWJiOGRlNjgyNjQ5OGQxMmY3MDFiMzIzNzJkZjM3NjQ3ZTMzYzljMWJjZmZkYjg4In0%3D; Hm_lpvt_020fbaad6104bcddd1db12d6b78812f6=1590494682",
        'cache-control': "no-cache",
        'Postman-Token': "1289e3d5-f361-4df8-913c-2aab83caec26"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    text_data = response.text
    mappings = {'7': 2, '9': 3,'4': 4, '3': 1, '6': 5, '1': 8, '8': 6, '4': 7, '0': 9, '2': 0}




def main():
    get_data()
if __name__ == '__main__':
    main()