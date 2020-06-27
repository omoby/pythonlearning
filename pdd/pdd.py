import json
import random
import urllib

import requests
import re

from DPCrawler.config import PROXY_POOL
from DPCrawler.setting import USER_AGENTS

session = requests.Session()

def get_agent_proxies():
    user_agent = random.choice(USER_AGENTS)
    proxy_ip = urllib.request.urlopen(PROXY_POOL).read().decode("utf-8").split("\n")[1]
    # print(proxy_ip)
    if ',' in proxy_ip:
        proxy_ip = proxy_ip.split(',')[0]
        # print(proxy_ip)
    if 'http' in proxy_ip:
        proxy_ip = proxy_ip.split('//')[1]
        # print(proxy_ip)
    proxy = {'https': proxy_ip, 'http': proxy_ip}
    return (user_agent,proxy)
def get_index_page():

    url = "http://yangkeduo.com/index.html"

    querystring = {"refer_page_name":"search","refer_page_id":"10031_1588985246715_og81tzcxf5","refer_page_sn":"10031"}

    headers = {
        # 'Pragma': "no-cache",
        'Cookie': "api_uid=CiS3B164rm0mbwBMNbhcAg==; _nano_fp=XpdJlpgjXpdJX5PqX9_awQm1oGHUOHEiS27K3F46; PDDAccessToken=XQNXEKAOYSLWJHX3QUAI5SYN5VOPSABQUZ7H6PHF7JWDKEYAXLEA1111969; pdd_user_id=1058890491161; pdd_user_uin=3R4Z7KFL26WAV6UGMP4YJ3Q76A_GEXDA; ua=Mozilla%2F5.0%20(Linux%3B%20Android%206.0%3B%20Nexus%205%20Build%2FMRA58N)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F70.0.3538.102%20Mobile%20Safari%2F537.36; webp=1; JSESSIONID=B9530552A283730DF428868E36CE87A7",
        # 'Accept-Encoding': "gzip, deflate",
        # 'Accept-Language': "zh-CN,zh;q=0.9",
        'User-Agent': "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Mobile Safari/537.36",
        # 'Accept': "image/webp,image/apng,image/*,*/*;q=0.8",
        # 'Cache-Control': "no-cache",
        # 'Referer': "http://yangkeduo.com/index.html?refer_page_name=search&refer_page_id=10031_1588985246715_og81tzcxf5&refer_page_sn=10031",
        # 'Proxy-Connection': "keep-alive",
        # 'cache-control': "no-cache",
        # 'Postman-Token': "4d703b0b-83f0-4962-bf2e-e439b1775cd3"
        }

    response = session.request("GET", url, headers=headers, params=querystring)
    #
    # print(response.text)
    pat_window_data = r'({"store".*?null}})'
    data = re.compile(pat_window_data).findall(response.text)[0]
    json_data = json.loads(data)
    print(json_data)


def get_classification_page():

    url = "http://yangkeduo.com/classification.html"

    querystring = {"refer_page_name": "index", "refer_page_id": "10002_1589164931239_ffx5irqk3n",
                   "refer_page_sn": "10002"}

    headers = {
        'Connection': "keep-alive",
        'Pragma': "no-cache",
        'Cache-Control': "no-cache",
        'Upgrade-Insecure-Requests': "1",
        'User-Agent': "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Mobile Safari/537.36",
        'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        'Referer': "http://yangkeduo.com/index.html?refer_page_name=search&refer_page_id=10031_1588985246715_og81tzcxf5&refer_page_sn=10031&list_id=vpIFwh2oic&page_id=10002_1589164931239_ffx5irqk3n&is_back=1",
        'Accept-Encoding': "gzip, deflate",
        'Accept-Language': "zh-CN,zh;q=0.9",
        'Cookie': "api_uid=CiS3B164rm0mbwBMNbhcAg==; _nano_fp=XpdJlpgjXpdJX5PqX9_awQm1oGHUOHEiS27K3F46; PDDAccessToken=XQNXEKAOYSLWJHX3QUAI5SYN5VOPSABQUZ7H6PHF7JWDKEYAXLEA1111969; pdd_user_id=1058890491161; pdd_user_uin=3R4Z7KFL26WAV6UGMP4YJ3Q76A_GEXDA; ua=Mozilla%2F5.0%20(Linux%3B%20Android%206.0%3B%20Nexus%205%20Build%2FMRA58N)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F70.0.3538.102%20Mobile%20Safari%2F537.36; webp=1; JSESSIONID=B9530552A283730DF428868E36CE87A7",
        'cache-control': "no-cache",
        'Postman-Token': "699c3fa1-c2a2-4260-8ee9-df8ca87afe18"
    }

    response = session.request("GET", url, headers=headers, params=querystring)
    # print(response.text)
    pat_window_data = r'window.rawData=(.*?);\s*</script>'
    data = re.compile(pat_window_data).findall(response.text)[0]
    json_data = json.loads(data)
    print(json_data)
    # root_items =  json_data.get('store').get('data').get('rootItems')
    # index = 0
    # for sub_list in root_items:
    #     if index == 0:
    #         index += 1
    #     else:
    #         print(sub_list)
    #         print(type(sub_list))

def get_catgoods_page():

    url = "http://yangkeduo.com/search_catgoods.html"

    querystring = {"opt_id": "9498", "opt1_id": "9490", "opt2_id": "999999", "opt_g": "1", "opt_type": "3",
                   "opt_name": "%E5%A5%B3%E8%A3%85T%E6%81%A4", "_x_link_id": "8d9100d3-4dd0-477e-bbd1-112048753cb7",
                   "_x_goods_id": "87799715295", "refer_page_name": "search",
                   "refer_page_id": "10031_1589170989878_ocxrxkeq6m", "refer_page_sn": "10031"}

    headers = {
        'Connection': "keep-alive",
        'Pragma': "no-cache",
        'Cache-Control': "no-cache",
        'Upgrade-Insecure-Requests': "1",
        'User-Agent': "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Mobile Safari/537.36",
        'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        'Referer': "http://yangkeduo.com/classification.html?refer_page_name=search&refer_page_id=10031_1589162944328_7aq63wtucu&refer_page_sn=10031&page_id=10031_1589170989878_ocxrxkeq6m&is_recover=1&is_back=1",
        'Accept-Encoding': "gzip, deflate",
        'Accept-Language': "zh-CN,zh;q=0.9",
        'Cookie': "api_uid=CiS3B164rm0mbwBMNbhcAg==; _nano_fp=XpdJlpgjXpdJX5PqX9_awQm1oGHUOHEiS27K3F46; PDDAccessToken=XQNXEKAOYSLWJHX3QUAI5SYN5VOPSABQUZ7H6PHF7JWDKEYAXLEA1111969; pdd_user_id=1058890491161; pdd_user_uin=3R4Z7KFL26WAV6UGMP4YJ3Q76A_GEXDA; ua=Mozilla%2F5.0%20(Linux%3B%20Android%206.0%3B%20Nexus%205%20Build%2FMRA58N)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F70.0.3538.102%20Mobile%20Safari%2F537.36; webp=1; JSESSIONID=A98C587FFA554E158C356851E219FBD1",
        'cache-control': "no-cache",
        'Postman-Token': "0ed95145-960f-4212-9a88-75932452b480"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    # print(response.text)
    # print(response.text)
    pat_window_data = r'({"store".*?null}})'
    data = re.compile(pat_window_data).findall(response.text)[0]
    json_data = json.loads(data)
    print(json_data)

def  get_group_data():

    url = "http://yangkeduo.com/proxy/api/api/search/opt/9498/groups"

    querystring = {"pdduid": "1058890491161", "source": "search", "opt_type": "3",
                   "white_ground_pic_goods_id": "87799715295",
                   "flip": "20%3B4%3B0%3B0%3B879729f8-5651-49e0-a540-ded6f3cc6680", "offset": "20", "count": "20",
                   "list_id": "0L2732Mz0s", "sort": "default", "filter": "",
                   "anti_content": "0aoAfaOdOscYq9duv8TV29QhQB9d0_w1eQzagLZaBk1d01vpAc30pDg8ZPMuVhpfgLpwB889qqooUWoQRoGQo2KOomArPQQQukbNyaGKNX29QJ47vZhjUhgM_uoQhjpyM7bqIE8hf5nKzZYFA5m7UKAfz-dr61-OvVkkeyML8vewYSX-XWSTvh5wJtjan-w8uM_k0D9l3o8KwxJcLGCcwxEPjtBa2x3bSZkSzO_m-clWfnZXRTlSMzd1zti6ddsooCfOirfCWKAgXVi69hmaNV26CjP-rp2vINDDNmT2Pos-0ZX6swxt1cSb0QbEQIo-8iWjJejhPH50X2q-tvu96NjTAm6jPuthHgXiYgLgnB9A1yV6aQtmP9EPJwVH9Wpc9cA9W9zbK-2ftPifVbxKI_vmAPLCF6-c5Bzh-TPQPzGKGnKJe38H9W7ZNDOnRClkRFOScNvFMBDzX5S7kZZzwrDE_g1IEpVzi5EcfpIe-UTENZSpnZppxBVFJuBzfkeR4G5HkKOJCkz3acNruMOblGPxnwmB1mx-AO0Jx_Ou4LO9sMPmSFGGEomE3f5FdM5VUNbKw3Low6mG6O8Kp5QxOM7Gu3w3rduZR51EJLy3uMM1LlwcMB4HWh2j31DiF6nuP6gAdsBlIcnSSvcgMJw7rdb_rWn3M1XY1evvNQAWylze6xbvsQvaUqKEVmxr2tzqTcX4tdXATa56JQ7U0AhpO_nlr_ividS5yW0xzzmfcsHXQCGmshwcT",
                   "opt_source": "search_opt_goods"}

    headers = {
        'Pragma': "no-cache",
        'Accept-Encoding': "gzip, deflate",
        'Accept-Language': "zh-CN,zh;q=0.9",
        'User-Agent': "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Mobile Safari/537.36",
        'VerifyAuthToken': "2bofYmt-s3AKrmb4hLnDig",
        'Accept': "application/json, text/plain, */*",
        'Cache-Control': "no-cache",
        'AccessToken': "XQNXEKAOYSLWJHX3QUAI5SYN5VOPSABQUZ7H6PHF7JWDKEYAXLEA1111969",
        'Cookie': "api_uid=CiS3B164rm0mbwBMNbhcAg==; _nano_fp=XpdJlpgjXpdJX5PqX9_awQm1oGHUOHEiS27K3F46; PDDAccessToken=XQNXEKAOYSLWJHX3QUAI5SYN5VOPSABQUZ7H6PHF7JWDKEYAXLEA1111969; pdd_user_id=1058890491161; pdd_user_uin=3R4Z7KFL26WAV6UGMP4YJ3Q76A_GEXDA; ua=Mozilla%2F5.0%20(Linux%3B%20Android%206.0%3B%20Nexus%205%20Build%2FMRA58N)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F70.0.3538.102%20Mobile%20Safari%2F537.36; webp=1; JSESSIONID=B54A0BE4AA46348E3D920EC663784DBD",
        'Connection': "keep-alive",
        'Referer': "http://yangkeduo.com/search_catgoods.html?opt_id=9498&opt1_id=9490&opt2_id=999999&opt_g=1&opt_type=3&opt_name=%E5%A5%B3%E8%A3%85T%E6%81%A4&_x_link_id=8d9100d3-4dd0-477e-bbd1-112048753cb7&_x_goods_id=87799715295&refer_page_name=search&refer_page_id=10031_1589170989878_ocxrxkeq6m&refer_page_sn=10031",
        'cache-control': "no-cache",
        'Postman-Token': "7116459e-aaf1-474c-8133-7a59245713ba"
    }

    response = session.request("GET", url, headers=headers, params=querystring)

    print(response.json())
def get_stm_page():
    # import requests

    url = "http://yangkeduo.com/proxy/api/api/server/_stm"

    querystring = {"pdduid": "1058890491161"}

    headers = {
        'Pragma': "no-cache",
        'Accept-Encoding': "gzip, deflate",
        'Accept-Language': "zh-CN,zh;q=0.9",
        'User-Agent': "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Mobile Safari/537.36",
        'VerifyAuthToken': "2bofYmt-s3AKrmb4hLnDig",
        'Accept': "application/json, text/plain, */*",
        'Cache-Control': "no-cache",
        'AccessToken': "XQNXEKAOYSLWJHX3QUAI5SYN5VOPSABQUZ7H6PHF7JWDKEYAXLEA1111969",
        'Cookie': "api_uid=CiS3B164rm0mbwBMNbhcAg==; _nano_fp=XpdJlpgjXpdJX5PqX9_awQm1oGHUOHEiS27K3F46; PDDAccessToken=XQNXEKAOYSLWJHX3QUAI5SYN5VOPSABQUZ7H6PHF7JWDKEYAXLEA1111969; pdd_user_id=1058890491161; pdd_user_uin=3R4Z7KFL26WAV6UGMP4YJ3Q76A_GEXDA; ua=Mozilla%2F5.0%20(Linux%3B%20Android%206.0%3B%20Nexus%205%20Build%2FMRA58N)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F70.0.3538.102%20Mobile%20Safari%2F537.36; webp=1; JSESSIONID=A98C587FFA554E158C356851E219FBD1",
        'Connection': "keep-alive",
        'Referer': "http://yangkeduo.com/search_catgoods.html?opt_id=9498&opt1_id=9490&opt2_id=999999&opt_g=1&opt_type=3&opt_name=%E5%A5%B3%E8%A3%85T%E6%81%A4&_x_link_id=8d9100d3-4dd0-477e-bbd1-112048753cb7&_x_goods_id=87799715295&refer_page_name=search&refer_page_id=10031_1589170989878_ocxrxkeq6m&refer_page_sn=10031",
        'cache-control': "no-cache",
        'Postman-Token': "0b7605ab-ac79-4634-b716-e23cee5e1e91"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    # print(response.text)
    # print(response.text)
    pat_window_data = r'({"store".*?null}})'
    data = re.compile(pat_window_data).findall(response.text)[0]
    json_data = json.loads(data)
    print(json_data)
def get_page_1():
    # import requests

    url = "http://cmtw.pinduoduo.com/api/page"

    headers = {
        'Access-Control-Request-Method': "POST",
        'Origin': "http://yangkeduo.com",
        'Referer': "http://yangkeduo.com/search_catgoods.html?opt_id=9498&opt1_id=9490&opt2_id=999999&opt_g=1&opt_type=3&opt_name=%E5%A5%B3%E8%A3%85T%E6%81%A4&_x_link_id=8d9100d3-4dd0-477e-bbd1-112048753cb7&_x_goods_id=87799715295&refer_page_name=search&refer_page_id=10031_1589170989878_ocxrxkeq6m&refer_page_sn=10031",
        'User-Agent': "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Mobile Safari/537.36",
        'Access-Control-Request-Headers': "content-type",
        'cache-control': "no-cache",
        'Postman-Token': "2f1ea5bd-6f72-40ee-8ece-627e8600204b"
    }

    response = requests.request("OPTIONS", url, headers=headers)

    # print(response.text)
    # print(response.text)
    pat_window_data = r'({"store".*?null}})'
    data = re.compile(pat_window_data).findall(response.text)[0]
    json_data = json.loads(data)
    print(json_data)
def get_page_2():
    import requests

    url = "http://cmtw.pinduoduo.com/api/page"

    payload = "{\"v\":1,\"t\":1589170993316,\"r\":\"cc6x2q\",\"c\":4273214038,\"d\":{\"t\":1589170993317,\"pn\":\"http://yangkeduo.com/search_catgoods.html\",\"n\":3,\"pl\":0,\"rts\":[1589170992245,0,0,1589170992256,1589170992256,1589170992256,1589170992256,0,1589170992256,1589170992259,1589170992287,1589170992350,1589170992353,1589170992298,1589170992368,1589170993048,1589170993048,1589170993048,1589170993314,1589170993314,1589170993314],\"e\":{},\"r\":1}}"
    headers = {
        'Referer': "http://yangkeduo.com/search_catgoods.html?opt_id=9498&opt1_id=9490&opt2_id=999999&opt_g=1&opt_type=3&opt_name=%E5%A5%B3%E8%A3%85T%E6%81%A4&_x_link_id=8d9100d3-4dd0-477e-bbd1-112048753cb7&_x_goods_id=87799715295&refer_page_name=search&refer_page_id=10031_1589170989878_ocxrxkeq6m&refer_page_sn=10031",
        'Origin': "http://yangkeduo.com",
        'User-Agent': "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Mobile Safari/537.36",
        'Content-Type': "application/json;charset=UTF-8",
        'cache-control': "no-cache",
        'Postman-Token': "a76b2f11-8f44-4863-b261-70f256cbb0a8"
    }

    response = requests.request("POST", url, data=payload, headers=headers)

    # print(response.text)
    # print(response.text)
    pat_window_data = r'({"store".*?null}})'
    data = re.compile(pat_window_data).findall(response.text)[0]
    json_data = json.loads(data)
    print(json_data)
def get_ajax_page():
    import requests

    url = "http://cmtw.pinduoduo.com/api/ajax"

    headers = {
        'Access-Control-Request-Method': "POST",
        'Origin': "http://yangkeduo.com",
        'Referer': "http://yangkeduo.com/search_catgoods.html?opt_id=9498&opt1_id=9490&opt2_id=999999&opt_g=1&opt_type=3&opt_name=%E5%A5%B3%E8%A3%85T%E6%81%A4&_x_link_id=8d9100d3-4dd0-477e-bbd1-112048753cb7&_x_goods_id=87799715295&refer_page_name=search&refer_page_id=10031_1589170989878_ocxrxkeq6m&refer_page_sn=10031",
        'User-Agent': "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Mobile Safari/537.36",
        'Access-Control-Request-Headers': "content-type",
        'cache-control': "no-cache",
        'Postman-Token': "a3dbfa2f-0db3-4349-9216-675c6ce492b2"
    }

    response = requests.request("OPTIONS", url, headers=headers)

    # print(response.text)
    # print(response.text)
    pat_window_data = r'({"store".*?null}})'
    data = re.compile(pat_window_data).findall(response.text)[0]
    json_data = json.loads(data)
    print(json_data)
def  get_search_result():
    import requests

    url = "http://yangkeduo.com/search_result.html"

    querystring = {"search_key": "%E9%9E%8B%E5%8C%85", "search_met_track": "history", "search_type": "mall",
                   "source": "index", "options": "1", "refer_page_el_sn": "403045", "refer_page_name": "search_result",
                   "refer_page_id": "10015_1589178729483_kwibst8md8", "refer_page_sn": "10015"}

    headers = {
        'Connection': "keep-alive",
        'Pragma': "no-cache",
        'Cache-Control': "no-cache",
        'Upgrade-Insecure-Requests': "1",
        'User-Agent': "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Mobile Safari/537.36",
        'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        'Referer': "http://yangkeduo.com/search_result.html?search_key=%E9%9E%8B%E5%8C%85&search_met_track=history&search_type=mall&source=index&options=1&refer_page_el_sn=403045&refer_page_name=search_result&refer_page_id=10015_1589178729483_kwibst8md8&refer_page_sn=10015",
        'Accept-Encoding': "gzip, deflate",
        'Accept-Language': "zh-CN,zh;q=0.9",
        'Cookie': "api_uid=CiS3B164rm0mbwBMNbhcAg==; _nano_fp=XpdJlpgjXpdJX5PqX9_awQm1oGHUOHEiS27K3F46; PDDAccessToken=XQNXEKAOYSLWJHX3QUAI5SYN5VOPSABQUZ7H6PHF7JWDKEYAXLEA1111969; pdd_user_id=1058890491161; pdd_user_uin=3R4Z7KFL26WAV6UGMP4YJ3Q76A_GEXDA; ua=Mozilla%2F5.0%20(Linux%3B%20Android%206.0%3B%20Nexus%205%20Build%2FMRA58N)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F70.0.3538.102%20Mobile%20Safari%2F537.36; webp=1; home_bottom=home_bottom_gphlnm; mall_main=mall_main_fpvkbh; JSESSIONID=F748600D67CD963DEE39B709A6546246",
        'cache-control': "no-cache",
        'Postman-Token': "a6155355-d9d0-44f1-b026-2e473c04d425"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    # print(response.text)
    pat_window_data = r'window.rawData=(.*?);\s*</script>'
    data = re.compile(pat_window_data).findall(response.text)[0]
    json_data = json.loads(data)
    print(json_data)
    # root_items =  json_data.get('store').get('data').get('rootItems')
    # index = 0
    # for sub_list in root_items:
    #     if index == 0:
    #         index += 1
    #     else:
    #         print(sub_list)
    #         print(type(sub_list))
def get_store_page():
    import requests

    url = "http://yangkeduo.com/mall_page.html"

    querystring = {"mall_id": "249266", "msn": "5qdl2fapsys6upccxu27rxnjbe_axbuy", "goods_id": "769654119",
                   "refer_page_name": "goods_detail", "refer_page_id": "10014_1589179870267_pw284wow3f",
                   "refer_page_sn": "10014"}

    headers = {
        'Connection': "keep-alive",
        'Pragma': "no-cache",
        'Cache-Control': "no-cache",
        'Upgrade-Insecure-Requests': "1",
        'User-Agent': "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Mobile Safari/537.36",
        'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        'Referer': "http://yangkeduo.com/goods.html?goods_id=769654119&page_from=39&is_spike=0&refer_page_name=mall_page&refer_page_id=10039_1589179850388_87ie8izp4f&refer_page_sn=10039&page_id=10014_1589179870267_pw284wow3f&is_back=1",
        'Accept-Encoding': "gzip, deflate",
        'Accept-Language': "zh-CN,zh;q=0.9",
        'Cookie': "api_uid=CiS3B164rm0mbwBMNbhcAg==; _nano_fp=XpdJlpgjXpdJX5PqX9_awQm1oGHUOHEiS27K3F46; PDDAccessToken=XQNXEKAOYSLWJHX3QUAI5SYN5VOPSABQUZ7H6PHF7JWDKEYAXLEA1111969; pdd_user_id=1058890491161; pdd_user_uin=3R4Z7KFL26WAV6UGMP4YJ3Q76A_GEXDA; ua=Mozilla%2F5.0%20(Linux%3B%20Android%206.0%3B%20Nexus%205%20Build%2FMRA58N)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F70.0.3538.102%20Mobile%20Safari%2F537.36; webp=1; JSESSIONID=E550D91B8DC8D7C41F657327FD7F6A43; mall_main=mall_main_1ldccl; home_bottom=home_bottom_a3nyjv",
        'cache-control': "no-cache",
        'Postman-Token': "59f464c3-c53e-43e5-9c13-4ced7d0db3ba"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    # print(response.text)
    pat_window_data = r'window.rawData=(.*?);\s*</script>'
    data = re.compile(pat_window_data).findall(response.text)[0]
    json_data = json.loads(data)
    print(json_data)
def get_mall_all_goods():
    user_agent,proxies = get_agent_proxies()
    url = "http://yangkeduo.com/proxy/api/api/turing/mall/query_cat_goods"

    import requests

    url = "http://yangkeduo.com/proxy/api/api/turing/mall/query_cat_goods"

    querystring = {"pdduid": "1058890491161",
                   "anticontent": "0aoAfaOUUOhgqgTaajh1CSTTCCl641og41KtGhAVqWAF1VttzMvntB4T4Hc18yJ6rpLx0LkKsi998Al7lZfIo4WCgr92xLNBFxoSVozZmQXk0qRivUAp3HsCGTsIHXG0JfWgcVR28colKu93JioqY94Obbf9PIEiZGmM_Hf_0HZ1d7xJXAxSCV6VwbigIE-UIJItGLDK6aukZisciHytBZITD6An_MWo2zm2Gi51H18sB7cKlBgi7d-Ay-Zf9LMuc3gpP31VlrHYO5hkVTpvvvfeqYKY3Lh-FIx85HGS1VY0pNnK-AqmbJs1zgLXLAAIxRk1MMlcMZNE9gIsUZDmvOY3ayuSjDqQ6d_yZjed8Zw7D4xbFzqt1b7XvkfIwf11vp7ZzvZkSAzvxwA1KeidxqJ4qg9nx4QaPHhfD0xgqxgXDchgrlZjs9KXdjpEQfY4__-V5gB1q9_SLYBo4lEmlweh1sV08um0vln3eCTp6z72KLMg0QToT1mA1jb42Al4tOonVz56EBQHBPWVOFsqG-5g2-5NFBmyInOyghNPSONeXKJBJ8EI4JwTDOyq6yFitK63BC0NWtmHaQ-0cftP7K6yU8d6VxXVYADZXmpVhkenrUjYQlSx2t-uG4Xee8SvskaVSkeB8lB75c2drpGDI9fbj7LnQmQAwJAMU3QXJL6FPNOkNS80OqaGC-5CiBH1fqt0Su47vuGOezFj0NXxEOX1lyKvMhlUWh_pkaSdfrW082dCxAo42LRuJWiimMs6S6DXtNh1KVTk-60dFvp2zhT1ArvcjRjfNoUh7IYucNgBAi6mDr7uIOR9z0nJVT",
                   "category_id": "0", "type": "0", "mall_id": "280511157", "page_size": "20", "sort_type": "default",
                   "refer_page_param": "", "refer_page_sn": "10015", "msn": "db62mjcvfhhsb4dnmqvxwlofn4_axbuy",
                   "list_id": "mall_main_k7w8lh", "page_from": "39", "query": "", "goods_id": "0",
                   "new_store_goods": "", "page_no": "2"}

    headers = {
        'Pragma': "no-cache",
        'Accept-Encoding': "gzip, deflate",
        'Accept-Language': "zh-CN,zh;q=0.9",
        'User-Agent': "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Mobile Safari/537.36",
        'VerifyAuthToken': "L2fohYxrsRbTvFFY_9HU-A",
        'Accept': "application/json, text/plain, */*",
        'Cache-Control': "no-cache",
        'AccessToken': "JEE4AZNHVL6AQGJJJGK2A42PCDVNSCE6O5X3F6W2V6GFMAVXALYA1111969",
        'Cookie': "api_uid=rBUGkl65AuNVDW/TGgiFAg==; _nano_fp=XpdJlpgJXqPol0T8lT_9qF4HbTB5ghHMxrtat_gM; PDDAccessToken=JEE4AZNHVL6AQGJJJGK2A42PCDVNSCE6O5X3F6W2V6GFMAVXALYA1111969; pdd_user_id=1058890491161; pdd_user_uin=3R4Z7KFL26WAV6UGMP4YJ3Q76A_GEXDA; ua=Mozilla%2F5.0%20(Linux%3B%20Android%206.0%3B%20Nexus%205%20Build%2FMRA58N)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F70.0.3538.102%20Mobile%20Safari%2F537.36; webp=1; home_bottom=home_bottom_rwor2w; JSESSIONID=CF3CBC4BAF647B276D97FEA837C0C96C; mall_main=mall_main_k7w8lh",
        'Connection': "keep-alive",
        'Referer': "http://yangkeduo.com/mall_page.html?mall_id=280511157&msn=db62mjcvfhhsb4dnmqvxwlofn4_axbuy&mall_type=0&refer_page_el_sn=373286&refer_page_name=search_result&refer_page_id=10015_1589183359608_g9crmcn1sd&refer_page_sn=10015",
        'cache-control': "no-cache",
        'Postman-Token': "950a2910-4012-4b32-b1ca-6948a3b1bd2e"
    }

    response = session.request("GET", url, headers=headers, params=querystring,proxies = proxies)
    print(response.text)
    pat_window_data = r'window.rawData=(.*?);\s*</script>'
    data = re.compile(pat_window_data).findall(response.text)
    json_data = json.loads(data)
    print(json_data)
def get_first_page():
    import requests

    url = "http://yangkeduo.com/"

    headers = {
        'User-Agent': "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Mobile Safari/537.36",
        'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        'Postman-Token': "621ea5a6-eb66-408a-b379-899431ecbaeb"
    }
    response = requests.request("GET", url, headers=headers)

    print(response.text)
    # pat_window_data = r'({"store".*?null}})'
    # data = re.compile(pat_window_data).findall(response.text)[0]
    # json_data = json.loads(data)
    # print(json_data)
def main():
    # get_index_page()
    get_classification_page()
    # get_catgoods_page()
    # get_group_data()
    # get_stm_page()
    # get_page_1()
    # get_page_2()
    # get_ajax_page()
    # get_search_result()
    # get_store_page()
    # get_mall_all_goods()
    # get_first_page()
if __name__ == '__main__':
    main()