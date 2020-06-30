import json
import random
import re
import socket
import ssl
import time
import urllib

import OpenSSL
import requests
import urllib3

from agent_util import AgentPoolUtil
from cookie_util import get_cookie
from date_util import get_timestamp

ip_pool = AgentPoolUtil()
g_proxy = ip_pool.get_high_proxy()
user_agent = ip_pool.get_user_agent()
headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Cookie': 'ITARANCELTEMPSESSION=K4fpp6HQvbxr1Yhw7LPV8hCj1RbtmqGDVbTpBzdQ1RSVdc4sC34jYNJ3FmlNRnN61nvTYxpnQZGrq0fm7SmPRppt93YPTn6x11Bk4zt2bst7qFn3PcGPRbSJYLQTNWGyLXJylZhLqRFQ8rMhbM7vkfB6FLJvMhG45lwbxBnjtC0dP91KWkJGgJTfc1f9vRLvLz9JtFj1TJVKVJhpJx41PGDhGG1T69jJGGwQyh33N82T2hnlnkvMPyljQVQt1JrP!-1777146076!-974476542; TS01577d4a=014dc399cbff204f010551a7ddd306a8f65eb123fc1a83e2f422909a4d74c80ff9a814b633866811cc1cb585ee9b70e002917e0472d476d6372ed4f5474929a3170c1a19a1',
        'Host': 'www.aduanet.gob.pe',
        'Pragma': 'no-cache',
        'Referer': 'http://www.aduanet.gob.pe/itarancel/arancelS01Alias',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36',
    }
cookie = get_cookie()
if len(cookie) > 0:
    headers['Cookie'] = cookie
    headers['User-Agent'] = user_agent

def get_buscarPartida(url, code):
    if code > 0:
        global g_proxy
        global user_agent
        g_proxy = ip_pool.get_high_proxy()
        user_agent = ip_pool.get_user_agent()
        headers['User-Agent'] = user_agent
    # url = 'http://www.aduanet.gob.pe/itarancel/arancelS01Alias?accion=buscarPartida&esframe=1&cod_partida=101210000'
    cod_partida = re.compile(r'cod_partida=(\d*)').findall(url)
    if len(cod_partida) > 0:
        cod_partida = cod_partida[0]
    else:
        print(f'错误的url={url}')
        return 'failed'

    real_url = "http://www.aduanet.gob.pe/itarancel/JSPDetallePartidaArancel.jsp"
    headers['Referer'] = f'http://www.aduanet.gob.pe/itarancel/arancelS01Alias?accion=buscarPartida&esframe=1&cod_partida={cod_partida}'

    try:
        # print(f'g_proxy={g_proxy}')
        response = requests.request("GET", real_url, headers=headers, proxies=g_proxy)
        response.encoding = 'utf-8'
        status_code = response.status_code
        text = response.text

        if status_code == 403:
            print(f'status_code={status_code}')
            text = 'failed'

        if status_code == 500 or 'Error 500--Internal Server Error' in text:
            print("Error 500--Internal Server Error!")
            text = 'failed'

        if 'Pagina de Errores' in text:
            print("Pagina de Errores！")
            text = 'failed'

        # # print(text)
        # else:
        if 'img1on = new Image()' not in text and 'Error 500--Internal Server Error' not in text:
            print(f'text={text}')
            text = 'failed'
        if 'Pagina de Errores' in text:
            text = 'failed'
        if 'Error 500--Internal Server Error' in text:
            text = 'failed'
        return text

    except socket.timeout as e:
        print('ConnectionResetError')
        get_buscarPartida(url, 1)
    except requests.exceptions.ReadTimeout as e:
        print('ConnectionResetError')
        return 'time_out'
    except ConnectionResetError as e:
        print('ConnectionResetError')
        get_buscarPartida(url, 1)
    except urllib3.exceptions.MaxRetryError as e:
        print('urllib3.exceptions.MaxRetryError')
        get_buscarPartida(url, 1)
    except requests.exceptions.ProxyError as e:
        print('requests.exceptions.ProxyError')
        get_buscarPartida(url, 1)
    except OpenSSL.SSL.SysCallError as e:
        print('OpenSSL.SSL.SysCallError')
        get_buscarPartida(url, 1)
    except ssl.SSLError as e:
        print('ssl.SSLError')
        get_buscarPartida(url, 1)
    except requests.exceptions.SSLError as e:
        print('requests.exceptions.SSLError')
        get_buscarPartida(url, 1)
    except OpenSSL.SSL.WantReadError as e:
        print('OpenSSL.SSL.WantReadError')
        get_buscarPartida(url, 1)
    except requests.exceptions.ConnectionError as e:
        print('OpenSSL.SSL.WantReadError')
        get_buscarPartida(url, 1)
    except OSError as e:
        print('OSError')
        get_buscarPartida(url, 1)
    except urllib.error.URLError as e:
        print('urllib.error.URLError')
        get_buscarPartida(url, 1)


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
        time.sleep(random.randint(5, 10))
        content = get_buscarPartida(sub.get('url'), 0)
        # print(content)
        if content == 'failed':
            fail_counter += 1
            print(f'TASK_URL={sub.get("url")}')
            # 返回页面中显示页面不存在3三次任务该cookie失效，更新cookie失效的时间并切换cookie
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
                "publishTime": sub.get('publishTime') if sub.get('publishTime') is not None else get_timestamp(),
                "publisherId": sub.get('publisherId'),
                "purl": "0000",
                "responseHeaders": {
                    "X-API-TOKEN": 'aaaa',
                    "connection": 'Keep-Alive',
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
            success_url.append((get_timestamp(), sub.get('url')))

    result_total = result_total - fail_counter

    if fail_counter != 0:
        print("爬取失败[ %d ]个页面！" % (fail_counter))
        # connection.mark_not_exit_url(fail_url)

    if result_total == 0:
        return (success_url, result_total)
    else:
        return_data = {
            "data": prev_data,
            "total": result_total
        }
        # print(json.dumps(return_data))
        return (success_url, return_data)
