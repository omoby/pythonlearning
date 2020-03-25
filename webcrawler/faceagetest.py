import re
import urllib.request
import urllib.error
import csv
def getfaceage():
    url = "https://i.xue.taobao.com/list.htm?spm=a2174.7365761.0.0.l8eeIN"

    headers = {'user-agent',
               'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.9 Safari/537.36'}
    opener = urllib.request.build_opener()
    opener.addheaders = [headers]
    urllib.request.install_opener(opener)
    file = ''
    try:
        file = urllib.request.urlopen(url)
    except urllib.error.HTTPError as e:
        print('facepageurl: ' + url)
        print(e.reason)
    data = file.read()
    try:
        data = data.decode("gbk")
    except UnicodeDecodeError as e:
        print('facepageurl: '+url)
        print(data)
        print(e.reason)
        return -1

    pat2 = '<div class="filter-row[\s\S]+? </div>'
    keclass = re.compile(pat2).findall(data)
    patspanurl = '<span class="cat".+? href="//(.+?)">(.+?)</a></span>'
    patliurl = '<li class="sm-item"><a href="//(.+?)">(.+?)</a></li>'
    alllist = []
    spanlist = []
    lilist = []
    for subdetail in keclass:
        span = re.compile(patspanurl).findall(subdetail)
        li = re.compile(patliurl).findall(subdetail)
        url = span[0][0]
        name = span[0][1]
        spanlist.append(url + "@" + name)
        for sub in li:
            suburl = sub[0].replace("&amp;", "&")
            subname = sub[1]
            lilist.append(suburl + "||" + subname)
        alllist.append(spanlist + lilist)
        spanlist.clear()
        lilist.clear()
    print(alllist)
    return alllist
getfaceage()