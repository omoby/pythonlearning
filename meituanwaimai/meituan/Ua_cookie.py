#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-03-29 18:51
# @Author  : yangshilong
# @Site    : 
# @File    : Ua_cookie.py
# @Software: PyCharm
import redis

USER_AGNET = [
    "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 8.0.0; Pixel 2 XL Build/OPD1.170816.004) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Mobile Safari/537.36",
    "Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1",
]

COOKIE = [
'terminal=i; w_utmz="utm_campaign=(direct)&utm_source=5000&utm_medium=(none)&utm_content=(none)&utm_term=(none)"; au_trace_key_net=default; _lx_utm=utm_source%3D60066; _lxsdk_cuid=1725df80e52c8-0ee02626181dce-3f674604-144000-1725df80e53c8; iuuid=DE1FA9F1F929CABFBCF92D7A6C3E237FE04C5D967A2100F553A61D4CE72EAC9D; wm_order_channel=default; utm_source=; _lxsdk=DE1FA9F1F929CABFBCF92D7A6C3E237FE04C5D967A2100F553A61D4CE72EAC9D; openh5_uuid=DE1FA9F1F929CABFBCF92D7A6C3E237FE04C5D967A2100F553A61D4CE72EAC9D; uuid=DE1FA9F1F929CABFBCF92D7A6C3E237FE04C5D967A2100F553A61D4CE72EAC9D; openh5_uuid=DE1FA9F1F929CABFBCF92D7A6C3E237FE04C5D967A2100F553A61D4CE72EAC9D; service-off=0; w_actual_lat=404669471; w_actual_lng=1159889722; _ga=GA1.3.1782694322.1594089125; _gid=GA1.3.1224513689.1594089125; __mta=150779785.1594089127566.1594089127566.1594089127566.1; ci=30; rvct=30; userId=2724915169; w_latlng=39904667,116408198; w_visitid=d8c3a265-88dc-4617-b136-4bcc02cb49fc; token=zetuOLzvDHvB8LBm5bTrn0QEGdUAAAAAAQsAADatlj_mG-vdrSyb9nukG2m6LjaXy16Ju80vCdpunz8mQE0H-O19AhB5P5xFtH_N5Q; mt_c_token=zetuOLzvDHvB8LBm5bTrn0QEGdUAAAAAAQsAADatlj_mG-vdrSyb9nukG2m6LjaXy16Ju80vCdpunz8mQE0H-O19AhB5P5xFtH_N5Q; oops=zetuOLzvDHvB8LBm5bTrn0QEGdUAAAAAAQsAADatlj_mG-vdrSyb9nukG2m6LjaXy16Ju80vCdpunz8mQE0H-O19AhB5P5xFtH_N5Q; cssVersion=ed62e738; _lxsdk_s=1732865638b-bb5-f2b-d5a%7C2724915169%7C10; w_token=zetuOLzvDHvB8LBm5bTrn0QEGdUAAAAAAQsAADatlj_mG-vdrSyb9nukG2m6LjaXy16Ju80vCdpunz8mQE0H-O19AhB5P5xFtH_N5Q'
]


class MeiTuanSpiser(object):

    @staticmethod
    def process_cookie(cookie):
        """
        cookie test
        :param cookie:
        :return:
        """
        list_dt = cookie.split(';')
        cookie_dict = {}
        for item in list_dt:
            if item and '=' in item:
                print(item.strip().split('='))
                key = item.strip().split('=')[0]
                value = item.strip().split('=')[1]
                cookie_dict[key] = value
        return cookie_dict

    @staticmethod
    def mysql_config():
        """
        mysql config
        :return:
        """
        test = {
            "host": "127.0.0.1",
            "port": 3306,
            "user": "root",
            "password": "inspur",
            "db": "meituan",
        }
        return test

    @staticmethod
    def redis_config():
        redis_config = {
            'host': '127.0.0.1',
            'port': 6379,
            'db': 0,
        }
        return redis_config
