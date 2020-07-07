def get_shops():
    import requests

    url = "https://i.waimai.meituan.com/openh5/channel/kingkongshoplist"

    querystring = {"_": "1594025777613",
                   "X-FOR-WITH": "ltJI0w99KbJyjiPTLfeuz0H9rP7EWm92%2F%2FCsN1qHUsregs03hW%2Bp%2FbQwy4JZeV%2FiljJ4XvmoQRRBy5Glc7TLPNQi%2BacH19EESUzW6s%2BJxzfB1ezodInS4sHNt72mWQR22oQTPFxO01iSA1kTb51LKHYkyBqIaRkk%2FgMb8FqRfvyloszEGoLFZH9sVyeCOPcfbMN44Bfoch1yVlCuzpxxMw%3D%3D"}

    payload = "startIndex=0&sortId=&navigateType=910&firstCategoryId=910&secondCategoryId=910&multiFilterIds=&sliderSelectCode=&sliderSelectMin=&sliderSelectMax=&actualLat=31.4891&actualLng=120.306289&initialLat=31.4891&initialLng=120.306289&geoType=2&rankTraceId=&uuid=6380715355AE14B00A89CB58B703AE8B7B225A362A48E83E064FC01825F81709&platform=3&partner=4&originUrl=https%253A%252F%252Fh5.waimai.meituan.com%252Fwaimai%252Fmindex%252Fkingkong%253FnavigateType%253D910%2526firstCategoryId%253D910%2526secondCategoryId%253D910%2526title%253D%2525E7%2525BE%25258E%2525E9%2525A3%25259F&riskLevel=71&optimusCode=10&wm_latitude=31489100&wm_longitude=120306289&wm_actual_latitude=31489100&wm_actual_longitude=120306289&openh5_uuid=6380715355AE14B00A89CB58B703AE8B7B225A362A48E83E064FC01825F81709&_token=eJzFkluvskYUhv8LF95AhBnOOzGNiIKKG9zgh9g2DYfhJIwHBlGb%252FveO7W739903aTIXaz3vuyZrzZrfmesyY96AAFQBcMwNXZk3BoyFscJwDOmoIuuSAGUZQFWGHJN%252Bx1RVlXWNY5LrN5N5%252B1miugL0X1%252Fgg%252BZf4CuCEj0vx5IamJKQc%252FfG86U8HuKqjatxiyrSx3icnlr%252Bb8S3Fc7QnW8R7n%252FKzn55Oi%252Bzyagln5GmAx1KQIOyDjUBjnrS%252Ftad%252BmuKJqO0jDFGzSRDedw3ZPTJO1rZVB0ZVbgiVdw4MZmIYCzRq%252F5FuJgAKIxFQYGaPopT2tUPvk%252Fyg42%252B2H8xEQCiLGq6Lsr%252F6zB0S23w2pKocjqgswGNg%252BCFj3%252FhX3pBAJAzXDOi4vcZtcRfldxyY%252F1TzS1fInmJL9OG%252FjUqdVWBaYRWD3I8sg58Trf3hHcKHAqrtHflaHnK8LToTADQoM4wDq3Hav1x528Yghwla%252FsgkyqQlmJ7V582ek71axqxFln552V4MXKyE9fl4tl4q0xtLzBwrTKPrcgLSj6oTyGewgLrChZsbBqCLzYO6zsoipNwbqjbuRQUXVvjZ9G6x5x6z2fewOkt6Pt1kQHn7p%252F9h7Mi7mIm4jq%252BikmM46rr20pgExnu6kxsgstcXdU9ux5kyWkOqU07Qx%252F3uiQzWfUkE8Hpws4cdgZCVKG8DQ8ofeTBTrJ2Ax7cOj4nMO8u%252FS5AhYU2Xa9sYidjPTGHit5ox9ltn5sL2do6bnW8yGvoA3%252Bf2Xv%252Fsd6y3ftxnpaGMISHq%252FLe2v6uC2un04zs3RStyGi0rr4tzW9NUnj7x%252BDObWVWHiQWv0snT3smi2GRLexHUSfy1nNnEsz8lD%252Fwm72SB2Q3w9TdWgXrR203l0Xeiy7mPvKf9uGZV7qrrnGiebdhXmiZaDB%252F%252FAmOXGPj&undefined="
    headers = {
        'Pragma': "no-cache",
        'Origin': "https://h5.waimai.meituan.com",
        'Accept-Encoding': "gzip, deflate, br",
        'Accept-Language': "zh-CN,zh;q=0.9",
        'User-Agent': "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Mobile Safari/537.36",
        'Content-Type': "application/x-www-form-urlencoded",
        'Accept': "application/json",
        'Cache-Control': "no-cache",
        'Referer': "https://h5.waimai.meituan.com/waimai/mindex/kingkong?navigateType=910&firstCategoryId=910&secondCategoryId=910&title=%E7%BE%8E%E9%A3%9F",
        'Cookie': "_lxsdk_cuid=17258e9bdcdc8-035b6212353d98-3f674604-144000-17258e9bdcec8; _ga=GA1.3.147549955.1594021774; _gid=GA1.3.423744456.1594021774; PHPSESSID=2huep8pinvja6qbllf74f3i9v2; Hm_lvt_f66b37722f586a240d4621318a5a6ebe=1594021789; Hm_lpvt_f66b37722f586a240d4621318a5a6ebe=1594021789; __utma=211559370.1176947614.1594021789.1594021789.1594021789.1; __utmc=211559370; __utmz=211559370.1594021789.1.1.utmcsr=baidu|utmccn=baidu|utmcmd=organic|utmcct=zt_search; __mta=256621876.1594021776291.1594021855987.1594021868864.3; wm_order_channel=default; utm_source=; au_trace_key_net=default; terminal=i; w_utmz=utm_campaign = (direct) & utm_source = 5000 & utm_medium = (none) & utm_content = (none) & utm_term = (none); service-off=0; iuuid=6380715355AE14B00A89CB58B703AE8B7B225A362A48E83E064FC01825F81709; _lxsdk=6380715355AE14B00A89CB58B703AE8B7B225A362A48E83E064FC01825F81709; openh5_uuid=6380715355AE14B00A89CB58B703AE8B7B225A362A48E83E064FC01825F81709; uuid=6380715355AE14B00A89CB58B703AE8B7B225A362A48E83E064FC01825F81709; openh5_uuid=6380715355AE14B00A89CB58B703AE8B7B225A362A48E83E064FC01825F81709; userId=2724915169; channelType={%22default%22:%220%22}; w_visitid=51e61e94-c03d-421e-815e-85145d63265d; token=GSRXwDLy_CCZdBpKhsXiWXURTWQAAAAAAQsAAFKn6Qr1uxoVpu__QcUz2sS_sTfpFzpZd98Pnsu5iKvXePglL-mZpNSxZb2eGm6gTQ; mt_c_token=GSRXwDLy_CCZdBpKhsXiWXURTWQAAAAAAQsAAFKn6Qr1uxoVpu__QcUz2sS_sTfpFzpZd98Pnsu5iKvXePglL-mZpNSxZb2eGm6gTQ; oops=GSRXwDLy_CCZdBpKhsXiWXURTWQAAAAAAQsAAFKn6Qr1uxoVpu__QcUz2sS_sTfpFzpZd98Pnsu5iKvXePglL-mZpNSxZb2eGm6gTQ; w_token=GSRXwDLy_CCZdBpKhsXiWXURTWQAAAAAAQsAAFKn6Qr1uxoVpu__QcUz2sS_sTfpFzpZd98Pnsu5iKvXePglL-mZpNSxZb2eGm6gTQ; w_actual_lat=31489100; w_actual_lng=120306289; w_latlng=31489100,120306289; cssVersion=ed62e738; _lx_utm=utm_source%3D; _lxsdk_s=173231a0445-802-fc0-941%7C%7C180",
        'Connection': "keep-alive",
        'cache-control': "no-cache",
        'Postman-Token': "76b6858c-7a4f-4392-bfa1-67ee421fadae"
    }

    response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

    print(response.text)

def get_shops_2():
    import requests

    url = "https://i.waimai.meituan.com/openh5/channel/kingkongshoplist"

    querystring = {"_": "1594026059031",
                   "X-FOR-WITH": "ltJI0w99KbJyjiPTLfeuz0H9rP7EWm92%2F%2FCsN1qHUspbYuwLBOmCqmh8eJ7SR3lAKfoyG3d0rrELIECVGnDirJVG2shd9KeHfYH%2BPC1pkTf2y1%2Fu1fRsmL8Od5aPgTN9rDrUuhM349fq8bkA8yjAsds5pEV4qkb0Rdr%2B4Z57QUUTFSoV72hdNAbKbkoyl3yceSlWjOAwXC%2BTFUyjkTB%2BHg%3D%3D"}

    payload = "startIndex=2&sortId=&navigateType=910&firstCategoryId=910&secondCategoryId=910&multiFilterIds=&sliderSelectCode=&sliderSelectMin=&sliderSelectMax=&actualLat=31.4891&actualLng=120.306289&initialLat=31.4891&initialLng=120.306289&geoType=2&rankTraceId=&uuid=6380715355AE14B00A89CB58B703AE8B7B225A362A48E83E064FC01825F81709&platform=3&partner=4&originUrl=https%253A%252F%252Fh5.waimai.meituan.com%252Fwaimai%252Fmindex%252Fkingkong%253FnavigateType%253D910%2526firstCategoryId%253D910%2526secondCategoryId%253D910%2526title%253D%2525E7%2525BE%25258E%2525E9%2525A3%25259F&riskLevel=71&optimusCode=10&wm_latitude=31489100&wm_longitude=120306289&wm_actual_latitude=31489100&wm_actual_longitude=120306289&openh5_uuid=6380715355AE14B00A89CB58B703AE8B7B225A362A48E83E064FC01825F81709&_token=eJzFkluPokgUx78LD75IpC7cqhOzEVFEsFHBoe3dzQahuAklcvG22e%252B%252BONMznXmbh002qYdzfv%252F%252FOTmnqv7majPiXiCACoA8d6E198LBERjJHM%252B1Ta9IRARIkiBSJMRz4SeTgUQAUnnuUH%252FRuZffxV6XIfnzCbZ9%252Fgk%252BIyT25%252BkwewOXtm3VvAhCKo2uQVYG2aikWdsFbBSeSuEbEsqMRfQmlJR1v0WVm54qMxoPyvYjUgkkSIQqkghSARp0bflXc%252BrqkI4HYRowRotxROOgK9rBB2%252F6yiJr2kHGsjYLCjtoxxiOxL7VD8SSMURghIGMVDIIwn6qn3wf5Cdbf2P%252FxUYQYgmrhGDpf12mf6XSe74SVngC%252B92gyiP4xMev%252BI8OAIh4zdH3vfirWV8efHblzZXxvTNvPsX2KT5Nq%252F4f9lKTJayP6PLeHo9DGz0mm9tBsBPmg2XYOdLePEVskjQ6hPSqTBnzjfvS2t6EC0Mwpgdr8S61mSeaGOyJ4tHHhNThfmi0S7cy%252FbMWtztspfNHsV5GSnlGnmOkcWDs114qePnJZxOUMCIzsGC6Blxc2EPXpvvg4M80ZTMTvaQpc%252FZISucY996qEjQWXryus5II2je3cu%252F2snXmU8zyoMaHgAVZ05UZoAcJ7fIIF955pizzbmhdJdEu3sNFPxnd3vK0nUrKWtQpmswXkT2cQp9mNC79dxreY28nGrsruzp5UB1Q3Jy7nUcTg66aTl4FdjRc4xgHpFCP08tbrM8lY2M72fEsWciF7lu0eHPv1mbYvB5nYaqBq%252F9ey6%252Flwt01fm43qha96vEKTO0qWtCJUVt4Fl%252BKJDTX19n0AYljw21cZdi%252BWrK1TicGRmm30m7N7SioMTkK%252BTmqk5283YU3oGSb%252BbzJnTVR5olD9HIlretmW2EaY5spqtZkXoR17p9%252FAQeials%253D"
    headers = {
        'Pragma': "no-cache",
        'Origin': "https://h5.waimai.meituan.com",
        'Accept-Encoding': "gzip, deflate, br",
        'Accept-Language': "zh-CN,zh;q=0.9",
        'User-Agent': "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Mobile Safari/537.36",
        'Content-Type': "application/x-www-form-urlencoded",
        'Accept': "application/json",
        'Cache-Control': "no-cache",
        'Referer': "https://h5.waimai.meituan.com/waimai/mindex/kingkong?navigateType=910&firstCategoryId=910&secondCategoryId=910&title=%E7%BE%8E%E9%A3%9F",
        'Cookie': "_lxsdk_cuid=17258e9bdcdc8-035b6212353d98-3f674604-144000-17258e9bdcec8; _ga=GA1.3.147549955.1594021774; _gid=GA1.3.423744456.1594021774; PHPSESSID=2huep8pinvja6qbllf74f3i9v2; Hm_lvt_f66b37722f586a240d4621318a5a6ebe=1594021789; Hm_lpvt_f66b37722f586a240d4621318a5a6ebe=1594021789; __utma=211559370.1176947614.1594021789.1594021789.1594021789.1; __utmc=211559370; __utmz=211559370.1594021789.1.1.utmcsr=baidu|utmccn=baidu|utmcmd=organic|utmcct=zt_search; __mta=256621876.1594021776291.1594021855987.1594021868864.3; wm_order_channel=default; utm_source=; au_trace_key_net=default; terminal=i; w_utmz=utm_campaign = (direct) & utm_source = 5000 & utm_medium = (none) & utm_content = (none) & utm_term = (none); service-off=0; iuuid=6380715355AE14B00A89CB58B703AE8B7B225A362A48E83E064FC01825F81709; _lxsdk=6380715355AE14B00A89CB58B703AE8B7B225A362A48E83E064FC01825F81709; openh5_uuid=6380715355AE14B00A89CB58B703AE8B7B225A362A48E83E064FC01825F81709; uuid=6380715355AE14B00A89CB58B703AE8B7B225A362A48E83E064FC01825F81709; openh5_uuid=6380715355AE14B00A89CB58B703AE8B7B225A362A48E83E064FC01825F81709; userId=2724915169; w_visitid=51e61e94-c03d-421e-815e-85145d63265d; token=GSRXwDLy_CCZdBpKhsXiWXURTWQAAAAAAQsAAFKn6Qr1uxoVpu__QcUz2sS_sTfpFzpZd98Pnsu5iKvXePglL-mZpNSxZb2eGm6gTQ; mt_c_token=GSRXwDLy_CCZdBpKhsXiWXURTWQAAAAAAQsAAFKn6Qr1uxoVpu__QcUz2sS_sTfpFzpZd98Pnsu5iKvXePglL-mZpNSxZb2eGm6gTQ; oops=GSRXwDLy_CCZdBpKhsXiWXURTWQAAAAAAQsAAFKn6Qr1uxoVpu__QcUz2sS_sTfpFzpZd98Pnsu5iKvXePglL-mZpNSxZb2eGm6gTQ; w_token=GSRXwDLy_CCZdBpKhsXiWXURTWQAAAAAAQsAAFKn6Qr1uxoVpu__QcUz2sS_sTfpFzpZd98Pnsu5iKvXePglL-mZpNSxZb2eGm6gTQ; w_actual_lat=31489100; w_actual_lng=120306289; w_latlng=31489100,120306289; cssVersion=ed62e738; _lx_utm=utm_source%3D; _lxsdk_s=173231a0445-802-fc0-941%7C%7C180",
    'Connection': "keep-alive",
    'cache-control': "no-cache",
    'Postman-Token': "4b051608-c8db-422c-b9d5-9ffcb8066ac5"
    }

    response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

    print(response.text)
def main():
    get_shops()


if __name__ == '__main__':
    main()
