import re

import requests
import execjs

user = '18859276109'
password = 'aa'


def get_new_user_pwd():
    with open('jk160.js', 'r', encoding='utf8') as f:
        js_code = f.read()
    new_user = execjs.compile(js_code).call('get_user_pwd', user)
    new_pwd = execjs.compile(js_code).call('get_user_pwd', password)
    return (new_user, new_pwd)


session = requests.Session()


def get_tokens():
    url = 'https://user.91160.com/login.html'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.59 Safari/537.36 115Browser/8.0.0'
    }
    response = session.get(url, headers=headers)
    pat = r'id="tokens" value="(.*?)"'
    import re
    result = re.compile(pat).findall(response.text)[0]
    return result


def login():
    token = get_tokens()
    crypt_user, crypt_pwd = get_new_user_pwd()
    url = 'https://user.91160.com/checkUser.html'
    headers = {
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://user.91160.com',
        'referer': 'https://user.91160.com/login.html',
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.59 Safari/537.36 115Browser/8.0.0',
        'x-requested-with': 'XMLHttpRequest',
    }
    data = {
        'type': 'm',
        'username': crypt_user,
        'password': crypt_pwd,
        'checkcode': '',
        'token': token,
    }
    response = session.post(url, data=data, headers=headers)
    # print(response.content)
    url = 'https://user.91160.com/login.html'
    crypt_user, crypt_pwd = get_new_user_pwd()
    data = {
        'clientLoginUrl': '',
        'username': crypt_user,
        'password': crypt_pwd,
        'target': 'https://www.baidu.com/link?url=H1ZG_fCbed_LtIhz2OXnchJt4UhBIUjrwnC8L4dXqsrr0IAV6gzsTIXKcx7P6Fa3&wd=&eqid=a98f07a900000fdd000000045eb25b09',
        'error_num': 0,
        'checkcode': '',
        'tokens': token,
    }
    headers = {
        'content-type': 'application/x-www-form-urlencoded',
        'referer': 'https://user.91160.com/login.html',
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.59 Safari/537.36 115Browser/8.0.0',
        'x-requested-with': 'XMLHttpRequest',
    }
    response = session.post(url, data=data, headers=headers)
    url = response.url
    # print(response.text)
    response = session.get(url, headers=headers)
    response.encoding = 'utf-8'

    print(response.text)


def main():
    # get_new_user_pwd()
    # get_tokens()
    login()


if __name__ == '__main__':
    main()
