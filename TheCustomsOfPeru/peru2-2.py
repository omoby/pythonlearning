import socket
import ssl
import urllib

import OpenSSL
import requests


# url = "http://www.aduanet.gob.pe/itarancel/arancelS01Alias"
#
# querystring = {"accion":"consultarConvenio","cod_partida":"201300010"}
# url = 'http://www.aduanet.gob.pe/itarancel/arancelS01Alias?accion=consultarConvenio&cod_partida=202200000'
# headers = {
#     'Connection': "keep-alive",
#     'Pragma': "no-cache",
#     'Cache-Control': "no-cache",
#     'Upgrade-Insecure-Requests': "1",
#     'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36",
#     'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
#     'Referer': "http://www.aduanet.gob.pe/itarancel/JSPDetallePartidaArancel.jsp",
#     'Accept-Encoding': "gzip, deflate",
#     'Accept-Language': "zh-CN,zh;q=0.9",
#     'Cookie': "TS01577d4a=014dc399cb1605ff7b2daabb19539ee4c0b34fe4a5bb4ea536574dea4ed99cd5cc63a41b913435206c40539f7d71e45b65684fad9752f0c65627f68c71ef81ed1210fbd538; ITARANCELTEMPSESSION=K62hp4TKPvjk7bfM5qhxg9hR7gnbZFBhvYsvk9Kf2Mym7G9q5xDVw5Zx9F9PmBLjLDhvbF0jDfwnRDk3Xq0mw0dxb0rSYh71Ls0J2T48LYrgzpwStGtbmG9QLwHXhTZRpcVX5DQ8gw6QG3YYv1pww7b0LTzvHvhkpCs1QZZ1xCgMs8BkqPHwynR2w9lVVFLBV2cKlJp4pVsfMH24CfjWMJ5sy1y77BwnZkZx1gDLx5L4xTdddBg9r1JgkCVjRyYT!-1653864741!1337442711",
#
#     }

# response = requests.request("GET", url, headers=headers)
#
# print(response.text)
import urllib3
session = requests.Session()

def get_detail(url, code):
    # url = 'http://www.aduanet.gob.pe/itarancel/arancelS01Alias?accion=consultarConvenio&cod_partida=201300010'
    #
    url = "http://www.aduanet.gob.pe/itarancel/arancelS01Alias"

    querystring = {"accion": "consultarConvenio", "cod_partida": "803901900"}

    headers = {
        'Connection': "keep-alive",
        'Pragma': "no-cache",
        'Cache-Control': "no-cache",
        'Upgrade-Insecure-Requests': "1",
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36",
        'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        'Referer': "http://www.aduanet.gob.pe/itarancel/JSPDetallePartidaArancel.jsp",
        'Accept-Encoding': "gzip, deflate",
        'Accept-Language': "zh-CN,zh;q=0.9",
        'Cookie': "ITARANCELTEMPSESSION=HdB2p4JbMbh3WqsM49vf32VW5PLnbvgqhhgrhRjN8kSDp2VSy2ZL6P2Gt5M7hfYmLTR0V2zQL2nYSZnzNpZzGDnN0QbdCWN4pnn2g651LYN0yqBKpRfs2p1Q1dYpYPQzZnvfd9rvJMG97wpVlM2jyvZnC6mKhB3fW93VXh5xRy9PS90CGd7WQs6CP8nGnr6yCkpTXlkGHDW01GGDZ9J7bLRSmcXDgW7GC2Fgsc8wNTTGhMhn46lFLG1SVz6wTFLh!-1777146076!789637656; TS01577d4a=014dc399cbf9017246dd8af8f77b5901bc6b0d2ca8bcb4c5055e51aed2d2d1423d6bde2e0e842dd753ac0e4f08775ed9c2b4c2a1e8a0116994c4463265be884a5762624153",
        'cache-control': "no-cache",
        'Postman-Token': "b5b68732-ec56-4b87-8355-473f179ab5d2"
    }

    global session
    try:
        response = session.get(url, headers=headers,params=querystring)
        response.encoding = 'utf-8'
        status_code = response.status_code
        text = response.text
        if status_code == 403:
            session = requests.Session()
            get_detail(url, 1)
        if 'Pagina de Errores' in text:
            print("Pagina de Errores！")
            get_detail(url, 1)
        print(text)
        # return text

    except socket.timeout as e:
        print('ConnectionResetError')
        get_detail(url, 1)
    except requests.exceptions.ReadTimeout as e:
        print('ConnectionResetError')
        return 'time_out'
    except ConnectionResetError as e:
        print('ConnectionResetError')
        get_detail(url, 1)
    except urllib3.exceptions.MaxRetryError as e:
        print('urllib3.exceptions.MaxRetryError')
        get_detail(url, 1)
    except requests.exceptions.ProxyError as e:
        print('requests.exceptions.ProxyError')
        get_detail(url, 1)
    except OpenSSL.SSL.SysCallError as e:
        print('OpenSSL.SSL.SysCallError')
        get_detail(url, 1)
    except ssl.SSLError as e:
        print('ssl.SSLError')
        get_detail(url, 1)
    except requests.exceptions.SSLError as e:
        print('requests.exceptions.SSLError')
        get_detail(url, 1)
    except OpenSSL.SSL.WantReadError as e:
        print('OpenSSL.SSL.WantReadError')
        get_detail(url, 1)
    except requests.exceptions.ConnectionError as e:
        print('OpenSSL.SSL.WantReadError')
        get_detail(url, 1)
    except OSError as e:
        print('OSError')
        get_detail(url, 1)
    except urllib.error.URLError as e:
        print('urllib.error.URLError')
        get_detail(url, 1)


def main():
    get_detail('', 0)


if __name__ == '__main__':
    main()
