import random
import re
import time

import requests

from meituanwaimai.meituan.Ua_cookie import COOKIE


def _send_request(index, lat, long):
    url = "http://i.waimai.meituan.com/openh5/homepage/poilist?_={}".format(int(time.time()))
    form_data = {
        "startIndex": "{}".format(index),
        "wm_actual_latitude": "{}".format(lat),
        "wm_actual_longitude": "{}".format(long),
    }
    cookie = random.choice(COOKIE)
    print(cookie)
    old_lat = re.compile(r'w_actual_lat=(\d+)').findall(cookie)[0]
    old_lng = re.compile(r'w_actual_lng=(\d+)').findall(cookie)[0]
    cookie = cookie.replace(old_lat, str(lat))
    cookie = cookie.replace(old_lng, str(long))
    old_w_latlng = re.compile(r' w_latlng=(\d+,\d+);').findall(cookie)[0]
    cookie = cookie.replace(old_w_latlng, f'{lat},{long}')
    print(old_lat)
    print(cookie)
    print(old_w_latlng)
    headers = {
        "Cookie": cookie
    }


def main():
    _send_request(1, 2, 3)


if __name__ == '__main__':
    main()
