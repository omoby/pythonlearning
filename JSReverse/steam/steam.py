import execjs
import requests
from urllib.parse import quote

from JSReverse.util.date_util import get_timestamp

user = '3165845957'
pwd = 'Zqx666666'

session = requests.Session()


def get_rsa_key(time_stamp):
    '''
    获取rsa的publickey
    :param time_stamp: 请求时间戳
    :return:rsa的publickey
    '''

    # print(time_stamp)
    url = "https://store.steampowered.com/login/getrsakey/"
    payload = f"donotcache={time_stamp}&username={user}"
    headers = {
        # 'Origin': "https://store.steampowered.com",
        # 'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36",
        'Content-Type': "application/x-www-form-urlencoded; charset=UTF-8",
        # 'X-Requested-With': "XMLHttpRequest",
        # 'Cookie': "browserid=1969711212066891896; steamCountry=CN%7C9a4974ba1e7266188fbd3ec09b447001; sessionid=01c1b84cbf58d8b55034b201; timezoneOffset=28800,0; _ga=GA1.2.1053234623.1593176908; _gid=GA1.2.1967924376.1593176908",
        # 'Referer': "https://store.steampowered.com/login/?redir=&redir_ssl=1",

    }

    response = session.request("POST", url, data=payload, headers=headers)

    return response.json()
    # print(response)


def get_pwd(results):
    '''
    获取加密后的密码
    :param results: 获取的publickey对象
    :return:加密后的密码
    '''
    with open('steam.js') as f:
        js_code = f.read()
    new_pwd = execjs.compile(js_code).call('get_pwd', pwd, results)
    return new_pwd


def login():
    '''
    登录
    :return:
    '''
    time_stamp = get_timestamp()
    results = get_rsa_key(time_stamp)
    new_pwd = get_pwd(results)
    url = "https://store.steampowered.com/login/dologin/"

    payload = f"donotcache={time_stamp}&password={quote(new_pwd)}&username={user}&twofactorcode=&emailauth=&loginfriendlyname=&captchagid=-1&captcha_text=&emailsteamid=&rsatimestamp={results.get('timestamp')}&remember_login=false"
    # print(payload)
    headers = {
        # 'Pragma': "no-cache",
        # 'Origin': "https://store.steampowered.com",
        # 'Accept-Encoding': "gzip, deflate, br",
        # 'Accept-Language': "zh-CN,zh;q=0.9",
        # 'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36",
        'Content-Type': "application/x-www-form-urlencoded; charset=UTF-8",
        # 'Accept': "*/*",
        # 'Cache-Control': "no-cache",
        # 'X-Requested-With': "XMLHttpRequest",
        # 'Cookie': "browserid=1969711212066891896; steamCountry=CN%7C9a4974ba1e7266188fbd3ec09b447001; sessionid=01c1b84cbf58d8b55034b201; timezoneOffset=28800,0; _ga=GA1.2.1053234623.1593176908; _gid=GA1.2.1967924376.1593176908",
        # 'Connection': "keep-alive",
        # 'Referer': "https://store.steampowered.com/login/?redir=&redir_ssl=1",
        # 'cache-control': "no-cache",
        # 'Postman-Token': "566fb3aa-2f84-4665-93da-3b1b6fda084a"
    }

    response = session.request("POST", url, data=payload, headers=headers)

    print(response.text)


def main():
    # time_stamp = get_timestamp()
    # get_rsa_key(time_stamp)
    # get_pwd()
    login()


if __name__ == '__main__':
    main()
