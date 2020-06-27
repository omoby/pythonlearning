import json
import re

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
    获取省份id的list
    """
    def insert_pdd_category(self,data):
        conn = cx_Oracle.connect(conn_info)
        # 获取cursor光标
        cursor = conn.cursor()
        # 数据库操作
        inser_sql = 'INSERT INTO PDD_CATEGORY VALUES (:CATEGORY_ID,:CATEGORY_NAME)'

        try:
            cursor.executemany(inser_sql, data)
            cursor.execute('commit')
            conn.commit()
        except cx_Oracle.IntegrityError as e:
            print('cx_Oracle.IntegrityError')
        cursor.close()
        conn.close()
oracle = OracleUtil()
def get_all_categroy():
    import requests

    url = "http://yangkeduo.com/classification.html"

    querystring = {"refer_page_name": "index", "refer_page_id": "10002_1590136501068_8xe0a1ttt1",
                   "refer_page_sn": "10002"}

    headers = {
        'Connection': "keep-alive",
        'Pragma': "no-cache",
        'Cache-Control': "no-cache",
        'Upgrade-Insecure-Requests': "1",
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36",
        'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        'Referer': "http://yangkeduo.com/?list_id=b5wsuk48mf&page_id=10002_1590136501068_8xe0a1ttt1&is_back=1",
        'Accept-Encoding': "gzip, deflate",
        'Accept-Language': "zh-CN,zh;q=0.9",
        'Cookie': "api_uid=rBUUM17HL6S8h0nKiiAsAg==; ua=Mozilla%2F5.0%20(Windows%20NT%2010.0%3B%20WOW64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F70.0.3538.102%20Safari%2F537.36; _nano_fp=XpdbX0gaXqU8n0Tbn9_0ijMkv14evpnbYZMXROBk; webp=1; PDDAccessToken=ARFCTNXKIX5IGSDJA7D5BAJ377SMFJGFTYMDJYC7R5TRF46OHYSQ1111969; pdd_user_id=1058890491161; pdd_user_uin=3R4Z7KFL26WAV6UGMP4YJ3Q76A_GEXDA; JSESSIONID=6656BE89DCA0D35D14FC8F54C9C945BB",
        'cache-control': "no-cache",
        'Postman-Token': "a4bdd561-1ee6-4afd-a956-4d12f5799b0c"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    # print(response.text)
    pat_window_data = r'window.rawData=(.*?);\s*</script>'
    data = re.compile(pat_window_data).findall(response.text)[0]
    # print(data)
    json_data = json.loads(data)
    # return json_data
    # print(json_data)
    store = json_data.get('store')
    data = store.get('data')
    # print(data)
    root_items = data.get('rootItems')
    items = []
    index = 0
    for item in root_items:
        opt_name = item.get('optName')
        if opt_name in '推荐':
            pass
        else:
            items.append((index,opt_name))
        index += 1
    print(items)
    oracle.insert_pdd_category(items)






def main():
    get_all_categroy()


if __name__ == '__main__':
    main()