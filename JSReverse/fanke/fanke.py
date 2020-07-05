import execjs
import requests

user = 'lq22845965'
pwd = 'aa'


def get_pwd():
    with open('fanke_2.js') as f:
        js_code = f.read()
    result = execjs.compile(js_code).call('get_pwd', pwd)
    f.close()
    return result


def login():
    url = "https://i.fkw.com/ajax/login_h.jsp"
    new_pwd = get_pwd()
    querystring = {"dogSrc": "3"}

    payload = f"cacct=lq22845965&sacct=boss&pwd={new_pwd}&autoLogin=false&staffLogin=false&bizType=5&dogId=0&fromsite=false&cmd=loginCorpNews&vc_type=2&checkSign=CS1AKWAvNEECgwxMTIuMjEuMjMuNzc&fallbacked=false"
    headers = {
        'Pragma': "no-cache",
        'Origin': "https://i.fkw.com",
        'Accept-Encoding': "gzip, deflate, br",
        'Accept-Language': "zh-CN,zh;q=0.9",
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36",
        'Content-Type': "application/x-www-form-urlencoded; charset=UTF-8",
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'X-Requested-With': "XMLHttpRequest",
        'Cookie': "_cliid=OncsDt2Lg-ciYD2I; loginComeForm=fkjz; _ta=207; _tp=-; _td=0 0 0 0; _newUnion=0; _kw=0; _audience=0; _haoci_rec_word=; _bidurl=; wxRegBiz=none; _fkwRegCount=3567; bdHomeFlag=0; faiscoRegUserJz=1; Hm_lvt_337c9c93ccaf12bf23e76a24b41f3ab8=1593961833; _pykey_=68dfad3b-101e-5320-9a3f-b5ce97e93589; www.fkw.com__MESIGN=AJzbh-gFCgQzMTY2EOaFpYgG; loginCacct=lq22845965; loginSacct=boss; loginUseSacct=0; regSucceedAcct=undefined; Hm_lvt_d6259e0f0ed435520c61be2682182ac2=1593961900; Hm_lpvt_d6259e0f0ed435520c61be2682182ac2=1593961900; _fkRegSuc_24632055=1; Hm_lpvt_337c9c93ccaf12bf23e76a24b41f3ab8=1593961909; loginReferer=https://www.fkw.com/reg.html?_fromsite=false; _portalLastEnterDay=2020-07-05; _initCoupon=0; _readCoupon=0; _readAllOrderTab=0; _tab=manage; cookie_count=1; _isFirstLoginPc=false; _isFirstLoginPc_7=false; bottom_adv_count=1; _portal_product_click_type_undefined=none; _portal_product_click_date_undefined=1593961914146; GUIDE_OPEN_show_24632055=true; GUIDE_OPEN_click_24632055=true; _FSESSIONID=; loginSign=",
        'Connection': "keep-alive",
        'Referer': "https://i.fkw.com/",
        'cache-control': "no-cache",
        'Postman-Token': "2922b766-b427-47ba-83fb-b53c54f399ef"
    }

    response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

    print(response.text)


def main():
    # login()
    print(get_pwd())


if __name__ == '__main__':
    main()
