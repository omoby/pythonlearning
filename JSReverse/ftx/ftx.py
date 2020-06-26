import requests
import execjs

user = "18859276109"
pwd = "aa"


def get_new_pwd():
    '''
    获取js加密后的密码
    :return: 加密后的密码
    '''
    with open("ftx.js", 'r') as  f:
        js_code = f.read()
    new_pwd = execjs.compile(js_code).call('test', pwd)
    return new_pwd


def login():
    """
    登录
    :return:
    """
    url = "https://passport.fang.com/login.api"

    headers = {
        'Pragma': "no-cache",
        'Origin': "https://passport.fang.com",
        'Accept-Encoding': "gzip, deflate, br",
        'Accept-Language': "zh-CN,zh;q=0.9",
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36",
        'Content-Type': "application/x-www-form-urlencoded; charset=UTF-8",
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'X-Requested-With': "XMLHttpRequest",
        'Cookie': "__jsluid_s=145cf66c267464cd94d10d877d931bf4; global_cookie=3t6zlyx4qxkrt0p141sx9a2gq12ka91ss0o; g_sourcepage=txz_dl%5Egg_pc; engine_source_cookie=baidu; sf_source=baidu; __utma=147393320.158765033.1589598326.1589598326.1589598326.1; __utmc=147393320; __utmz=147393320.1589598326.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; token=6e1d0296f921463a86b3256f3301f7c2; unique_cookie=U_3t6zlyx4qxkrt0p141sx9a2gq12ka91ss0o*4; __utmt_t0=1; __utmt_t1=1; __utmb=147393320.6.10.1589598326",
        'Connection': "keep-alive",
        'Referer': "https://passport.fang.com/",
        'cache-control': "no-cache",
        'Postman-Token': "13934233-ced9-4646-83bd-24907ae42907"
    }
    new_pwd = get_new_pwd()
    data = {
        'uid': user,
        'pwd': new_pwd,
        'Service': 'soufun-passport-web',
        'AutoLogin': '0',
    }

    response = requests.request("POST", url, data=data, headers=headers)
    print(response.text)


def main():
    login()


if __name__ == '__main__':
    main()
