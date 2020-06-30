def get_cookie():
    with open('cookie.txt') as f:
        cookie = f.read()
    # headers = {
    #     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    #     'Accept-Encoding': 'gzip, deflate',
    #     'Accept-Language': 'zh-CN,zh;q=0.9',
    #     'Cache-Control': 'no-cache',
    #     'Connection': 'keep-alive',
    #     'Cookie': 'hello python',
    #     'Host': 'www.aduanet.gob.pe',
    #     'Pragma': 'no-cache',
    #     'Referer': 'http://www.aduanet.gob.pe/itarancel/JSPDetallePartidaArancel.jsp',
    #     'Upgrade-Insecure-Requests': '1',
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36',
    # }
    # print(headers)
    # headers['Cookie'] = cookie
    # print(headers)
    return cookie
def get_convenio_cookie():
    with open('convenio_cookie.txt') as f:
        cookie = f.read()
    # headers = {
    #     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    #     'Accept-Encoding': 'gzip, deflate',
    #     'Accept-Language': 'zh-CN,zh;q=0.9',
    #     'Cache-Control': 'no-cache',
    #     'Connection': 'keep-alive',
    #     'Cookie': 'hello python',
    #     'Host': 'www.aduanet.gob.pe',
    #     'Pragma': 'no-cache',
    #     'Referer': 'http://www.aduanet.gob.pe/itarancel/JSPDetallePartidaArancel.jsp',
    #     'Upgrade-Insecure-Requests': '1',
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36',
    # }
    # print(headers)
    # headers['Cookie'] = cookie
    # print(headers)
    return cookie
def get_detail_cookie():
    with open('detail_cookie.txt') as f:
        cookie = f.read()
    # headers = {
    #     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    #     'Accept-Encoding': 'gzip, deflate',
    #     'Accept-Language': 'zh-CN,zh;q=0.9',
    #     'Cache-Control': 'no-cache',
    #     'Connection': 'keep-alive',
    #     'Cookie': 'hello python',
    #     'Host': 'www.aduanet.gob.pe',
    #     'Pragma': 'no-cache',
    #     'Referer': 'http://www.aduanet.gob.pe/itarancel/JSPDetallePartidaArancel.jsp',
    #     'Upgrade-Insecure-Requests': '1',
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36',
    # }
    # print(headers)
    # headers['Cookie'] = cookie
    # print(headers)
    return cookie
def main():
    print(get_convenio_cookie())
    print(get_detail_cookie())
if __name__ == '__main__':
    main()