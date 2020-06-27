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

    # aut = 'hmac username="' + user + '",algorithm="hmac-sha256",headers="date",signature="' + str( get_secret(date))
    aut = 'hmac username="'+user+'", algorithm="hmac-sha256", headers="date", signature="'+get_secret(date)+'"'
    # print(aut)
    # aut = json.dumps({
    #     "hmac username":user,
    #     "algorithm":"hmac-sha256",
    #     "headers":"date",
    #     "signature":str(get_secret(date))
    # })

    # print(aut)
    # headers = {
    #     "Host":"172.22.5.243:30080",
    #     "connection": "Keep-Alive",
    #     "user-agent": "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1;SV1)",
    #     "Accept": 'application/json',
    #     "Authorization": aut,
    #     'Content-Type': 'application/json',
    #     "X-API-TOKEN": 'aaaa',
    #     "Date": date,
    # }
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
    print(url)
    conn.request(method=method, url=url, headers=headers)
    # 获取响应消息体
    response = conn.getresponse()

    # print(response.status, response.reason)
    data = response.read()
    return (json.loads(data.decode("utf8")))

    # # 获取响应头部信息，列表形式
    # resheader = response.getheaders()
    # print(resheader)
    #
    # # 取出响应头部的Set-Cookie的值
    # responsehead = response.getheader('Set-Cookie')
    # print(responsehead)


def get_json_obj(sub_data):
    print(sub_data)
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
        'Cookie': g_cookie
        # 'Cookie':'au_trace_key_net=default;_lxsdk=925D202C34254B4BB548450110B9E3038AF16AF59236A3F2F4A9682B330AC601;service-off=0;channelType={%22default%22:%220%22};uuid=925D202C34254B4BB548450110B9E3038AF16AF59236A3F2F4A9682B330AC601;userId=730229479;token=hTCL2XB6aNmVJEmoMX8O1Z2Z6uQAAAAAjwoAAByXkOI0btfmSZ5boLN64kQ5gZQhy4lQSGHH7jJiDAwViHNv4YPuMfy-7XElmKUyJg;openh5_uuid=925D202C34254B4BB548450110B9E3038AF16AF59236A3F2F4A9682B330AC601;channelConfig={%22channel%22:%22default%22%2C%22type%22:0%2C%22fixedReservation%22:{%22reservationTimeStatus%22:0%2C%22startReservationTime%22:0%2C%22endReservationTime%22:0}};mt_c_token=hTCL2XB6aNmVJEmoMX8O1Z2Z6uQAAAAAjwoAAByXkOI0btfmSZ5boLN64kQ5gZQhy4lQSGHH7jJiDAwViHNv4YPuMfy-7XElmKUyJg;oops=hTCL2XB6aNmVJEmoMX8O1Z2Z6uQAAAAAjwoAAByXkOI0btfmSZ5boLN64kQ5gZQhy4lQSGHH7jJiDAwViHNv4YPuMfy-7XElmKUyJg;_lxsdk_cuid=1720b84753cc8-011b8a7b84bf26-2d604637-54600-1720b84753dc8;_lx_utm=utm_source%3D60066;_lxsdk_s=1720b84753e-3e5-861-d11%7C%7C6;iuuid=925D202C34254B4BB548450110B9E3038AF16AF59236A3F2F4A9682B330AC601;wm_order_channel=default;webloc_geo=36.674225%2C117.127767%2Cgcj02%2C-1;utm_source=;'
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
        # if '很抱歉，您要访问的页面不存在' in text:
        #     return 'not_exist'
        # print(response.text)
        return response.text
        # return  zlib.compress(response.content)
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

def get_json_data(data):
    # json_data  = json.loads(data)
    json_data = data
    result_total = json_data.get('result').get('total')
    result_data = json_data.get('result').get('data')
    prev_data = []
    for sub in result_data:
        # print(sub)
        content = get_shop_info(sub.get('url'),0)
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
    return_data = {
        "data": prev_data,
        "total": result_total
    }
    return json.dumps(return_data)

def  post_result(body):
    url = '172.22.5.243:30080'

    date = get_date()

    # aut = 'hmac username="' + user + '",algorithm="hmac-sha256",headers="date",signature="' + str( get_secret(date))
    aut = 'hmac username="' + user + '", algorithm="hmac-sha256", headers="date", signature="' + get_secret(date) + '"'
    # print(aut)
    # aut = json.dumps({
    #     "hmac username":user,
    #     "algorithm":"hmac-sha256",
    #     "headers":"date",
    #     "signature":str(get_secret(date))
    # })

    # print(aut)
    # headers = {
    #     "Host":"172.22.5.243:30080",
    #     "connection": "Keep-Alive",
    #     "user-agent": "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1;SV1)",
    #     "Accept": 'application/json',
    #     "Authorization": aut,
    #     'Content-Type': 'application/json',
    #     "X-API-TOKEN": 'aaaa',
    #     "Date": date,
    # }
    headers = {
        'Date': date,
        'Authorization': aut,
        'X-API-TOKEN': 'sadb',
        'connection': 'Keep-Alive',
        'Content-Type': 'application/json',
        'Accept':'application/json',
        'user-agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1;SV1)'
    }
    # print(headers)
    # 与服务器建立链接
    conn = http.client.HTTPConnection(url)
    # test_data = urllib.parse.urlencode(body)
    # 向服务器发送请求
    method = "POST"
    url = 'http://172.22.5.243:30080/download-api/v1/results?ts='+str(get_timestamp())+"&user="+user
    print(url)
    conn.request(method=method, url=url, body=body, headers=headers)
    # 获取响应消息体
    response = conn.getresponse()
    print(response.status, response.reason)
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
    # data = '{"code":10001,"msg":"获取成功","result":{"total":10,"data":[{"taskId":1255,"taskInstanceId":"e8ff5c74-0b93-4fe2-9c63-483a353b844e","url":"https://i.meituan.com/poi/1044108693","purl":"0000","traceId":"ab2c509f-e52e-4497-ab0c-24f3a1c1d57c","parentTraceId":"0e8f128d-6e46-4e2c-a8a0-30d069f0f846","markId":"B86E4AADA214D54F7169AE72AFB3D913","ruleId":null,"attemptCount":0,"maxDepth":10,"currentDepth":1,"httpMethodName":"GET","downloadTool":1,"failureCount":0,"urlType":"NAV","publishTime":null,"publisherId":null},{"taskId":1255,"taskInstanceId":"e8ff5c74-0b93-4fe2-9c63-483a353b844e","url":"https://i.meituan.com/poi/104410892","purl":"0000","traceId":"a5aebdf1-e955-44d5-8045-1842201422d5","parentTraceId":"c14adb20-a3fc-4628-964c-a16291990458","markId":"D1E69E8F09A915ECDD988742D4C0EBB9","ruleId":null,"attemptCount":0,"maxDepth":10,"currentDepth":1,"httpMethodName":"GET","downloadTool":1,"failureCount":0,"urlType":"NAV","publishTime":null,"publisherId":null},{"taskId":1255,"taskInstanceId":"e8ff5c74-0b93-4fe2-9c63-483a353b844e","url":"https://i.meituan.com/poi/1044112991","purl":"0000","traceId":"3335f293-d773-4ee8-8d77-cc5b92ed9e4c","parentTraceId":"d6aaa458-d1d7-4c19-b974-05545d94f544","markId":"7F170DA9FC7599EF1D79172161568B70","ruleId":null,"attemptCount":0,"maxDepth":10,"currentDepth":1,"httpMethodName":"GET","downloadTool":1,"failureCount":0,"urlType":"NAV","publishTime":null,"publisherId":null},{"taskId":1255,"taskInstanceId":"e8ff5c74-0b93-4fe2-9c63-483a353b844e","url":"https://i.meituan.com/poi/1044121209","purl":"0000","traceId":"7b673745-a8ce-4864-9e25-41dd0fabe893","parentTraceId":"d96ba118-8d1f-4c14-9717-519ecb2ecb46","markId":"98BA8743CCCAF863E77B7EA8D0A1FE82","ruleId":null,"attemptCount":0,"maxDepth":10,"currentDepth":1,"httpMethodName":"GET","downloadTool":1,"failureCount":0,"urlType":"NAV","publishTime":null,"publisherId":null},{"taskId":1255,"taskInstanceId":"e8ff5c74-0b93-4fe2-9c63-483a353b844e","url":"https://i.meituan.com/poi/1044126766","purl":"0000","traceId":"cc6dd23c-6190-4017-b4d9-6b500e4077e0","parentTraceId":"c31389b5-d755-49fd-b51d-569ed95d6213","markId":"4CB439E42E791305E70DA65236217CC5","ruleId":null,"attemptCount":0,"maxDepth":10,"currentDepth":1,"httpMethodName":"GET","downloadTool":1,"failureCount":0,"urlType":"NAV","publishTime":null,"publisherId":null},{"taskId":1255,"taskInstanceId":"e8ff5c74-0b93-4fe2-9c63-483a353b844e","url":"https://i.meituan.com/poi/104413083","purl":"0000","traceId":"f2ca0a90-da6a-454f-bd44-c1b51d16e430","parentTraceId":"64c2213c-8adb-4ab8-af31-754ec932c8fc","markId":"ED759983657EC3B330B77A66B886D6D5","ruleId":null,"attemptCount":0,"maxDepth":10,"currentDepth":1,"httpMethodName":"GET","downloadTool":1,"failureCount":0,"urlType":"NAV","publishTime":null,"publisherId":null},{"taskId":1255,"taskInstanceId":"e8ff5c74-0b93-4fe2-9c63-483a353b844e","url":"https://i.meituan.com/poi/1044131157","purl":"0000","traceId":"6ddc7165-6d6b-46da-9562-f16cd001307b","parentTraceId":"3aa0bdd2-2eee-47ee-a42e-8a6b414ee9fc","markId":"3447B0684663EAED1628A20792F62879","ruleId":null,"attemptCount":0,"maxDepth":10,"currentDepth":1,"httpMethodName":"GET","downloadTool":1,"failureCount":0,"urlType":"NAV","publishTime":null,"publisherId":null},{"taskId":1255,"taskInstanceId":"e8ff5c74-0b93-4fe2-9c63-483a353b844e","url":"https://i.meituan.com/poi/1044139892","purl":"0000","traceId":"513d013b-899d-4b6e-9fb9-7567fad17728","parentTraceId":"68af9548-3454-4b87-839c-58f5da5b6d3e","markId":"4E22093BEA72C90C64D8505AD19A23E9","ruleId":null,"attemptCount":0,"maxDepth":10,"currentDepth":1,"httpMethodName":"GET","downloadTool":1,"failureCount":0,"urlType":"NAV","publishTime":null,"publisherId":null},{"taskId":1255,"taskInstanceId":"e8ff5c74-0b93-4fe2-9c63-483a353b844e","url":"https://i.meituan.com/poi/1044146033","purl":"0000","traceId":"377572b2-9215-40b8-a323-c5fd8f7be9f4","parentTraceId":"df78901c-58eb-44bc-b4d5-b630fb812b5c","markId":"F919E1622479577800F6D56FBE54D814","ruleId":null,"attemptCount":0,"maxDepth":10,"currentDepth":1,"httpMethodName":"GET","downloadTool":1,"failureCount":0,"urlType":"NAV","publishTime":null,"publisherId":null},{"taskId":1255,"taskInstanceId":"e8ff5c74-0b93-4fe2-9c63-483a353b844e","url":"https://i.meituan.com/poi/104414817","purl":"0000","traceId":"695820cc-a769-458b-9508-d979b58e53f6","parentTraceId":"a59ba682-7844-44bf-990e-a50099fe3ac1","markId":"7087892A38DC53ED38E1F50EA64BF315","ruleId":null,"attemptCount":0,"maxDepth":10,"currentDepth":1,"httpMethodName":"GET","downloadTool":1,"failureCount":0,"urlType":"NAV","publishTime":null,"publisherId":null}]}}'
    # date = get_date()
    # get_secret(date)
    task_id = "1255"
    task_instance  = "a3c8352c-c239-4a29-80cc-68454bb5eb59"

    data = get_url(task_id,task_instance,data_size=1)
    # print(type(data))
    # print(data)
    # print(get_secret('a'))
    # print(g_user_agent,g_proxy,g_cookie)
    body = get_json_data(data)
    print(body)
    post_result(body)
    # print(get_timestamp())
if __name__ == '__main__':
    main()