import requests

url = "https://i.waimai.meituan.com/openh5/homepage/poilist"

querystring = {"_": "1594090962818",
               "X-FOR-WITH": "%2F94HsBK4tenCEjakqImet4U4WatnGTWtzYKP8OCnNLfy0LL3%2Ffni6oqA8u1Kure9oE1%2BJPWJzDB%2FaVFaNj%2FWsRJ%2Bp99SJ684IEDEK4fbAVif4ccDHUokFdL2RLR%2FcOR2kf7XUfoumyRUUsR59mk%2BFtQrmBJ6jOchOHyKDI8TzKnd7Lt77oxU7IIplZedqZcwAUJQQGgavfdicvc19GtXYA%3D%3D"}

payload = "startIndex=1&sortId=0&multiFilterIds=&sliderSelectCode=&sliderSelectMin=&sliderSelectMax=&geoType=2&rankTraceId=&uuid=DE1FA9F1F929CABFBCF92D7A6C3E237FE04C5D967A2100F553A61D4CE72EAC9D&platform=3&partner=4&originUrl=https%253A%252F%252Fh5.waimai.meituan.com%252Fwaimai%252Fmindex%252Fhome&riskLevel=71&optimusCode=10&wm_latitude=404669471&wm_longitude=1168429388&wm_actual_latitude=403762364&wm_actual_longitude=117051981&openh5_uuid=DE1FA9F1F929CABFBCF92D7A6C3E237FE04C5D967A2100F553A61D4CE72EAC9D&_token=eJx9UGuPmkAU%252FS8k2y8aZxgExWTTgCgguuyCyqNtmuEhDwVWHBDZ9L937G6y%252FdA0ucm5cx65J%252FPG1HrEzFjITiA7ZNq4ZmYMO4IjgRky5EIVXhxDEYo8ghM0ZMK%252FOQFNWWHIBPVeYWbfxjwa8qLw405Y9P1JfG5oTOfu0KmBSQl5vcwASPnRFWcFzkZFnJEGl6OwKsA7BYqsjOIOpFUR00r%252Fj5yqJCu%252FHqo6jB9J3cRfAhwefzb16fFP7oGTHtCSzj%252FTlH8n6fJ%252B9O68n6WFiy0tTPF4R%252BZ7AyGLhrKpeHcRf4jkA%252FGGfiIte8mSkm7x6kaOC7ZNemmTtmCt5IWzkqX5kTMSCVsGQmXUeLVksFqf7FZeww0AUViIuOPACcV6MHHFSLIB4F%252FlnWq5C85pt559VbtYBlLXeFXEsvipMkWdi3ZAKAi%252BoYMfFIHhPAnuxuTrvr2YS19lo2nl2bnWqtOzdwzsxWRbE5UtIF7W%252B2g5OGkL6SXXgGU1IEo6eZu3Slei8AX5gkNgelmb54kRvPjtpW%252BNWvNyd71eOXDez8lSXkgOzr3q8HzKrEpQQmyBnbQmVmXMXXgl0yRVw2rjVotQD1Q5z%252FoDdOO94z7D%252BUTWbjq2ZNWGXdEIDaebKdBKFcm9cxxMr2ngT82t1Z788MRbXnMoyoPWwETvxv1uGRTnvPPt%252Fbz0lC1%252FNkK%252Bu9rtTZRQg%252F1IY379BvmF6e4%253D&undefined="
headers = {
    'Pragma': "no-cache",
    'Origin': "https://h5.waimai.meituan.com",
    'Accept-Encoding': "gzip, deflate, br",
    'Accept-Language': "zh-CN,zh;q=0.9",
    'User-Agent': "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Mobile Safari/537.36",
    'Content-Type': "application/x-www-form-urlencoded",
    'Accept': "application/json",
    'Cache-Control': "no-cache",
    'Referer': "https://h5.waimai.meituan.com/waimai/mindex/home",
    'Connection': "keep-alive",
    'cache-control': "no-cache",
    'Postman-Token': "282a8e1b-228d-4f9a-bae1-26d371f20db6",
    'Cookie': 'terminal=i; w_utmz="utm_campaign=(direct)&utm_source=5000&utm_medium=(none)&utm_content=(none)&utm_term=(none)"; au_trace_key_net=default; _lx_utm=utm_source%3D60066; _lxsdk_cuid=1725df80e52c8-0ee02626181dce-3f674604-144000-1725df80e53c8; iuuid=DE1FA9F1F929CABFBCF92D7A6C3E237FE04C5D967A2100F553A61D4CE72EAC9D; wm_order_channel=default; utm_source=; _lxsdk=DE1FA9F1F929CABFBCF92D7A6C3E237FE04C5D967A2100F553A61D4CE72EAC9D; openh5_uuid=DE1FA9F1F929CABFBCF92D7A6C3E237FE04C5D967A2100F553A61D4CE72EAC9D; uuid=DE1FA9F1F929CABFBCF92D7A6C3E237FE04C5D967A2100F553A61D4CE72EAC9D; openh5_uuid=DE1FA9F1F929CABFBCF92D7A6C3E237FE04C5D967A2100F553A61D4CE72EAC9D; service-off=0; w_actual_lat=116400000; w_actual_lng=39900000; _ga=GA1.3.1782694322.1594089125; _gid=GA1.3.1224513689.1594089125; __mta=150779785.1594089127566.1594089127566.1594089127566.1; w_latlng=116400000,39900000; userId=268898875; w_visitid=8235291a-29e6-4312-bf94-14c08ed188ef; token=aMg8Z0UtMb0dB_UklWuA8N8a7EwAAAAAAQsAAKjKbTHOi4ie7zl0iBM2igSwi5XwOtjo0jlmqeeM68iZTCf1ivfCQXW9uM4A6S2h3w; mt_c_token=aMg8Z0UtMb0dB_UklWuA8N8a7EwAAAAAAQsAAKjKbTHOi4ie7zl0iBM2igSwi5XwOtjo0jlmqeeM68iZTCf1ivfCQXW9uM4A6S2h3w; oops=aMg8Z0UtMb0dB_UklWuA8N8a7EwAAAAAAQsAAKjKbTHOi4ie7zl0iBM2igSwi5XwOtjo0jlmqeeM68iZTCf1ivfCQXW9uM4A6S2h3w; cssVersion=6c38b92f; _lxsdk_s=173275655ff-406-964-fa4%7C268898875%7C9; w_token=aMg8Z0UtMb0dB_UklWuA8N8a7EwAAAAAAQsAAKjKbTHOi4ie7zl0iBM2igSwi5XwOtjo0jlmqeeM68iZTCf1ivfCQXW9uM4A6S2h3w'
}

response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

print(response.text)
