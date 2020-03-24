import re
import urllib.request
import urllib.error

def craw(url,page):
    print(url)
    html1 = urllib.request.urlopen(url).read()
    html1 = str(html1)
    pat1 = '<div id="plist".+? <div class="page clearfix"'
    result1 = re.compile(pat1).findall(html1)
    result1 = result1[0]
    pat2 = '<img width="220" height="220" data-img="1" data-lazy-img="//(.+?\.jpg)">'
    imglist = re.compile(pat2).findall(result1)
    x = 1
    for imgurl in imglist:
        print(imgurl)
        if imgurl.endswith('.jpg'):
            imgname = "/home/hadoop/webcrawler/jdimg/"+str(page)+str(x)+".jpg"
            imgurl = "https://"+imgurl
            print(imgurl)
            print(imgname)
            try:
                urllib.request.urlretrieve(imgurl,filename=imgname)
            except urllib.error.URLError as e:
                if hasattr(e,"code"):
                    print(e.code)
                    x += 1
                if hasattr(e,"reason"):
                    x += 1
                    print(e.reason)
            except urllib.error.HTTPError as e:
                if hasattr(e,"code"):
                    print(e.code)
                    x += 1
                if hasattr(e,"reason"):
                    x += 1
                    print(e.reason)
        x += 1
for i in range(1,136):
    url = "https://list.jd.com/list.html?cat=9987,653,655&page="+str(i)+"&sort=sort_rank_asc&trans=1&JL=6_0_0#J_main"
    craw(url,i)
