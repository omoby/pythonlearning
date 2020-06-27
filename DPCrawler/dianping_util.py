# -*- coding:utf-8 -*-
import uuid
import time
def get_uuid():
    id = uuid.uuid1()
    tm = int(time.time())
    iuuid = str(id)+"."+str(tm)
    print(iuuid)
    return iuuid

def get_cookie(city_en_name,city_id):
    lxsdk_cuid = 'lxsdk_cuid='+'17115b17b3ec8-0ce6d033e7a434-6e52782d-144000-17115b17b3ec8'+';'
    lxsdk = '_lxsdk='+'17115b17b3ec8-0ce6d033e7a434-6e52782d-144000-17115b17b3ec8'+';'
    hc='_hc.v='+'c43e76d1-800b-eeec-d5d1-970df938af29.1585206885'+';'
    switch='switchcityflashtoast=1;'
    logan = 'logan_custom_report =;'
    lx_utm='_lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic;'
    source = 'source=m_browser_test_33;'
    dp_pwa_v = 'dp_pwa_v_='+'fe25b31c1e622e79b2c551c1b73fa76ba19c48e7'+';'
    view = 's_ViewType=10;'
    flash = 'm_flash2=1;'
    pvhistory='pvhistory="6L+U5ZuePjo8L2hvbmdrb25tZz46PDE1ODUzNzYwNTQ5NjFdX1s=";'
    hm='Hm_lvt_233c7ef5b9b2d3d59090b5fc510a19ce=1585293703,1585297544,1585297990,1585380183;'
    default = 'default_ab=citylist%3AA%3A1%7Cshop%3AA%3A6%7Cindex%3AA%3A3%7CshopList%3AA%3A5;'
    cy=3173;
    cityname ='cye={city_en_name};'
    cityid='cityid={city_id};'
    hm_l = 'Hm_lpvt_233c7ef5b9b2d3d59090b5fc510a19ce=1585561097;'
    ms = 'msource=default;'
    token = 'logan_session_token=='+'vlx9r0lnixj8l2m8gyjs'
get_uuid()