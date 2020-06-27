# coding=utf8
import re
import time

import requests
import execjs

user = '18859276109'
password = "aa"


def get_crypt_user_pwd():
    with open('mg2.js', 'r', encoding='utf8') as f:
        js_code = f.read()
    crypt_user = execjs.compile(js_code).call('get_loginid_enpassword', user)
    crypt_pwd = execjs.compile(js_code).call('get_loginid_enpassword', password)
    return (crypt_user, crypt_pwd)


def get_fingerprint_details():
    with open('mg2.js', 'r', encoding='utf8') as f:
        js_code = f.read()
    result = execjs.compile(js_code).call('rsaFingerprint')
    return result


def pre_login_authn():
    url = 'https://passport.migu.cn/authn'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Host': 'passport.migu.cn',
        'Origin': 'https://passport.migu.cn',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.59 Safari/537.36 115Browser/8.0.0',
        'X-Requested-With': 'XMLHttpRequest',
    }
    crypt_user, crypt_pwd = get_crypt_user_pwd()
    results = get_fingerprint_details()
    finger_print = results.get('result')
    finger_print_detail = results.get('details')

    data = {
        'sourceID': '203021',
        'appType': '2',
        'relayState': 'login',
        'loginID': crypt_user,
        'enpassword': crypt_pwd,
        'captcha': '',
        'imgcodeType': '1',
        'fingerPrint': finger_print,
        'fingerPrintDetail': finger_print_detail,
        'isAsync': 'true',
    }
    session = requests.Session()
    response = session.post(url, data=data, headers=headers)
    return response.text


def pre_login_callback():
    pre_login_authn_response = pre_login_authn()
    import json
    json_data = json.loads(pre_login_authn_response)
    redirect_url = json_data['result']['redirectURL']
    token = json_data['result']['token']
    other_paramter_string = '?callbackURL=http%3A%2F%2Fwww.miguvideo.com%2Fmgs%2Fwebsite%2Fprd%2Findex.html%3FisIframe%3Dweb&relayState=login&token='
    url = redirect_url + other_paramter_string + token
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.59 Safari/537.36 115Browser/8.0.0',
    }
    response = requests.get(url, headers=headers)

    data_text = response.text
    # print data_text
    pat_sign = r'sign=(.*?)&'
    pat_sign_type = r'signType=(.*?)&'
    pat_client_id = r'clientId: \\"(.*?)\\",'
    pat_device_id = r'deviceId: \\"(.*?)\\",'
    sign = re.compile(pat_sign).findall(data_text)[0]
    sign_type = re.compile(pat_sign_type).findall(data_text)[0]
    client_id = re.compile(pat_client_id).findall(data_text)[0]
    device_id = re.compile(pat_device_id).findall(data_text)[0]
    # print client_id
    return (sign, sign_type, client_id, device_id, token)


def login_migutokenforall():
    url = 'https://m.miguvideo.com/userCenterLogin/login/migutokenforall'
    sign, sign_type, client_id, device_id, token = pre_login_callback()
    url = url + "?sign=" + sign + "&signType=" + sign_type + "&clientId=" + client_id
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.59 Safari/537.36 115Browser/8.0.0',
    }
    data = {
        'deviceId': device_id,
        'miguToken': token,
        'timestamp': int(round(time.time() * 1000))
    }
    import json
    response = requests.post(url, data=json.dumps(data), headers=headers)
    print(response.text)


def main():
    # get_crypt_user_pwd()
    # get_fingerprint_details()
    # pre_login_authn()
    # pre_login_callback()
    login_migutokenforall()


if __name__ == '__main__':
    main()
