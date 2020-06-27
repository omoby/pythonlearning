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
'''
获取代理IP
'''
def get_proxy():
    proxy_pool_url = random.choice(PROXY_POOL)
    proxy_ip = urllib.request.urlopen(proxy_pool_url).read().decode("utf-8").split("\n")[1]
    if ',' in proxy_ip:
        proxy_ip = proxy_ip.split(',')[0]
    if 'http' in proxy_ip:
        proxy_ip = proxy_ip.split('//')[1]
    proxy = {'https': proxy_ip, 'http': proxy_ip}
    return proxy

'''
切换代理池,包括切换代理头，cookie和代理IP
'''
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

'''
python连接Oracle数据库的工具类
'''
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
        sql = "select ID_SEQ, TASK_URL from o1255_task_url_202004 where ID_SEQ NOT IN (select ID_SEQ FROM MT_MALL_DETAIL_202004) AND ID_SEQ > 15000 AND ID_SEQ <=100000"

        result = cursor.execute(sql)
        data = result.fetchall()
        cursor.close()
        conn.close()
        return data
    """
    保存采集到的页面
    """
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
        cursor.close()
        conn.close()

    """
        标记不存在的页面的URL
     """
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
        print('end')
        cursor.close()
        conn.close()

    """
        获取数据中保存的页面
    """
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




"""
爬取店铺详情页面
"""
def get_shop_info(url,code):
    if code == 1:
        global  g_user_agent
        global g_proxy
        global g_cookie
        g_user_agent,g_proxy,g_cookie = get_agent_proxies()
        print(url,g_user_agent,g_proxy,g_cookie)
    headers = {
        'Host': 'i.meituan.com',
        'User-Agent': g_user_agent,
        'Cookie': g_cookie
    }
    global session
    try:
        response = session.get(url,headers=headers,proxies=g_proxy,timeout=50)
        response.encoding='utf-8'
        status_code = response.status_code
        text = response.text
        if status_code == 403:
            session = requests.session()
            get_shop_info(url, 1)
        if '很抱歉，您要访问的页面不存在' in text:
            print(text)
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

"""
解析数据库中不存的页面
"""
def analysis_page(data):
    decompressor = zlib.decompressobj()
    decompressed = decompressor.decompress(data) # 这里只解压压缩的数据
    decompressed.decode ('utf-8')
    print(decompressed)


connection = OracleUtil()
session = requests.Session()
g_user_agent = random.choice(USER_AGENTS)
g_proxy = get_proxy()
g_cookie = random.choice(MT_COOKIE)
def main():
    data = connection.get_url()
    for url_tuple in data:
        print('begin')
        time.sleep(1)
        id_seq = url_tuple[0]
        url = url_tuple[1]
        print(id_seq,url)
        data = []
        global session
        data_text = get_shop_info(url,0)
        if 'not_exist' == data_text:
            data.append((id_seq, url))
            connection.save_page_not_exist(data)
            g_user_agent, g_proxy, g_cookie = get_agent_proxies()
            print('page_not_exist', g_user_agent, g_proxy, g_cookie)
            session = requests.Session()
        elif 'time_out' == data_text:
            data.append((id_seq, url))
            connection.save_page_not_exist(data)
            g_user_agent, g_proxy, g_cookie = get_agent_proxies()
            print('time_out', g_user_agent, g_proxy, g_cookie)
            session = requests.Session()
        else:
            data.append((id_seq, data_text))
            connection.save_page(data)
if __name__ == '__main__':
    main()
    # get_agent_proxies()
    # data = connection.get_page()
    # analysis_page(data)