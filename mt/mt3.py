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

from DPCrawler.config import PROXY_POOL, MT_COOKIE
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
    cookie = random.choice(MT_COOKIE)
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
        sql = "select ID_SEQ, TASK_URL from o1255_task_url_202004 where ID_SEQ NOT IN (select ID_SEQ FROM MT_MALL_DETAIL_202004) AND ID_SEQ > 100000 and ID_SEQ <=101000"

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
        print('+++++++++++save_page++++++++'*2)
        print()
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
            print(e)
        cursor.execute('commit')
        conn.commit()
        print('--------save_page_not_exist--------' * 2)
        print()
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
    if code == 1:
        global  g_user_agent
        global g_proxy
        global g_cookie
        # g_user_agent,g_proxy,g_cookie = get_agent_proxies()
        g_proxy  = get_proxy()
        g_user_agent = random.choice(USER_AGENTS)
        print(url,g_user_agent,g_proxy)
    headers = {
        'Host': 'i.meituan.com',
        'User-Agent': g_user_agent,
        # 'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Mobile Safari/537.36',
        # 'Cookie': g_cookie
        'Cookie':'au_trace_key_net=default;_lxsdk=925D202C34254B4BB548450110B9E3038AF16AF59236A3F2F4A9682B330AC601;service-off=0;channelType={%22default%22:%220%22};uuid=925D202C34254B4BB548450110B9E3038AF16AF59236A3F2F4A9682B330AC601;userId=730229479;token=hTCL2XB6aNmVJEmoMX8O1Z2Z6uQAAAAAjwoAAByXkOI0btfmSZ5boLN64kQ5gZQhy4lQSGHH7jJiDAwViHNv4YPuMfy-7XElmKUyJg;openh5_uuid=925D202C34254B4BB548450110B9E3038AF16AF59236A3F2F4A9682B330AC601;channelConfig={%22channel%22:%22default%22%2C%22type%22:0%2C%22fixedReservation%22:{%22reservationTimeStatus%22:0%2C%22startReservationTime%22:0%2C%22endReservationTime%22:0}};mt_c_token=hTCL2XB6aNmVJEmoMX8O1Z2Z6uQAAAAAjwoAAByXkOI0btfmSZ5boLN64kQ5gZQhy4lQSGHH7jJiDAwViHNv4YPuMfy-7XElmKUyJg;oops=hTCL2XB6aNmVJEmoMX8O1Z2Z6uQAAAAAjwoAAByXkOI0btfmSZ5boLN64kQ5gZQhy4lQSGHH7jJiDAwViHNv4YPuMfy-7XElmKUyJg;_lxsdk_cuid=1720b84753cc8-011b8a7b84bf26-2d604637-54600-1720b84753dc8;_lx_utm=utm_source%3D60066;_lxsdk_s=1720b84753e-3e5-861-d11%7C%7C6;iuuid=925D202C34254B4BB548450110B9E3038AF16AF59236A3F2F4A9682B330AC601;wm_order_channel=default;webloc_geo=36.674225%2C117.127767%2Cgcj02%2C-1;utm_source=;'
    }
    global session
    try:
        response = session.get(url,headers=headers,proxies=g_proxy,timeout= 40)
        response.encoding='utf-8'
        status_code = response.status_code
        text = response.text
        if status_code == 403:
            session = requests.Session()
            get_shop_info(url, 1)
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
        get_shop_info(url, 1)
    except urllib3.exceptions.MaxRetryError as e:
        print(e.errno)
        print('urllib3.exceptions.MaxRetryError')
        get_shop_info(url, 1)
    except requests.exceptions.ProxyError as e:
        print(e.errno)
        print('requests.exceptions.ProxyError')
        get_shop_info(url, 1)
    except OpenSSL.SSL.SysCallError as e:
        print(e.errno)
        print('OpenSSL.SSL.SysCallError')
        get_shop_info(url, 1)
    except ssl.SSLError as e:
        print(e.errno)
        print('ssl.SSLError')
        get_shop_info(url, 1)
    except requests.exceptions.SSLError as e:
        print(e.errno)
        print('requests.exceptions.SSLError')
        get_shop_info(url, 1)
def analysis_page(data):
    decompressor = zlib.decompressobj()
    decompressed = decompressor.decompress(data) # 这里只解压压缩的数据
    decompressed.decode ('utf-8')

    print(decompressed)



g_user_agent = random.choice(USER_AGENTS)
g_proxy = get_proxy()
g_cookie = random.choice(MT_COOKIE)
session = requests.Session()
start_time = time.time()

def main():
    data = connection.get_url()
    success_counter = 0
    fail_counter = 0
    for url_tuple in data:
        print('**********begin******'*2)
        time.sleep(1)
        id_seq =   url_tuple[0]
        url = url_tuple[1]
        print(id_seq,url)
        data = []
        # global session
        data_text = get_shop_info(url,0)
        if 'not_exist' == data_text:
            data.append((id_seq, url))
            print('run_time=%d' % (time.time() - start_time))
            fail_counter += 1
            print('not_exist_counter=%d' % (fail_counter))
            # g_user_agent, g_proxy, g_cookie = get_agent_proxies()
            g_proxy = get_proxy()
            g_user_agent = random.choice(USER_AGENTS)
            # print('page_not_exist', g_user_agent, g_proxy, g_cookie)
            print('page_not_exist', g_proxy,g_user_agent)
            session = requests.Session()
            connection.save_page_not_exist(data)
        elif 'time_out' == data_text:
            data.append((id_seq, url))

            g_user_agent, g_proxy, g_cookie = get_agent_proxies()
            print('time_out', g_user_agent, g_proxy, g_cookie)
            # session = requests.Session()
            connection.save_page_not_exist(data)
        else:
            data.append((id_seq, data_text))
            success_counter += 1
            print('counter=%d' % (success_counter))
            connection.save_page(data)


if __name__ == '__main__':
    main()
    # get_agent_proxies()
    # data = connection.get_page()
    # analysis_page(data)