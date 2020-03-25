import re
import urllib.request
import urllib.error
'''
请求评论数据
'''
def getcommentcount(url,suburl):
    req = urllib.request.Request(suburl)
    # 添加header信息
    req.add_header("User-Agent","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36")
    # 由于请求的连接是建立在详情页上面的，需要在header上添加详情页的信息，否则请求不到数据
    req.add_header("Referer",url)
    file = ''
    try:
        file = urllib.request.urlopen(url)
    except urllib.error.HTTPError as e:
        print('commentcountlurl: ' + url)
        print(e.reason)
    data = file.read()

    try:
        data = data.decode("gbk")
    except UnicodeDecodeError as e:
        print(data)
        print(e.reason)
    print(data)
    # 匹配评论数的正则表达式
    patcommenttotal = '"totalFull":(\d+)'
    total = re.compile(patcommenttotal).findall(data)
    print(total[0])
'''
用于测试匹配详情页面页面中的评论数连接
'''
def analysispagedetail(url):
    headers = {"User-Agent",
               "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"}

    opener = urllib.request.build_opener()
    opener.addheaders = [headers]
    urllib.request.install_opener(opener)
    file = ''
    try:
        file = urllib.request.urlopen(url)
    except urllib.error.HTTPError as e:
        print('coursedetailurl: '+url)
        print(e.reason)

    data = file.read()

    try:
        data = data.decode("gbk")
    except UnicodeDecodeError as e:
        print(data)
        print(e.reason)

    # "evCommonApi":"//rate.taobao.com/detailCommon.htm?userNumId=2201264572608&auctionNumId=602929401807&siteID=12&spuId=0"
    patcommentcounturl = '"evCommonApi":"//([\s\S]*?)"'

    commentcounturl = re.compile(patcommentcounturl).findall(data)
    print(commentcounturl)
    if len(commentcounturl)==0 or commentcounturl[0]=='':
        print(0)
    else:
        print(commentcounturl)
        suburl = 'https://'+commentcounturl.pop(0)
        getcommentcount(url,suburl)


url = ''
analysispagedetail(url)