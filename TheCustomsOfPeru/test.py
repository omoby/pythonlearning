import re
import socket
import ssl
import time
import urllib

import OpenSSL
import requests
import urllib3

from TheCustomsOfPeru.agent_util import AgentPoolUtil
from TheCustomsOfPeru.date_util import get_timestamp
from TheCustomsOfPeru.encrypt_util import get_secret

ip_pool = AgentPoolUtil()
# proxy = ip_pool.get_high_proxy()
#
# print(proxy)
#
# secret = get_secret(str(get_timestamp()))
# print(secret)
#
#
# def get_detail(url, code):
#     print(code)
#     code += 1
#     if code > 2:
#         print('-----')
#         return 'failed'
#     # url = 'http://www.aduanet.gob.pe/itarancel/arancelS01Alias?accion=consultarConvenio&cod_partida=201300010'
#     # cod_partida = re.compile(r'cod_partida=(\d*)').findall(url)
#     # if len(cod_partida) > 0:
#     #     cod_partida = cod_partida[0]
#     # else:
#     #     print(f'错误的url={url}')
#     #     return 'failed'
#     # real_url = "http://www.aduanet.gob.pe/itarancel/arancelS01Alias"
#     #
#     # querystring = {"accion": "consultarConvenio", "cod_partida": cod_partida}
#     #
#     # headers = {
#     #     'Connection': "keep-alive",
#     #     'Pragma': "no-cache",
#     #     'Cache-Control': "no-cache",
#     #     'Upgrade-Insecure-Requests': "1",
#     #     'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36",
#     #     'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
#     #     'Referer': "http://www.aduanet.gob.pe/itarancel/JSPDetallePartidaArancel.jsp",
#     #     'Accept-Encoding': "gzip, deflate",
#     #     'Accept-Language': "zh-CN,zh;q=0.9",
#     #     'Cookie': "TS01577d4a=014dc399cbcb104fe745c7a43d95e4ac429ffa1a2e5537e47dc75cc27e20f268de10d446394026cafc6fa5e642b87c306d3a68d9bd197cb1242b96b3ae8b5bf8dd11f2919b; ITARANCELTEMPSESSION=z3n7p4HTJnCk1FxTY1fb1JlNLJBGZfzXzvBYgbdZykhJL7wn97G3JkvSb01LYrT4Qz0TKTLRCvyVGkvYFGhdGxhLWQLxfzhdhQwpK2yT3mDwlQYgXzHhshHH2fTm6d2fzSxsNJD4Fy10n3hJrWhbykFp4QLyWkXLxq0z6tvCw9wLY2TJ6mKj0n9v6TRx7bmBX1Kmt3gjyQnzhTQn82wLwQzkqVgvh9VTBfx2L2nG3G11yTCyqZ95sVJn92hnCvTd!-1653864741!1337442711",
#     #     'cache-control': "no-cache",
#     #     'Postman-Token': "af56dd47-b86b-482a-af29-99e9966197f8"
#     # }
#     #
#     # global session
#     try:
#         # response = session.get(real_url, headers=headers, params=querystring)
#         # response.encoding = 'utf-8'
#         # status_code = response.status_code
#         # text = response.text
#         status_code = 403
#         text = ''
#         if status_code == 403:
#             # session = requests.Session()
#             get_detail(url, code)
#         if 'Pagina de Errores' in text:
#             print("Pagina de Errores！")
#             get_detail(url, code)
#         # print(text)
#         return text
#
#     except socket.timeout as e:
#         print('ConnectionResetError')
#         get_detail(url, code)
#     except requests.exceptions.ReadTimeout as e:
#         print('ConnectionResetError')
#         return 'time_out'
#     except ConnectionResetError as e:
#         print('ConnectionResetError')
#         get_detail(url, code)
#     except urllib3.exceptions.MaxRetryError as e:
#         print('urllib3.exceptions.MaxRetryError')
#         get_detail(url, code)
#     except requests.exceptions.ProxyError as e:
#         print('requests.exceptions.ProxyError')
#         get_detail(url, code)
#     except OpenSSL.SSL.SysCallError as e:
#         print('OpenSSL.SSL.SysCallError')
#         get_detail(url, code)
#     except ssl.SSLError as e:
#         print('ssl.SSLError')
#         get_detail(url, code)
#     except requests.exceptions.SSLError as e:
#         print('requests.exceptions.SSLError')
#         get_detail(url, code)
#     except OpenSSL.SSL.WantReadError as e:
#         print('OpenSSL.SSL.WantReadError')
#         get_detail(url, code)
#     except requests.exceptions.ConnectionError as e:
#         print('OpenSSL.SSL.WantReadError')
#         get_detail(url, code)
#     except OSError as e:
#         print('OSError')
#         get_detail(url, code)
#     except urllib.error.URLError as e:
#         print('urllib.error.URLError')
#         get_detail(url, code)
#
#
# url = 'http://www.aduanet.gob.pe/itarancel/arancelS01Alias?accion=consultarConvenio&cod_partida=201300010'
# cod_partida = re.compile(r'cod_partida=(\d*)').findall(url)
# if len(cod_partida) > 0:
#     cod_partida = cod_partida[0]
# else:
#     print(f'错误的url={url}')
# content = 'failed'
# content = get_detail(url, 0)
# print(content)
# if 'failed' == content:
#     print(1)
# ip = proxy['https'].split(":")[0]
#
# url = 'http://ip.ws.126.net/ipquery?ip='+ip
# resp = requests.get(url)
# print(resp.text)
# member = "\xe6\x8f\x90\xe5\x8f\x96\xe5\xa4\xaa\xe9\xa2\x91\xe7\xb9\x81,\xe8\xaf\xb7\xe6\x8c\x89\xe8\xa7\x84\xe5\xae\x9a\xe9\xa2\x91\xe7\x8e\x87\xe6\x8f\x90\xe5\x8f\x96!"
# print(str(member).encode('string-escape'))

for i in range(1, 10):
    proxy = ip_pool.get_high_proxy()
    print(i)
    print(proxy)
