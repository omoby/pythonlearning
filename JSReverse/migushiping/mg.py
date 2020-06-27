
import requests
import execjs
import json
import re
import time

user = '18859276109'
passwd = 'aa'

session = requests.Session()


def get_timestamp():
    return int(round(time.time() * 1000))


def get_crypt_user_or_pwd(paramter):
    with open('mg.js', 'r', encoding='utf8') as f:
        js_code = f.read()
    result = execjs.compile(js_code).call('get_user_or_pwd', paramter)
    return result


def get_fingerprint_details():
    with open('mg.js', 'r',encoding='utf8') as f:
        js_code = f.read()
    results = execjs.compile(js_code).call('get_result_detail')
    return results


def login():
    url = 'https://passport.migu.cn/authn'
    headers = {
        # 'Host': 'passport.migu.cn',
        # 'Origin': 'https://passport.migu.cn',
        # 'Referer': 'https://passport.migu.cn/login?sourceid=203021&apptype=2&forceAuthn=true&isPassive=false&authType=&display=&nodeId=70027513&relayState=login&weibo=1&callbackURL=http%3A%2F%2Fwww.miguvideo.com%2Fmgs%2Fwebsite%2Fprd%2Findex.html%3FisIframe%3Dweb%26isIframe%3Dweb',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.59 Safari/537.36 115Browser/8.0.0',
        # 'X-Requested-With': 'XMLHttpRequest',
        # 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    }
    crypt_user = get_crypt_user_or_pwd(user)
    crypt_pwd = get_crypt_user_or_pwd(passwd)
    details = get_fingerprint_details()
    finger_print = details.get('result')
    finger_print_detail = details.get('details')

    data = {
        'sourceID': 100001,
        'appType': 2,
        'relayState': 'login',
        'loginID': crypt_user,
        'enpassword': crypt_pwd,
        'captcha': '',
        'imgcodeType': 1,
        'fingerPrint': finger_print,
        'fingerPrintDetail': finger_print_detail,
        'isAsync': 'true',
    }

    response = session.post(url, data=data, headers=headers)
    data_text = response.text
    print(data_text)
    data_json = json.loads(data_text)
    result = data_json.get('result')
    redirect_url = result.get('redirectURL')
    token = result.get('token')

    querystring = {
        "callbackURL": "",
        "relayState": "",
        "token": token
    }

    headers = {

        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36",
        # 'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        # 'Referer': "https://passport.migu.cn/login?sourceid=100001&apptype=0&forceAuthn=false&isPassive=false&authType=MiguPassport&passwordControl=0&display=web&referer=https://passport.migu.cn/portal&logintype=1&qq=null&weibo=null&alipay=null&weixin=null&andPass=null&phoneNumber=&callbackURL=&relayState=",
        # 'Cookie': "mgpt_session_id=ADARWQIRI2-KI2H0B5R0ZGN4BKNLS853-38WREXBK-0; mgpt_session_create=1593248087523; mgnd_session_id=ADARBWHIK2-KI2HIK5S0O9GEATLOROL2-7DWREXBK-0; mgnd_session_create=1593248087707; mgpt_session_last_access=1593248098485; mgnd_session_last_access=1593248734546; LTToken=TGnid0000001593248734564xM0c3ORH6EZ57sIHDBWcawf5yOR1Mubj; USessionID=UDnid0000011593248734561Ob0Awr4IZOxGfUcHERfuvTl6A9jtwX09; idmpauth=true@passport.migu.cn",
    }

    response = session.request("GET", redirect_url, headers=headers, params=querystring)
    print(response.text)

    url = re.compile("<script>window.top.location.href = '(.*?)';</script>").findall(response.text)[0]

    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36",
        # 'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        # 'Referer': "https://passport.migu.cn/portal/sso/authn_success?relateToMiguPassport=1&callbackURL=&relayState=",

        # 'Cookie': "mgpt_session_id=ADARWQIRI2-KI2H0B5R0ZGN4BKNLS853-38WREXBK-0; mgpt_session_create=1593248087523; mgnd_session_id=ADARBWHIK2-KI2HIK5S0O9GEATLOROL2-7DWREXBK-0; mgnd_session_create=1593248087707; mgnd_session_last_access=1593248734546; LTToken=TGnid0000001593248734564xM0c3ORH6EZ57sIHDBWcawf5yOR1Mubj; USessionID=UDnid0000011593248734561Ob0Awr4IZOxGfUcHERfuvTl6A9jtwX09; idmpauth=true@passport.migu.cn; mgpt_session_last_access=1593248734689",

    }

    response = session.request("GET", url, headers=headers)
    print(response.text)


def main():
    # print get_timestamp()
    # get_fingerprint_details()
    # get_crypt_user_or_pwd(passwd)
    login()


if __name__ == '__main__':
    main()
