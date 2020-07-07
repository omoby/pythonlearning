def get_shop():
    import requests

    url = "https://i.waimai.meituan.com/openh5/poi/food"

    querystring = {"_": "1594025513261",
                   "X-FOR-WITH": "ltJI0w99KbJyjiPTLfeuz0H9rP7EWm92%2F%2FCsN1qHUsqOfcx%2BNHski8og40HzhnaoFUcVM5zzYwqJZ%2B8%2FO6DstMz7Cl5sbDvpyTmGCDXoIrYeCfyNDD5%2Ft9QPgLs71nVFtsWl1sL7lrDX1aUJgIMbt4aQX2WXBRtNBDOmkYaQbbTPqYDK0RZr7qKp4NYFlaYkXdwgGnbhBnfsDNEORgxj5g%3D%3D"}

    payload = "geoType=2&mtWmPoiId=891924182592802&dpShopId=-1&source=shoplist&skuId=&uuid=6380715355AE14B00A89CB58B703AE8B7B225A362A48E83E064FC01825F81709&platform=3&partner=4&originUrl=https%253A%252F%252Fh5.waimai.meituan.com%252Fwaimai%252Fmindex%252Fmenu%253FdpShopId%253D%2526mtShopId%253D891924182592802%2526utm_source%253D%2526channel%253Ddefault%2526source%253Dshoplist%2526initialLat%253D31.4891%2526initialLng%253D120.306289%2526actualLat%253D31.4891%2526actualLng%253D120.306289&riskLevel=71&optimusCode=10&wm_latitude=31489100&wm_longitude=120306289&wm_actual_latitude=31489100&wm_actual_longitude=120306289&openh5_uuid=6380715355AE14B00A89CB58B703AE8B7B225A362A48E83E064FC01825F81709&_token=eJzFkm2PmkAQx78LL3xzRmAXVExMowen8iTqgmLTNDyDwKKwINL0u5dLbS%252F3vkmTzc7Mb%252F6z2dnZH1S58akZy7AThh1STVBSM4odMaMxNaRI1Wd4gWMAz7NgwoMh5X1isN%252BGlFtaIjX7yvX5MSt8ewf7Pv4AHx7g%252BvWu2PQCKibkWs1oOuZHdyfJnWSUBwmpHTzyipz%252Bjeg8wX7Q0nmA6y%252F%252B9RAX140%252FH%252BTk6U0FVgAcOwW8AKYMGNQk%252F14VdekF84EXOxgH2dwPQqfOyODJq74ySyoySHBCEidTHTKH7Ijrj%252FqLcDRnATOCzBhMhYHj9bf6pHuST7L%252Bxf5FRywLeTgVBMj%252F12b6KeWon1Jv06d1npb8ibX%252Bs%252FRdV0mEey%252BQHyR9Y8uoW9hxSKsq3sDODvfbRSwmnLVU764LFFNC6GSGiijXDZxcLaQc8Y2%252FcajDTZg%252BTriAPimg2RjrVrKva0h7Z%252FlSGACHpXl73FpJ9rjdfYIkcSVHGO0urqnvDG8qR%252FdjEuvKbWeluu2dFGSy55O5POjhqtAc23qcVlZlO%252Ftl7Z79SDeOVr16zS4rTRGYo%252BiArG2X9spjFUNrEewYmLCGg8oD%252F5qYb0m5N5s0Qrp8xudxZr026PEimId2G6jCy2a8bUh2aTl44EAnw7RY1m%252FaSU0a%252F6Fq6%252Fw%252BThsP6yiJkKoo3ZrEW0%252BSrVyr0zjnFhcx1hZe1SobNZP9F8vNQO1Kkw3wgp3ryUYXdNcCaUqTVbIeSo6%252BsMVckmiGPAyaCXVEVk6tl1MvsAVGwscopsW6O18iY0OnyvrmQ%252BuF59aQW4qHIxCj%252BZz6%252BQsfVEVs&undefined="
    headers = {
        'Pragma': "no-cache",
        'Origin': "https://h5.waimai.meituan.com",
        'Accept-Encoding': "gzip, deflate, br",
        'Accept-Language': "zh-CN,zh;q=0.9",
        'User-Agent': "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Mobile Safari/537.36",
        'Content-Type': "application/x-www-form-urlencoded",
        'Accept': "application/json",
        'Cache-Control': "no-cache",
        'Referer': "https://h5.waimai.meituan.com/waimai/mindex/menu?dpShopId=&mtShopId=891924182592802&utm_source=&channel=default&source=shoplist&initialLat=31.4891&initialLng=120.306289&actualLat=31.4891&actualLng=120.306289",
        'Cookie': "_lxsdk_cuid=17258e9bdcdc8-035b6212353d98-3f674604-144000-17258e9bdcec8; _ga=GA1.3.147549955.1594021774; _gid=GA1.3.423744456.1594021774; PHPSESSID=2huep8pinvja6qbllf74f3i9v2; Hm_lvt_f66b37722f586a240d4621318a5a6ebe=1594021789; Hm_lpvt_f66b37722f586a240d4621318a5a6ebe=1594021789; __utma=211559370.1176947614.1594021789.1594021789.1594021789.1; __utmc=211559370; __utmz=211559370.1594021789.1.1.utmcsr=baidu|utmccn=baidu|utmcmd=organic|utmcct=zt_search; __mta=256621876.1594021776291.1594021855987.1594021868864.3; wm_order_channel=default; utm_source=; au_trace_key_net=default; terminal=i; w_utmz=utm_campaign = (direct) & utm_source = 5000 & utm_medium = (none) & utm_content = (none) & utm_term = (none); service-off=0; iuuid=6380715355AE14B00A89CB58B703AE8B7B225A362A48E83E064FC01825F81709; _lxsdk=6380715355AE14B00A89CB58B703AE8B7B225A362A48E83E064FC01825F81709; openh5_uuid=6380715355AE14B00A89CB58B703AE8B7B225A362A48E83E064FC01825F81709; uuid=6380715355AE14B00A89CB58B703AE8B7B225A362A48E83E064FC01825F81709; openh5_uuid=6380715355AE14B00A89CB58B703AE8B7B225A362A48E83E064FC01825F81709; userId=2724915169; channelType={%22default%22:%220%22}; w_visitid=51e61e94-c03d-421e-815e-85145d63265d; token=GSRXwDLy_CCZdBpKhsXiWXURTWQAAAAAAQsAAFKn6Qr1uxoVpu__QcUz2sS_sTfpFzpZd98Pnsu5iKvXePglL-mZpNSxZb2eGm6gTQ; mt_c_token=GSRXwDLy_CCZdBpKhsXiWXURTWQAAAAAAQsAAFKn6Qr1uxoVpu__QcUz2sS_sTfpFzpZd98Pnsu5iKvXePglL-mZpNSxZb2eGm6gTQ; oops=GSRXwDLy_CCZdBpKhsXiWXURTWQAAAAAAQsAAFKn6Qr1uxoVpu__QcUz2sS_sTfpFzpZd98Pnsu5iKvXePglL-mZpNSxZb2eGm6gTQ; w_token=GSRXwDLy_CCZdBpKhsXiWXURTWQAAAAAAQsAAFKn6Qr1uxoVpu__QcUz2sS_sTfpFzpZd98Pnsu5iKvXePglL-mZpNSxZb2eGm6gTQ; w_actual_lat=31489100; w_actual_lng=120306289; w_latlng=31489100,120306289; cssVersion=ed62e738; _lx_utm=utm_source%3D; _lxsdk_s=173231a0445-802-fc0-941%7C%7C176",
        'Connection': "keep-alive",
        'cache-control': "no-cache",
        'Postman-Token': "2b04667f-2035-41a2-bda7-79e4a59c520d"
    }

    response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

    print(response.text)


def main():
    get_shop()


if __name__ == '__main__':
    main()
