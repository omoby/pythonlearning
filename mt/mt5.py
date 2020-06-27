import random
import socket
import ssl
import urllib
import re
import zlib
import os
import time

import OpenSSL
import cx_Oracle
import requests
import urllib3

from DPCrawler.config import PROXY_POOL, MT_5_COOKIE
from DPCrawler.setting import USER_AGENTS

user = 'crawlm'
passwd = 'crawlm_Sd'
database = 'dcappdb'
host = '172.22.5.61'
port = '1526'
conn_info = user+"/"+passwd+"@"+host+":"+port+"/"+database


def get_proxy():
    proxy_pool_url = random.choice(PROXY_POOL)
    proxy_ip = urllib.request.urlopen(proxy_pool_url).read().decode("utf-8").split("\n")[1]
    if ',' in proxy_ip:
        proxy_ip = proxy_ip.split(',')[0]
    if 'http' in proxy_ip:
        proxy_ip = proxy_ip.split('//')[1]
    proxy = {'https': proxy_ip, 'http': proxy_ip}
    return proxy
def get_agent_proxies():
    user_agent = random.choice(USER_AGENTS)
    proxy_pool_url = random.choice(PROXY_POOL)
    cookie = random.choice(MT_5_COOKIE)
    proxy_ip = urllib.request.urlopen(proxy_pool_url).read().decode("utf-8").split("\n")[1]
    if ',' in proxy_ip:
        proxy_ip = proxy_ip.split(',')[0]
    if 'http' in proxy_ip:
        proxy_ip = proxy_ip.split('//')[1]
    proxy = {'https': proxy_ip, 'http': proxy_ip}
    return (user_agent,proxy,cookie)

#python连接Oracle数据库的工具类
class OracleUtil():
    """
    获取省份id的list
    """
    def get_url(self):
        conn = cx_Oracle.connect(conn_info)
        # 获取cursor光标
        cursor = conn.cursor()
        # 数据库操作
        # 1.查询
        sql = "select ID_SEQ, TASK_URL from o1255_task_url_202004 where ID_SEQ NOT IN (select ID_SEQ FROM MT_MALL_DETAIL_202004) AND ID_SEQ > 10000 and ID_SEQ <=15000"

        result = cursor.execute(sql)
        data = result.fetchall()
        cursor.close()
        conn.close()
        return data

    def save_page(self,data):
        conn = cx_Oracle.connect(conn_info)
        cursor = conn.cursor()
        inser_sql = 'insert into MT_MALL_DETAIL_202004 values(:ID_SEQ,:DATA_CLOB)'
        try:
            cursor.executemany(inser_sql, data)
        except cx_Oracle.IntegrityError as e:
            print(e)
        except cx_Oracle.DatabaseError as e:
            print(e)
        cursor.execute('commit')
        conn.commit()
        print('end')
        print('--------save_page--------' * 2)
        cursor.close()
        conn.close()
    def save_page_not_exist(self,data):
        conn = cx_Oracle.connect(conn_info)
        cursor = conn.cursor()
        inser_sql = 'insert into MT_PAGE_NOT_EXIST_202004 values(:ID_SEQ,:TASK_URL)'
        try:
            cursor.executemany(inser_sql, data)
        except cx_Oracle.IntegrityError as e:
            print(e)
        except cx_Oracle.DatabaseError as e:
            print(data)
            print(e)
        cursor.execute('commit')
        conn.commit()
        print('end')
        print('/////////////save_page_not_exist////////' * 2)
        cursor.close()
        conn.close()

    def get_page(self):
        conn = cx_Oracle.connect(conn_info)
        cursor = conn.cursor()

        sql = 'select * from  MT_MALL_DETAIL_202004 '
        result = cursor.execute(sql)
        data = result.fetchall()
        for sub in data:
            text = sub[1].read()
        cursor.close()
        conn.close()
        return text



connection = OracleUtil()

def get_shop_info(url,code):
    global g_user_agent
    global g_proxy
    global g_cookie
    global session
    if code == 1:

        # g_user_agent,g_proxy,g_cookie = get_agent_proxies()
        print(url,g_user_agent,g_proxy,g_cookie)
        g_cookie = random.choice(MT_5_COOKIE)
        g_user_agent = random.choice(USER_AGENTS)

        print('g_cookie=%s' %(g_cookie))
        print('g_user_agent=%s' % (g_user_agent))
    if code == 2:
        session = requests.Session()
        # g_user_agent,g_proxy,g_cookie = get_agent_proxies()
        # print(url,g_user_agent,g_proxy,g_cookie)
        # g_cookie = random.choice(MT_2_COOKIE)
        g_proxy = get_proxy()
        print('g_proxy=%s' % (g_proxy))
    headers = {
        'Host': 'i.meituan.com',
        # 'User-Agent': g_user_agent,
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Mobile Safari/537.36',
        # 'Cookie': '__mta=174554781.1589017495929.1589017662742.1589017680828.5; JSESSIONID=mbuia9ebhzm0dm0qrx1p6i6q; IJSESSIONID=mbuia9ebhzm0dm0qrx1p6i6q; iuuid=721340E7D319C753C4313C5ABB2D84715700475E1807165AA261906AA994B427; latlng=31.575595%2C120.295214%2C1589017492962; ci=52; cityname=%E6%97%A0%E9%94%A1; _lxsdk_cuid=171f7207099c8-0df914ad397918-87f133f-144000-171f7207099c8; _lxsdk=721340E7D319C753C4313C5ABB2D84715700475E1807165AA261906AA994B427; _hc.v=8f6b3d58-31f6-5220-9423-eec9136cafba.1589017495; webp=1; i_extend=H__a100016__b1; __utma=74597006.901397947.1589017496.1589017496.1589017496.1; __utmc=74597006; __utmz=74597006.1589017496.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmb=74597006.5.10.1589017496; _lxsdk_s=171f8d2c5d9-403-2db-8b%7C%7C10'
        'Cookie': g_cookie

    }

    try:
        response = session.get(url,headers=headers,proxies=g_proxy,timeout=30)
        response.encoding='utf-8'
        status_code = response.status_code
        text = response.text
        if status_code == 403:

            get_shop_info(url, 2)
        if '很抱歉，您要访问的页面不存在' in text:
            return 'not_exist'
        return  zlib.compress(response.content)
    except socket.timeout as e:
        print(e.errno)
        print('ConnectionResetError')
        return 'time_out'
    except requests.exceptions.ReadTimeout as e:
        print(e.errno)
        print('ConnectionResetError')
        return 'time_out'
    except ConnectionResetError as e:
        print(e.errno)
        print('ConnectionResetError')
        get_shop_info(url, 2)
    except urllib3.exceptions.MaxRetryError as e:
        print(e.errno)
        print('urllib3.exceptions.MaxRetryError')
        get_shop_info(url, 2)
    except requests.exceptions.ProxyError as e:
        print(e.errno)
        print('requests.exceptions.ProxyError')
        get_shop_info(url, 2)
    except OpenSSL.SSL.SysCallError as e:
        print(e.errno)
        print('OpenSSL.SSL.SysCallError')
        get_shop_info(url, 2)
    except ssl.SSLError as e:
        print(e.errno)
        print('ssl.SSLError')
        get_shop_info(url, 2)
    except requests.exceptions.SSLError as e:
        print(e.errno)
        print('requests.exceptions.SSLError')
        get_shop_info(url, 2)
def analysis_page(data):
    decompressor = zlib.decompressobj()
    decompressed = decompressor.decompress(data) # 这里只解压压缩的数据
    decompressed.decode ('utf-8')

    print(decompressed)



g_user_agent = random.choice(USER_AGENTS)
g_proxy = get_proxy()
g_cookie = random.choice(MT_5_COOKIE)
session = requests.Session()

def main():
    data = connection.get_url()
    success_counter = 0
    fail_counter = 0
    for url_tuple in data:
        print('***********begin**************'*2)
        time.sleep(1)
        id_seq =   url_tuple[0]
        url = url_tuple[1]
        print(id_seq,url)
        data = []
        global session
        data_text = get_shop_info(url,0)
        if 'not_exist' == data_text:
            data.append((id_seq, url))

            g_user_agent, g_proxy, g_cookie = get_agent_proxies()
            # g_proxy = get_proxy()
            print('page_not_exist', g_proxy,g_cookie)
            fail_counter += 1
            print('fail_counter=%d' % (fail_counter))

            connection.save_page_not_exist(data)

            # print(data)
            session = requests.Session()
        elif 'time_out' == data_text:
            data.append((id_seq, url))
            connection.save_page_not_exist(data)
            g_user_agent, g_proxy, g_cookie = get_agent_proxies()
            print('time_out', g_user_agent, g_proxy, g_cookie)
            print(data)
            # session = requests.Session()
        else:
            data.append((id_seq, data_text))
            success_counter += 1
            print('success_counter=%d' % (success_counter))
            connection.save_page(data)

if __name__ == '__main__':
    main()
    # get_agent_proxies()
    # data = connection.get_page()
    # analysis_page(data)