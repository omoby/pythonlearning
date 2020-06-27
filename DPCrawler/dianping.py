# -- coding: utf-8 --
import json
import sys
import urllib
# from http.cookiejar import Cookie

import requests
import time
import random
import requests
from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

from DPCrawler.config import PROXY_POOL, COOKIE
from DPCrawler.dianping_main_category import DianpingMainCategory
from DPCrawler.dianping_record import DianpingRecord
from DPCrawler.dianping_sub_category import DianpingSubCategory
from DPCrawler.dianping_util import get_uuid
from DPCrawler.oracle_util import OracleUtil
from DPCrawler.setting import USER_AGENTS


def get_headers(cityEnName,categoryId,regionId):
    user_agent = random.choice(USER_AGENTS)
    cookie= random.choice(COOKIE)
    # print(user_agent)
    headers = {
        'Host':'m.dianping.com',
        'Referer': 'https://m.dianping.com/'+str(cityEnName)+'/ch'+str(categoryId)+'/r'+str(regionId),
        'Origin': 'https://m.dianping.com',
        'User-Agent': user_agent,
        'Content-Type': 'application/json',
        'Cookie': cookie
    }
    return headers
def get_payload(citiId,cityEnName,categoryId,regionId):
    # my_uuid = get_uuid()
    payload = {
        "uuid":'c43e76d1-800b-eeec-d5d1-970df938af29.1585206885',
        "platform":1,
        "partner":150,
        "optimusCode":10,
        "originUrl":'https://m.dianping.com/'+cityEnName+'/ch'+str(categoryId)+'/r'+str(regionId),
        "pageEnName":"shopList",
        "moduleInfoList":[
            {
                "moduleName":"mapiSearch",
                "query":
                    {
                        "search":
                            {
                                "start":0,
                                "categoryId":''+str(categoryId),
                                "parentCategoryId":categoryId,
                                "locateCityid":0,
                                "limit":20,
                                "sortId":"0",
                                "cityId":citiId,
                                "regionId":regionId,
                                "maptype":0,
                                "keyword":""
                            }
                    }
            },
            {
                "moduleName":"downloadlayer",
                "query":
                    {}
            },
            {
                "moduleName":"red-pocket",
                "query":
                    {},
                "config":
                    {
                        "openUTM":"pmx:all:shoplist_xrhb:m",
                        "downloadUTM":"pmx:all:shoplist_xrhb:m",
                        "oldUser":'true',
                        "downloadURL":"https://m.dianping.com/download/redirect?id=4913289",
                        "smallImageUrl":"https://p1.meituan.net/scarlett/a880313f0f0e72515cda184b7a7daa1391293.png",
                        "bigImageUrl":"https://p0.meituan.net/scarlett/2ff3f5830faa0cca88651c010edb282d70448.png",
                        "openURL":"dianping://shoplist?categoryid={categoryId}&keepcategory=1&target=localshoplist",
                        "timeout":"1800",
                        "url":"dianping://web?url=https%3a%2f%2fm.dianping.com%2fnode-newcomer-gift-web%2fpages%2fmain.html%3fnotitlebar%3d1%26cityid%3d*%26dpid%3d*%26latitude%3d*%26longitude%3d*%26utm%3d",
                        "ignorable":'true',
                        "newUser":'true'
                    }
            },
            {
                "moduleName":"autoopen",
                "query":
                    {}
            }
        ]
    }
    return payload
'''
请求module接口数据
'''
def dianping_module(city_id,city_en_name,region_id,main_category_id):
    payload_headers = get_headers(city_en_name,main_category_id,region_id)
    payload = get_payload(city_id,city_en_name,main_category_id,region_id)
    re = ''
    module_url = 'https://m.dianping.com/isoapi/module'
    flage = 1
    if flage ==0:
        # print(payload_headers)
        proxy_ip = urllib.request.urlopen(PROXY_POOL).read().decode("utf-8").split("\n")[1]
        print(proxy_ip)
        proxy = {'https':proxy_ip,'http':proxy_ip}
        print(proxy)

        #proxies= proxy
        re = requests.post(url=module_url,data=json.dumps(payload),headers = payload_headers,proxies= proxy,timeout=5,verify=False)
    else:
        re = requests.post(url=module_url, data=json.dumps(payload), headers=payload_headers, timeout=5,verify=False)
    # dumpJsonData = json.dumps(payload)
    # # print(f"dumpJsonData = {dumpJsonData}")
    text = re.text
    if '403 Forbidden' in text:
        print(f"res={re.text}")
        dianping_module(city_id, city_en_name, region_id, main_category_id)
    # sys.exit(0)
    elif '您的网络好像不太给力' in text:
        load_dict = re.json()
        print(re.json())
        sys.exit(0)
    else:
        print(re.json())
        load_dict = re.json()
        # load_dict=''
        main_category_list = []
        sub_category_list = []
        record_list = []
        # with open("../file/module.json", mode='r', encoding='utf-8') as load_f:
        #     load_dict = json.load(load_f)
        data = load_dict['data']
        moduleInfoList = data['moduleInfoList']
        list_first = moduleInfoList[0]
        # query = list_first['query']
        # search = query['search']
        # analysis_search(search)
        # (category_id, city_id, region_id) = analysis_search(search)
        # print(f"categoryId={category_id},cityId={city_id},regionId={region_id}")

        categoryNavs = list_first['moduleData']['data']['listData']['categoryNavs']
        main_categorys = oracleUtil.get_main_category_id()
        sub_categorys = oracleUtil.get_sub_category_id()
        for index in range(len(categoryNavs)):
            row_record = categoryNavs[index]
            count = row_record['count']
            id = row_record['id']
            name = row_record['name']
            parent_id = row_record['parentId']
            if (id != 0) and (parent_id == 0) and (id not in main_categorys):
                main_category = DianpingMainCategory(id, name)
                main_category_list.append(main_category)
                # print(main_category.__str__())
            elif id != 0 and parent_id != 0:
                row_key = str(int(time.time() * 1000 * 1000))
                if(id not in sub_categorys ):
                    sub_category = DianpingSubCategory(id, parent_id, name)
                    if(sub_category not in sub_category_list):
                        sub_category_list.append(sub_category)
                # print(sub_category.__str__())
                record = DianpingRecord(row_key, region_id, id, count)
                record_list.append(record)
                # print(record.__str__())
        #     # print(categoryNavs[index])
        # # print(type(categoryNavs))
        conntion = OracleUtil()
        conntion.insert_main_category(main_category_list)
        conntion.insert_sub_category(sub_category_list)
        if len(record_list) == 0:
            row_key = str(int(time.time() * 1000 * 1000))
            record = DianpingRecord(row_key,region_id,0,0)
            record_list.append(record)
        conntion.insert_record(record_list)

# def analysis_search(search):
#     print(search)
#     category_id = search['categoryId']
#     city_id = search['cityId']
#     region_id = search['regionId']
#     return category_id,city_id,region_id



oracleUtil = OracleUtil()
# 获取数据库中省份的id的list
province_list = oracleUtil.get_province_id()
#
crowed_region_list =oracleUtil.get_crawed_region_id()
# # 获取数据库中店铺大类的id的list
main_category_list = oracleUtil.get_main_category_id()
# category_length = len(main_category_list)
for province_id in province_list:
    print("----------"*20)
    print(f"province_id=%d "%(province_id))
    # 获取每一个省份的城市id的list
    city_list = oracleUtil.get_city_info(province_id)
    # dianping_module(434, 'miyun', 65443, 10)
    for city in city_list:
        city_id = city[0]
        print(f"city_id=%d" %(city_id))
        city_en_name = city[1]
        region_list = oracleUtil.get_region_id(city_id)
        for region_id in region_list:
            if region_id not in crowed_region_list:
                time.sleep(5)
                # ran_id = int(random.uniform(0,category_length))
                # main_category_id = main_category_list[ran_id]
                main_category_id = 10
                print(f"city_id=%d, city_en_name=%s, region_id=%d" %(city_id,city_en_name,region_id))
                dianping_module(city_id,city_en_name,region_id,main_category_id)
    print("----------" * 20)




# dianping_module(434, 'miyun', 65443, 10)
# dianping_module(prev_url,module_url)
# analysis_module()
