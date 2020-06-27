import json
import random
import time

import requests

import cx_Oracle

user = 'crawlm'
passwd = 'crawlm_Sd'
database = 'dcappdb'
host = '172.22.5.61'
port = '1526'
conn_info = user+"/"+passwd+"@"+host+":"+port+"/"+database

"""
python连接Oracle数据库的工具类
"""
class OracleUtil():
    """
    获取所有店铺的信息
    """
    def get_mall_info(self,data):
        conn = cx_Oracle.connect(conn_info)
        #获取cursor游标
        cursor=conn.cursor()
        #数据库操作
        #1.查询
        query_sql='SELECT DISTINCT MALL_ID,MALL_NAME,MERCHANT_TYPE FROM  PDD_MALL WHERE MALL_ID=:1'
        result=cursor.execute(query_sql,data)
        mall_data = result.fetchall()
        #1.插入操作
        cursor.close()
        conn.close()
        return mall_data

    """
    插入店铺信息
    """
    def insert_mall_info(self,data):
        conn = cx_Oracle.connect(conn_info)
        # 获取cursor光标
        cursor = conn.cursor()
        # 数据库操作
        inser_sql = 'INSERT INTO PDD_MALL VALUES (:MALL_ID,:MALL_NAME,:MERCHANT_TYPE)'

        try:
            cursor.executemany(inser_sql, data)
            cursor.execute('commit')
            conn.commit()
        except cx_Oracle.IntegrityError as e:
            print('cx_Oracle.IntegrityError')
        cursor.close()
        conn.close()
    '''
    获取店铺分类
    '''
    def get_pdd_category(self):
        conn = cx_Oracle.connect(conn_info)
        # 获取cursor游标
        cursor = conn.cursor()
        # 数据库操作
        # 1.查询
        query_sql = 'SELECT DISTINCT CATEGORY_NAME FROM  PDD_CATEGORY'
        result = cursor.execute(query_sql)
        category_data = result.fetchall()
        # 1.插入操作
        cursor.close()
        conn.close()
        return category_data

oracle = OracleUtil()

'''
采集店铺数据
'''
def get_all_mall_data(key_word,page_num):
    global total_count
    global now_count
    url = "https://jinbao.pinduoduo.com/network/api/merchant/queryMallByKeyword"
    if page_num ==1:
        payload = '{"keyword":"'+key_word+'"}'
    else:
        payload = '{"keyword":"'+key_word+'","pageNumber":"'+str(page_num)+'"}'
    headers = {
        'pragma': "no-cache",
        'cookie': "_nano_fp=XpdbX0X8XpCqn5djl9_b_Bywp_CajUUhEuw6LCea; api_uid=rBUUYF7LJf2AL1tP9awcAg==; DDJB_PASS_ID=171536280ca22da9c6ea3f0d835e0bb3",
        'origin': "https://jinbao.pinduoduo.com",
        'accept-encoding': "gzip, deflate, br",
        'accept-language': "zh-CN,zh;q=0.9",
        'user-agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36",
        'content-type': "application/json;charset=UTF-8",
        'accept': "application/json, text/plain, */*",
        'cache-control': "no-cache,no-cache",
        'authority': "jinbao.pinduoduo.com",
        'referer': "https://jinbao.pinduoduo.com/promotion/store-promotion?keyword=%E6%89%8B%E6%9C%BA",
        'Postman-Token': "cee85eb0-4215-49e0-aec4-09593b67ab2e"
        }
    # print(payload)
    response = requests.request("POST", url, data=payload.encode('utf-8'), headers=headers)
    json_data = response.json()
    # print(json_data)
    success = json_data.get('success')
    if success is True:
        # print(json_data)
        result = json_data.get('result')
        mall_List = result.get('mallSearchInfoVoList')
        # print(mall_List)
        if len(mall_List) ==0 :
            return 'acquisition complete！'
        else:
            mall_data = []
            for mall in mall_List:
                mall_id = mall.get('mallId')
                mall_name = mall.get('mallName')
                merchant_type = mall.get('merchantType')
                mall_json = (mall_id,mall_name,merchant_type)
                # print(mall_json)
                mall_data.append(mall_json)
            return mall_data
    else:
        return json_data.get('errorMsg')
        # return  '.....'

'''
采集一个店铺的所有商品
'''
def get_one_mall_data():
    import requests

    url = "https://jinbao.pinduoduo.com/network/api/merchant/queryAllGoodsByMallId"

    querystring = {"mallId": "805735", "pageNumber": "1", "pageSize": "100"}

    headers = {
        'pragma': "no-cache",
        'cookie': "_nano_fp=XpdbX0gaX5gjXqT8X9_nPjiBJq_N3luP9oxAhVFF; api_uid=rBUU+V7HL6NoTRmTio1sAg==; DDJB_PASS_ID=0075f253858d83f6dfcf593850563925",
        'accept-encoding': "gzip, deflate, br",
        'accept-language': "zh-CN,zh;q=0.9",
        'user-agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36",
        'accept': "application/json, text/plain, */*",
        'cache-control': "no-cache,no-cache",
        'authority': "jinbao.pinduoduo.com",
        'referer': "https://jinbao.pinduoduo.com/promotion/store-promotion?keyword=890164712",
        'Postman-Token': "9d7e0ad1-6057-4b8c-8700-b170f91a8ae0"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    print(response.json())
def get_analysis_json():
    with open('D:\MyFile\工作记录文件\python3开发网络爬虫\拼多多\ddjb.txt','r',encoding='utf-8') as f:
        data = f.read()
    data = data.replace("'",'"')
    print(data)
    print(type(data))
    json_data= json.loads(data)
    print(type(json_data))
    print(json_data)


def main():
    category = oracle.get_pdd_category()
    for cat in category:
        key_word = cat[0]
        page_num = 1
        index = 0
        msg = 'running'
        flag = True
        print(key_word)
        if key_word =='食品' or key_word =='鞋包' or key_word == '生鲜' or key_word == '数码' \
                or key_word == '百货' or key_word == '手机' or key_word == '运动' or key_word == '家装'\
                or key_word == '车品' or key_word == '健康' or key_word == '海淘':
            pass
        else:
            while flag:
                time.sleep(random.randint(1,5))
                data = get_all_mall_data(key_word, page_num)
                print(data)
                if 'complete' in data:
                    if index > 5:
                        msg = 'complete'
                        flag = False
                    print('msg=%s' %(msg))
                    print('品类[ %s ]采集完毕' % (key_word))
                    print('index=%s,page_num=%d' % (index, page_num))
                    index +=1
                    page_num += 1

                elif '页码最大为999' in data:
                    msg = '页码最大为999'
                    flag = False
                    print('msg=%s' %(msg))
                    print('品类[ %s ]采集完毕' % (key_word))
                    print('index=%s,page_num=%d' % (index, page_num))
                else:
                    oracle.insert_mall_info(data)
                    print('category=%s,page_num=%d' % (key_word, page_num))
                    page_num += 1
                    index = 0
        # get_one_mall_data()
        # get_analysis_json()
    # get_analysis_json()

if __name__ == '__main__':
    main()


