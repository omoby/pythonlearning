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

from TheCustomsOfPeru.agent_util import AgentPoolUtil
from TheCustomsOfPeru.cookie_util import get_cookie
from TheCustomsOfPeru.date_util import get_timestamp

ip_pool = AgentPoolUtil()
# g_proxy = ip_pool.get_high_proxy()
# user_agent = ip_pool.get_user_agent()
# print(f'proxy={proxy}')

# start = time.time()
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Cookie': 'TS01577d4a=014dc399cbff204f010551a7ddd306a8f65eb123fc1a83e2f422909a4d74c80ff9a814b633866811cc1cb585ee9b70e002917e0472d476d6372ed4f5474929a3170c1a19a1; ITARANCELTEMPSESSION=ZKKzp6LH4xC5y6sZVC1C18y54xYpyYRdkghtG1JRBd7W4kv8VHl7lnB1X1j11yX3dssYtCrXSrXtPWtb21SdYwnk5w9vn2ZzF02sXCnVJRJLPQgQJGc5yKjJKppvHDrsSMlfWGbnPwNybnxQNQYHGs7PsvPDL3108XtLc1tyh3M1rsBxcTvHb2yyBcv88CFhcyKBsPssRQxvkjJfZmbWZknMtLk40qyNSlyvT8J3RGvmBpLmHQWL0nf8chZGjFRv!-1653864741!1337442711',
    'Host': 'www.aduanet.gob.pe',
    'Pragma': 'no-cache',
    'Referer': 'http://www.aduanet.gob.pe/itarancel/JSPDetallePartidaArancel.jsp',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36',
}
# print(headers)
cookie = get_cookie()
if len(cookie) > 0:
    headers['Cookie'] = cookie
    # headers['User-Agent'] = user_agent
# print(headers)
'''
抓取mt店铺详情页
'''


def get_consultarConvenio(url, code):
    # print(code)
    # global start
    # end = time.time()
    # if end - start > 1 * 60:
    #     global g_proxy
    #     global user_agent
    #     g_proxy = ip_pool.get_high_proxy()
    #     user_agent = ip_pool.get_user_agent()
    #     headers['User-Agent'] = user_agent
    #     start = end
    # if code > 0:
    #     g_proxy = ip_pool.get_high_proxy()
    #     user_agent = ip_pool.get_user_agent()
    #     headers['User-Agent'] = user_agent
    #     start = end
    # print(f'proxy={g_proxy}')
    # print(f'user_agent={user_agent}')
    # code += 1
    # url = 'http://www.aduanet.gob.pe/itarancel/arancelS01Alias?accion=consultarConvenio&cod_partida=201300010'
    cod_partida = re.compile(r'cod_partida=(\d*)').findall(url)
    if len(cod_partida) > 0:
        cod_partida = cod_partida[0]
    else:
        print(f'错误的url={url}')
        return 'failed'
    real_url = "http://www.aduanet.gob.pe/itarancel/arancelS01Alias"

    querystring = {"accion": "consultarConvenio", "cod_partida": cod_partida}

    try:
        # print(g_proxy)
        # print(headers)
        response = requests.get(real_url, headers=headers, params=querystring)
        response.encoding = 'utf-8'
        status_code = response.status_code
        text = response.text
        if status_code == 500:
            print(f'status={status_code}')
            text = 'failed'
        if status_code == 403:
            print(f'status={status_code}')
            text = 'failed'
        if 'Pagina de Errores' in text:
            print("Pagina de Errores！")
            text = 'failed'
        return text

    except socket.timeout as e:
        print('ConnectionResetError')
        get_consultarConvenio(url, 1)
    except requests.exceptions.ReadTimeout as e:
        print('ConnectionResetError')
        return 'time_out'
    except ConnectionResetError as e:
        print('ConnectionResetError')
        get_consultarConvenio(url, 1)
    except urllib3.exceptions.MaxRetryError as e:
        print('urllib3.exceptions.MaxRetryError')
        get_consultarConvenio(url, 1)
    except requests.exceptions.ProxyError as e:
        print('requests.exceptions.ProxyError')
        get_consultarConvenio(url, 1)
    except OpenSSL.SSL.SysCallError as e:
        print('OpenSSL.SSL.SysCallError')
        get_consultarConvenio(url, 1)
    except ssl.SSLError as e:
        print('ssl.SSLError')
        get_consultarConvenio(url, 1)
    except requests.exceptions.SSLError as e:
        print('requests.exceptions.SSLError')
        get_consultarConvenio(url, 1)
    except OpenSSL.SSL.WantReadError as e:
        print('OpenSSL.SSL.WantReadError')
        get_consultarConvenio(url, 1)
    except requests.exceptions.ConnectionError as e:
        print('OpenSSL.SSL.WantReadError')
        get_consultarConvenio(url, 1)
    except OSError as e:
        print('OSError')
        get_consultarConvenio(url, 1)
    except urllib.error.URLError as e:
        print('urllib.error.URLError')
        get_consultarConvenio(url, 1)


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
    sucess_counter = 0
    for sub in result_data:
        time.sleep(random.randint(5, 10))
        content = get_consultarConvenio(sub.get('url'), 0)
        counter = 0
        while content == 'failed' and counter < 10:
            counter += 1
            content = get_consultarConvenio(sub.get('url'), 0)
        if counter >= 10:
            print(f'采集失败,TASK_URL={sub.get("url")}')
            continue
        else:
            sucess_counter += 1
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

    fail_counter = result_total - sucess_counter

    if fail_counter != 0:
        print("爬取失败[ %d ]个页面！" % (fail_counter))
        # connection.mark_not_exit_url(fail_url)

    if sucess_counter == 0:
        return (success_url, result_total)
    else:
        return_data = {
            "data": prev_data,
            "total": sucess_counter
        }
        # print(json.dumps(return_data))
        return (success_url, return_data)
