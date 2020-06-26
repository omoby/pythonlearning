import execjs
import requests

user = '18859276109'
pwd = 'zqx'

session = requests.Session()


def get_pwd():
    '''
    获取js加密后的密码
    :return: 加密后的密码
    '''
    with open('aiqiyi.js') as f:
        js_code = f.read()
    result = execjs.compile(js_code).call('new_pwd', pwd)
    return result


def login():
    '''
    登录
    :return:
    '''
    url = "https://passport.iqiyi.com/apis/reglogin/login.action"
    new_pwd = get_pwd()
    payload = f"email={user}&fromSDK=1&sdk_version=1.0.0&passwd={new_pwd}&agenttype=1&__NEW=1&checkExist=1&lang=&ptid=01010021010000000000&nr=2&verifyPhone=1&area_code=86&dfp=a0471f329cb4ae4f6eb4e70955f8dc98b9ecf0fc904eae0e1b91a15b846ed16a9a"
    headers = {
        # 'Pragma': "no-cache",
        # 'Origin': "https://www.iqiyi.com",
        # 'Accept-Encoding': "gzip, deflate, br",
        # 'Accept-Language': "zh-CN,zh;q=0.9",
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36",
        'Content-Type': "application/x-www-form-urlencoded; charset=UTF-8",
        # 'Accept': "application/json, text/javascript, */*; q=0.01",
        # 'Cache-Control': "no-cache",
        # 'Referer': "https://www.iqiyi.com/iframe/loginreg",
        # 'Cookie': 'QC005=5971ea4fc39016bc5099593c2a621926; QC173=0; Hm_lvt_53b7374a63c37483e5dd97d78d9bb36e=1592911303; Hm_lpvt_53b7374a63c37483e5dd97d78d9bb36e=1592911303; QC006=jwp6c02lsiy7cavoljiujel; QYABEX={"pcw_home_movie":{"value":"old","abtest":"146_A"}}; QC175=%7B%22upd%22%3Atrue%2C%22ct%22%3A%22%22%7D; QC008=1592911303.1592911303.1592911305.2; nu=0; P00004=.1592911308.b91c59f6f2; QC007=DIRECT; QC010=231502491; QC160=%7B%22u%22%3A%22%22%2C%22lang%22%3A%22%22%2C%22local%22%3A%7B%22name%22%3A%22%E4%B8%AD%E5%9B%BD%E5%A4%A7%E9%99%86%22%2C%22init%22%3A%22Z%22%2C%22rcode%22%3A48%2C%22acode%22%3A86%7D%7D; __dfp=a0471f329cb4ae4f6eb4e70955f8dc98b9ecf0fc904eae0e1b91a15b846ed16a9a@1594207304562@1592911305562',
        # 'Connection': "keep-alive"
    }
    response = session.request("POST", url, data=payload, headers=headers)

    json_data = response.json()
    redirect = json_data['data']['redirect']
    print(redirect)
    response = session.get(redirect, headers=headers)
    # print(response.text)

    url = "https://pcw-api.iqiyi.com/passport/user/userinfodetail"

    headers = {
        # 'pragma': "no-cache",
        # 'cookie': 'QC005=5971ea4fc39016bc5099593c2a621926; QC173=0; Hm_lvt_53b7374a63c37483e5dd97d78d9bb36e=1592911303; QC006=jwp6c02lsiy7cavoljiujel; QYABEX={"pcw_home_movie":{"value":"old","abtest":"146_A"}}; QC008=1592911303.1592911303.1592911305.2; nu=0; P00004=.1592911308.b91c59f6f2; QC007=DIRECT; QC160=%7B%22u%22%3A%2218859276109%22%2C%22lang%22%3A%22%22%2C%22local%22%3A%7B%22name%22%3A%22%E4%B8%AD%E5%9B%BD%E5%A4%A7%E9%99%86%22%2C%22init%22%3A%22Z%22%2C%22rcode%22%3A48%2C%22acode%22%3A%2286%22%7D%2C%22type%22%3A%22p1%22%7D; QC179=%7B%22userIcon%22%3A%22//www.iqiyipic.com/common/fix/headicons/male-130.png%22%2C%22vipTypes%22%3A-1%7D; QY_PUSHMSG_ID=5971ea4fc39016bc5099593c2a621926; QC178=true; Hm_lpvt_53b7374a63c37483e5dd97d78d9bb36e=1592912500; QC010=160053817; P00001=2bum34Rny2aUiu7jMcPcL8m37yi1wkGTkuVxQOdym3TSz4m2Zm2pu2qK0T7WepbqsbigzeP1c; P00003=685916515477516; P00010=685916515477516; P01010=1592928000; P00007=2bum34Rny2aUiu7jMcPcL8m37yi1wkGTkuVxQOdym3TSz4m2Zm2pu2qK0T7WepbqsbigzeP1c; P00PRU=685916515477516; P00002=%7B%22uid%22%3A%22685916515477516%22%2C%22pru%22%3A685916515477516%2C%22user_name%22%3A%2218859276109%22%2C%22nickname%22%3A%22%5Cu7528%5Cu623726fd66240280c%22%2C%22pnickname%22%3A%22%5Cu7528%5Cu623726fd66240280c%22%2C%22type%22%3A11%2C%22email%22%3A%22%22%7D; P000email=18859276109; QC175=%7B%22upd%22%3Atrue%2C%22ct%22%3A1592913169815%7D; QC170=0; __dfp=a0471f329cb4ae4f6eb4e70955f8dc98b9ecf0fc904eae0e1b91a15b846ed16a9a@1594207304562@1592911305562',
        'origin': "https://www.iqiyi.com",
        # 'accept-encoding': "gzip, deflate, br",
        # 'accept-language': "zh-CN,zh;q=0.9",
        'user-agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36",
        # 'accept': "application/json, text/plain, */*",
        # 'cache-control': "no-cache,no-cache",
        # 'authority': "pcw-api.iqiyi.com",
        'referer': "https://www.iqiyi.com/u/accountset",
    }

    response = session.request("GET", url, headers=headers)
    print(response.text)


def main():
    login()


if __name__ == '__main__':
    main()
