import json
import urllib.parse

import requests
import time
import locale
import hmac
import base64
from hashlib import sha256
import http.client

import urllib3
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

from DPCrawler.config import PROXY_POOL, MT_6_COOKIE
from DPCrawler.setting import USER_AGENTS


user = "inspur"
# user = "tianyancha"
# key = '6vs7fTpvL6FLtcEfWbz2AHITlISnCjFO'
key = "eqGRl7KlipogzCWXt5lvKRbgOAOOcdj8"



def  get_timestamp():
    return int(time.time() * 1000 )

def get_proxy():
    proxy_pool_url = random.choice(PROXY_POOL)
    proxy_ip = urllib.request.urlopen(proxy_pool_url).read().decode("utf-8").split("\n")[1]
    if ',' in proxy_ip:
        proxy_ip = proxy_ip.split(',')[0]
    if 'http' in proxy_ip:
        proxy_ip = proxy_ip.split('//')[1]
    proxy = {'https': proxy_ip, 'http': proxy_ip}
    return proxy
def get_date():
    from datetime import datetime
    GMT_FORMAT = '%a, %d %b %Y %H:%M:%S GMT'

    return datetime.utcnow().strftime(GMT_FORMAT)

def get_secret(date):

    date = 'date: '+date
    appsecret = bytes(key, encoding = "utf8")
    data = bytes(date,encoding="utf8")  # 加密数据
    signature = base64.b64encode(hmac.new(appsecret, data, digestmod=sha256).digest())
    return signature.decode("utf8")
    # 获取十六进制加密数据
    # signature = base64.b64encode(hmac.new(appsecret, data, digestmod=sha256).hexdigest())
    # return signature


def get_url(task_id,task_intance,data_size):
    url = '172.22.5.243:30080'
    date = get_date()
    aut = 'hmac username="'+user+'", algorithm="hmac-sha256", headers="date", signature="'+get_secret(date)+'"'
    headers  ={
        'Date': date,
        'Authorization': aut,
        'X-API-TOKEN': 'sadb',
        'connection': 'Keep-Alive',
        'Accept': 'application/json',
        'user-agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1;SV1)'
    }
    # print(headers)
    # 与服务器建立链接
    conn = http.client.HTTPConnection(url)
    # 向服务器发送请求
    method = "GET"
    url = "http://172.22.5.243:30080/download-api/v1/requests/"+task_id+"/"+task_intance+"?user=" + user+"&size="+str(data_size)+"&ts=" + str(get_timestamp())
    # print(url)
    conn.request(method=method, url=url, headers=headers)
    # 获取响应消息体
    response = conn.getresponse()
    data = response.read()
    return (json.loads(data.decode("utf8")))

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
        'Cookie': g_cookie
    }
    global session
    try:
        response = session.get(url,headers=headers,proxies=g_proxy,timeout= 40)
        response.encoding='utf-8'
        status_code = response.status_code
        text = response.text
        # print(text)
        if status_code == 403:
            session = requests.Session()
            get_shop_info(url, 1)
        if '很抱歉，您要访问的页面不存在' in text:
            return 'not_exist'
        # print(response.text)
        return response.text
        # return  zlib.compress(response.content)
    except socket.timeout as e:
        print(e.errno)
        print('ConnectionResetError')
        get_shop_info(url, 1)
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
    except OpenSSL.SSL.WantReadError as e:
        print(e.errno)
        print('OpenSSL.SSL.WantReadError')
        get_shop_info(url, 1)
    except requests.exceptions.ConnectionError as e:
        print(e.errno)
        print('OpenSSL.SSL.WantReadError')
        get_shop_info(url, 1)

def get_json_data(data):
    json_data = data
    result_total = json_data.get('result').get('total')
    result_data = json_data.get('result').get('data')
    prev_data = []
    fail_counter = 0
    for sub in result_data:
        content = get_shop_info(sub.get('url'),0)
        if 'not_exist' == content:
            fail_counter += 1
            print('not_exist_counter=%d' % (fail_counter))
            if fail_counter % 5 == 0:
                global g_cookie
                g_cookie = random.choice(MT_6_COOKIE)
                print('page_not_exist', g_cookie)
            print('page_not_exist')
        else:
            # print(content)
            data = {
              "attemptCount": sub.get('attemptCount'),
              "content": content,
              "currentDepth": sub.get('currentDepth'),
              "downloadTime": get_timestamp(),
              "downloadTool": sub.get('downloadTool'),
              "failureCount": sub.get('failureCount'),
              "httpMethodName": sub.get('httpMethodName'),
              "httpStatus": 200,
              "markId": sub.get('markId'),
              "maxDepth": sub.get('maxDepth'),
              "other": {
                "additionalProp1": "string",
                "additionalProp2": "string",
                "additionalProp3": "string"
              },
              "parentTraceId": sub.get('parentTraceId'),
              "publishTime": sub.get('publishTime') if sub.get('publishTime') is None else 0,
              "publisherId": sub.get('publisherId'),
              "purl": "0000",
              "responseHeaders": {
                  "X-API-TOKEN":'aaaa',
                  "connection":'Keep-Alive',
                  "user-agent": "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1;SV1)",
                  "Content-Type": "application/json"
              },
              "ruleId": sub.get('ruleId'),
              "taskId": sub.get('taskId'),
              "taskInstanceId": sub.get('taskInstanceId'),
              "traceId": sub.get('traceId'),
              "url": sub.get('url'),
              "urlType": sub.get('urlType')
            }
            prev_data.append(data)
    result_total = result_total - fail_counter
    print(result_total)
    if result_total == 0:
        result_total
    else:
        return_data = {
            "data": prev_data,
            "total": result_total
        }
        return json.dumps(return_data)

def  post_result(body):
    server_url = '172.22.5.243:30080'
    date = get_date()

    aut = 'hmac username="' + user + '", algorithm="hmac-sha256", headers="date", signature="' + get_secret(date) + '"'
    headers = {
        'Date': date,
        'Authorization': aut,
        'X-API-TOKEN': 'sadb',
        'connection': 'Keep-Alive',
        'Content-Type': 'application/json',
        'Accept':'application/json',
        'user-agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1;SV1)'
    }
    # 与服务器建立链接
    conn = http.client.HTTPConnection(server_url)
    # 向服务器发送请求
    method = "POST"
    post_url = 'http://172.22.5.243:30080/download-api/v1/results?ts='+str(get_timestamp())+"&user="+user
    # print(url)
    conn.request(method=method, url=post_url, body=body, headers=headers)
    # 获取响应消息体
    response = conn.getresponse()
    status = response.status
    print(status)
    while status != 201:
        conn = http.client.HTTPConnection(server_url)
        conn.request(method=method, url=post_url, body=body, headers=headers)
        # 获取响应消息体
        # response = conn.getresponse()
        status = response.status
        print('in',response.status)
    data = response.read()
    print(data.decode("utf8"))

    # 获取响应头部信息，列表形式
    resheader = response.getheaders()
    print(resheader)

    # 取出响应头部的Set-Cookie的值
    responsehead = response.getheader('Set-Cookie')
    print(responsehead)

g_user_agent = random.choice(USER_AGENTS)
g_proxy = get_proxy()
g_cookie = random.choice(MT_6_COOKIE)
session = requests.Session()

def main():
    task_id = "1255"
    task_instance  = "a3c8352c-c239-4a29-80cc-68454bb5eb59"
    index = 0
    while index < 10:
        data = get_url(task_id,task_instance,data_size=10)
        body = get_json_data(data)
        if body == 0:
            pass
        else:
            post_result(body)
            index += 1
            print("index=%d" %(index))
if __name__ == '__main__':
    main()