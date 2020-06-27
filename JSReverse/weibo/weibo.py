import json
import re
from urllib.parse import quote

import execjs
import requests

from JSReverse.util.date_util import get_timestamp

user = '18859276109'
password = 'aa'

session = requests.Session()


def get_user():
    '''
    获取加密后的账号
    :return: 加密后的账号
    '''
    with open('weibo.js') as f:
        js_code = f.read()
    su = execjs.compile(js_code).call('get_user', user)
    f.close()
    return quote(su)


def get_pwd(me):
    '''
    获取加密后的密码
    :param me: sra pubkey
    :return: 加密后的密码
    '''
    with open('weibo.js') as f:
        js_code = f.read()
    sp = execjs.compile(js_code).call('get_pwd', user, me)
    return sp


def get_prelogin():
    '''
    获取sra pubkey
    :return: sra pubkey
    '''
    time_stamp = get_timestamp()
    su = get_user()
    url = "https://login.sina.com.cn/sso/prelogin.php"
    querystring = {
        "entry": "weibo",
        "callback": "sinaSSOController.preloginCallBack",
        "su": su,
        "rsakt": "mod",
        "checkpin": "1",
        "client": "ssologin.js%28v1.4.19%29",
        "_": time_stamp
    }
    headers = {
        'Referer': "https://weibo.com/",
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36",
        'cache-control': "no-cache",
        'Postman-Token': "9e1b8929-6e1a-4506-9a20-bc74417667e6"
    }

    response = session.request("GET", url, headers=headers, params=querystring)
    text_data = re.compile(f'sinaSSOController.preloginCallBack\((.*?)\)').findall(response.text)[0]
    json_data = json.loads(text_data)
    return json_data


def get_captcha(p):
    '''
    下载验证码
    :param p:
    :return:
    '''
    url = "https://login.sina.com.cn/cgi/pin.php"

    querystring = {
        "r": "67607331",
        "s": "0",
        "p": p
    }

    headers = {
        'Connection': "keep-alive",
        'Pragma': "no-cache",
        'Cache-Control': "no-cache",
        'Upgrade-Insecure-Requests': "1",
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36",
        'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        'Accept-Encoding': "gzip, deflate, br",
        'Accept-Language': "zh-CN,zh;q=0.9",
        'Cookie': "SINAGLOBAL=112.21.22.173_1593223532.636329; Apache=112.21.22.173_1593223532.636330; SCF=AnQZmbOBU2jQFXomGVrN0tWXzCYKFW2bd66a-96dJZTEe9j-ycSTD6JFciHSZa1bA6M8WP2_-ncbeBXzEJMztJA.; SUB=_2AkMpqjEXdcPxrAZZmfwVz23gbopH-jyaf1jhAn7tJhMyAhh87ko2qSVutBF-XHn9R7TWaoGayfQQAZlYuH_iR5sK; SUBP=0033WrSXqPxfM72wWs9jqgMF55529P9D9W5YLGcVrNpPgLfgAZZMhlpe5JpVF02R1h-4eoMceK54; ULOGIN_IMG=yf-226fbcc75acdd7b191422da55f89fe5dfb61",
        'cache-control': "no-cache",
        'Postman-Token': "23c8a9cd-d3b8-451b-a780-e491711ac8c1"
    }

    response = session.request("GET", url, headers=headers, params=querystring)

    with open('./captcha.jpg', 'wb') as fp:
        fp.write(response.content)
        fp.close()


def login():
    '''
    登录
    :return:
    '''
    me = get_prelogin()
    su = get_user()
    pwd = get_pwd(me)
    get_captcha(me.get('pcid'))
    door = input('请输入验证码：')
    print(door)

    url = "https://login.sina.com.cn/sso/login.php"

    querystring = {"client": "ssologin.js%28v1.4.19%29", "wsseretry": "servertime_error"}

    payload = f"entry=weibo&gateway=1&from=&savestate=0&qrcode_flag=false&useticket=1&pagerefer=&wsseretry=servertime_error&pcid={me.get('pcid')}&door={door}&vsnf=1&su={su}&service=miniblog&servertime={me.get('servertime')}&nonce={me.get('nonce')}&pwencode=rsa2&rsakv={me.get('rsakv')}&sp={pwd}&sr=1536*864&encoding=UTF-8&prelt=60&url=https%253A%252F%252Fweibo.com%252Fajaxlogin.php%253Fframelogin%253D1%2526callback%253Dparent.sinaSSOController.feedBackUrlCallBack&returntype=META"
    headers = {
        'Connection': "keep-alive",
        'Pragma': "no-cache",
        'Cache-Control': "no-cache",
        'Origin': "https://weibo.com",
        'Upgrade-Insecure-Requests': "1",
        'Content-Type': "application/x-www-form-urlencoded",
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36",
        'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        'Referer': "https://weibo.com/",
        'Accept-Encoding': "gzip, deflate, br",
        'Accept-Language': "zh-CN,zh;q=0.9",
        'Cookie': "SINAGLOBAL=112.21.22.173_1593223532.636329; Apache=112.21.22.173_1593223532.636330; SUB=_2AkMpqjgwdcPxrAZZmfwVz23gbopH-jyaf1HGAn7tJhMyAhj_7mcDqSVutBF-XI9KeGoSJOKigJ_OlFxoKMtpzHle; SUBP=0033WrSXqPxfM72wWs9jqgMF55529P9D9W5YLGcVrNpPgLfgAZZMhlpe5JpVF02R1h-4eoMceK54; ULOGIN_IMG=yf-a9ae99c19d285a0303e9635af0689acea00c",
        'cache-control': "no-cache",
        'Postman-Token': "9827df95-16ae-409c-9882-3af8fbff0ce6"
    }

    response = session.request("POST", url, data=payload, headers=headers, params=querystring)
    # response.encoding = 'GBK'
    # print(response.text)

    # 访问用户首页
    url = "https://weibo.com/u/5814036227/home"

    querystring = {"wvr": "5", "uut": "fin", "from": "reg"}

    headers = {
        'Connection': "keep-alive",
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36",
        'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        'Referer': "https://weibo.com/",
        # 'Cookie': "_s_tentry=passport.weibo.com; Apache=733649897040.185.1593223530548; SINAGLOBAL=733649897040.185.1593223530548; ULV=1593223530667:1:1:1:733649897040.185.1593223530548:; Ugrow-G0=589da022062e21d675f389ce54f2eae7; YF-V5-G0=9717632f62066ddd544bf04f733ad50a; WBtopGlobal_register_version=fd6b3a12bb72ffed; login_sid_t=7f7885624efcdece1a89b32e05374eb2; cross_origin_proto=SSL; wb_view_log=1536*8641.25; un=18859276109; wb_view_log_5814036227=1536*8641.25; UOR=,,login.sina.com.cn; YF-Page-G0=530872e91ac9c5aa6d206eddf1bb6a70|1593228728|1593228559; webim_unReadCount=%7B%22time%22%3A1593228816283%2C%22dm_pub_total%22%3A40%2C%22chat_group_client%22%3A0%2C%22chat_group_notice%22%3A0%2C%22allcountNum%22%3A87%2C%22msgbox%22%3A0%7D; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5YLGcVrNpPgLfgAZZMhlpe5JpX5K2hUgL.Fo-ReKB7e0qEeoM2dJLoI7HDdGLfd7tt; ALF=1624766206; SSOLoginState=1593230206; SCF=AnQZmbOBU2jQFXomGVrN0tWXzCYKFW2bd66a-96dJZTEmintA1QTUTAU56uvDGTVFUjhj6DASaabhCeew8yI6ck.; SUB=_2A25z8rMuDeRhGeNG6lYR8yjOyTuIHXVQiaPmrDV8PUNbmtAKLWamkW9NS2nCRFqaZz_D4K2SOzX5YihiJp_Ni6Fa; SUHB=0Jvgw_5JMZdiTa",
        'Cookie': "SINAGLOBAL=112.21.22.173_1593223532.636329; Apache=112.21.22.173_1593223532.636330; SUB=_2AkMpqjgwdcPxrAZZmfwVz23gbopH-jyaf1HGAn7tJhMyAhj_7mcDqSVutBF-XI9KeGoSJOKigJ_OlFxoKMtpzHle; SUBP=0033WrSXqPxfM72wWs9jqgMF55529P9D9W5YLGcVrNpPgLfgAZZMhlpe5JpVF02R1h-4eoMceK54; ULOGIN_IMG=yf-a9ae99c19d285a0303e9635af0689acea00c",

    }

    response = session.request("GET", url, headers=headers, params=querystring)
    response.encoding = 'utf-8'
    print(response.text)


def main():
    # me = get_prelogin()
    # get_user()
    # print(me)
    login()


if __name__ == '__main__':
    main()
