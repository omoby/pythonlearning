import json
import socket
import ssl

import OpenSSL
import requests
import urllib3


from MTStoreDetail.date_util import get_timestamp
from MTStoreDetail.oracle_util import OracleUtil
from MTStoreDetail.agent_util import  AgentPoolUtil

agent_pool_util = AgentPoolUtil()
g_user_agent = agent_pool_util.get_user_agent()
g_proxy = agent_pool_util.get_proxy()
g_cookie = agent_pool_util.get_cookie()
session = requests.Session()
connection = OracleUtil()

'''
抓取mt店铺详情页
'''
def get_shop_info(url,code):
    if code == 1:
        global  g_user_agent
        global g_proxy
        global g_cookie
        g_proxy = agent_pool_util.get_proxy()
        g_user_agent = agent_pool_util.get_user_agent()
        print("切换代理IP和User Agent成功!")
    headers = {
        'Host': 'm.dianping.com',
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
            print("页面不存在！")
            return 'not_exist'
        if '验证中心' in text:
            print("验证中心！")
            return 'not_exist'
        # print(text)
        return text

    except socket.timeout as e:
        print('ConnectionResetError')
        get_shop_info(url, 1)
    except requests.exceptions.ReadTimeout as e:
        print('ConnectionResetError')
        return 'time_out'
    except ConnectionResetError as e:
        print('ConnectionResetError')
        get_shop_info(url, 1)
    except urllib3.exceptions.MaxRetryError as e:
        print('urllib3.exceptions.MaxRetryError')
        get_shop_info(url, 1)
    except requests.exceptions.ProxyError as e:
        print('requests.exceptions.ProxyError')
        get_shop_info(url, 1)
    except OpenSSL.SSL.SysCallError as e:
        print('OpenSSL.SSL.SysCallError')
        get_shop_info(url, 1)
    except ssl.SSLError as e:
        print('ssl.SSLError')
        get_shop_info(url, 1)
    except requests.exceptions.SSLError as e:
        print('requests.exceptions.SSLError')
        get_shop_info(url, 1)
    except OpenSSL.SSL.WantReadError as e:
        print('OpenSSL.SSL.WantReadError')
        get_shop_info(url, 1)
    except requests.exceptions.ConnectionError as e:
        print('OpenSSL.SSL.WantReadError')
        get_shop_info(url, 1)

'''
构造需要向download api提交的数据
'''
def get_json_data(data):
    json_data = data
    result_total = json_data.get('result').get('total')
    result_data = json_data.get('result').get('data')
    prev_data = []
    fail_url = []
    success_url = []
    fail_counter = 0
    for sub in result_data:

        content = get_shop_info(sub.get('url'),0)
        if 'not_exist' == content:
            fail_url.append((get_timestamp(),sub.get('url')))
            fail_counter += 1
            print('not_exist_counter=%d' % (fail_counter))
            if fail_counter % 3 == 0:
                global g_cookie
                g_cookie =  agent_pool_util.get_cookie()
                print('切换Cooki成功！')
        else:
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
              "publishTime": sub.get('publishTime') if sub.get('publishTime') is not None else 0,
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
            success_url.append((get_timestamp(),sub.get('url')))

    result_total = result_total - fail_counter

    if fail_counter != 0:
        print("爬取失败[ %d ]个页面！" %(fail_counter))
        connection.mark_not_exit_url(fail_url)

    if result_total == 0:
        return (success_url,result_total)
    else:
        return_data = {
            "data": prev_data,
            "total": result_total
        }
        # print(json.dumps(return_data))
        return (success_url,return_data)



