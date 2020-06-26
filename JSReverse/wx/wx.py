import execjs
import requests

user = '3165845957@qq.com'
pwd = 'zqx'


def get_pwd():
    '''
    获取js加密的新密码
    :return: 加密后的密码
    '''
    with open('wxgzh.js') as f:
        js_code = f.read()
    result = execjs.compile(js_code).call('get_pwd', pwd)
    return result


def login():
    '''
    登录
    :return:
    '''
    url = "https://mp.weixin.qq.com/cgi-bin/bizlogin"

    querystring = {"action": "startlogin"}

    payload = f"username={user}&pwd={get_pwd()}&imgcode=&f=json&userlang=zh_CN&redirect_url=&token=&lang=zh_CN&ajax=1"
    headers = {
        'origin': "https://mp.weixin.qq.com",
        'accept-encoding': "gzip, deflate, br",
        'accept-language': "zh-CN,zh;q=0.9",
        'x-requested-with': "XMLHttpRequest",
        'cookie': "ua_id=vQFVVGyGDXi7zjnlAAAAAEZ5L-soq87oLQWaIS6Zius=; pgv_pvi=3215070208; pgv_si=s8740655104; cert=QynNHNkczaaxtiSeRUXbWGWQhQBGI2oT; sig=h014d8dd051ee4e119f120c34083b4a319b9fa8b95bff5304c1f7bbfb070e19294f295e695c7996a67d; uuid=fbc993865901275b29aa0fa15e74d171; bizuin=3595703489; ticket=813e568f982b117843b86fcf1ba39349b270205d; ticket_id=gh_91b8ea3db7e0; noticeLoginFlag=1",
        'pragma': "no-cache",
        'user-agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36",
        'content-type': "application/x-www-form-urlencoded; charset=UTF-8",
        'accept': "*/*",
        'cache-control': "no-cache,no-cache",
        'authority': "mp.weixin.qq.com",
        'referer': "https://mp.weixin.qq.com/",
        'Postman-Token': "abd94aaa-7264-42e1-8097-258542f3fc25"
    }

    response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

    url = "https://mp.weixin.qq.com/cgi-bin/bizlogin"

    querystring = {"action": "validate", "lang": "zh_CN", "account": "3165845957%40qq.com", "token": ""}

    headers = {
        'authority': "mp.weixin.qq.com",
        'pragma': "no-cache",
        'cache-control': "no-cache,no-cache",
        'upgrade-insecure-requests': "1",
        'user-agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36",
        'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        'referer': "https://mp.weixin.qq.com/",
        'accept-encoding': "gzip, deflate, br",
        'accept-language': "zh-CN,zh;q=0.9",
        'cookie': "ua_id=vQFVVGyGDXi7zjnlAAAAAEZ5L-soq87oLQWaIS6Zius=; pgv_pvi=3215070208; pgv_si=s8740655104; cert=QynNHNkczaaxtiSeRUXbWGWQhQBGI2oT; noticeLoginFlag=1; sig=h012aa7654535f7ac7b7ffeb4763e2b8d4abe60b11f4c9c0ef352e036d1b38269f4d80ec27771167ab7; uuid=79365904a4319171696d21f9e08c758d; bizuin=3595703489; ticket=813e568f982b117843b86fcf1ba39349b270205d; ticket_id=gh_91b8ea3db7e0; ticket_uin=3595703489; login_certificate=WdyY5zfWEFO+B4N1GB3V/My/SK59uvEXp6Qib8Bhwrk=; ticket_certificate=OTqBvmLV0K4rGHZ3RE1oOSPwiLWkIvjLA4Pkv4myKyk=; fake_id=3595703489; login_sid_ticket=ebe6391d71da0e327da0ef9f03781ffc885d4988",
        'Postman-Token': "66c982c8-e72d-4a87-8556-eaadcd535eee"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)


def main():
    login()
    # get_pwd()


if __name__ == '__main__':
    main()
