import requests
import execjs
import os

os.environ["EXECJS_RUNTIME"] = "phantomjs"

user = "18859276109"
pwd = "aa"

session = requests.Session()


def get_crypt_pwd():
    with open("./qdzg.js", 'r', encoding='UTF-8') as fp:
        ajs = fp.read()
    loader = execjs.compile(ajs)
    r = loader.call('get_pwd_no_cap', user, pwd)
    return r


def get_crypt_pwd_with_capt(captch):
    with open("qdzg.js", 'r', encoding='UTF-8') as fp:
        ajs = fp.read()
    loader = execjs.compile(ajs)
    r = loader.call('get_pwd', user, pwd, captch)
    return r


def get_login():
    url = 'https://www.yypt.com/finance/j_spring_security_check'
    crypt_pwd = get_crypt_pwd()
    header = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Host': 'www.yypt.com',
        'Origin': 'https://www.yypt.com',
        'Referer': 'https://www.yypt.com/finance/login.do?error=true',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36',
    }
    data = {
        'ncid': '',
        'loginType': '-1',
        'custType': '',
        'j_username': user,
        'j_password': crypt_pwd,
        'encodeType': 'pc',
        'loginSim': ''
    }
    print(data)
    respose = session.post(url, data=data, headers=header)
    print(respose.status_code)
    print(respose.url)
    print(respose.text)


def main():
    get_login()


if __name__ == '__main__':
    main()
