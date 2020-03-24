import re
import urllib.request
import urllib.error
'''
获取淘宝教育课程首页的内容，包括所有课程分类列表
课程列表首页：url = "https://i.xue.taobao.com/list.htm?spm=a2174.7365761.0.0.l8eeIN"
所有课程分类列表：
[['i.xue.taobao.com/list.htm?firstCat=52272004@学历教育', 'i.xue.taobao.com/list.htm?firstCat=52272004&secondCat=53934130||专升本', 'i.xue.taobao.com/list.htm?firstCat=52272004&secondCat=52276007||技校', 'i.xue.taobao.com/list.htm?firstCat=52272004&secondCat=52284021||其他学历'], ['i.xue.taobao.com/list.htm?firstCat=57206007@语言学习线上培训'], ['i.xue.taobao.com/list.htm?firstCat=52302004@技能培训', 'i.xue.taobao.com/list.htm?firstCat=52302004&secondCat=57254001||职业管理', 'i.xue.taobao.com/list.htm?firstCat=52302004&secondCat=52286007||其他技能', 'i.xue.taobao.com/list.htm?firstCat=52302004&secondCat=57090002||驾驶技能', 'i.xue.taobao.com/list.htm?firstCat=52302004&secondCat=52274005||专业设计', 'i.xue.taobao.com/list.htm?firstCat=52302004&secondCat=52296008||影音制作', 'i.xue.taobao.com/list.htm?firstCat=52302004&secondCat=52294005||IT技能', 'i.xue.taobao.com/list.htm?firstCat=52302004&secondCat=57280001||it编程'], ['i.xue.taobao.com/list.htm?firstCat=52334002@外语课程', 'i.xue.taobao.com/list.htm?firstCat=52334002&secondCat=56498006||留学游学', 'i.xue.taobao.com/list.htm?firstCat=52334002&secondCat=52288005||英语四六级', 'i.xue.taobao.com/list.htm?firstCat=52334002&secondCat=53936148||英语入门', 'i.xue.taobao.com/list.htm?firstCat=52334002&secondCat=57256001||小语种', 'i.xue.taobao.com/list.htm?firstCat=52334002&secondCat=54016122||GRE/GMAT', 'i.xue.taobao.com/list.htm?firstCat=52334002&secondCat=53952113||PETS', 'i.xue.taobao.com/list.htm?firstCat=52334002&secondCat=52274004||商务英语', 'i.xue.taobao.com/list.htm?firstCat=52334002&secondCat=52322003||其他语言', 'i.xue.taobao.com/list.htm?firstCat=52334002&secondCat=53958136||SAT', 'i.xue.taobao.com/list.htm?firstCat=52334002&secondCat=52312003||雅思托福', 'i.xue.taobao.com/list.htm?firstCat=52334002&secondCat=52374015||英语口语', 'i.xue.taobao.com/list.htm?firstCat=52334002&secondCat=53944149||汉语培训'], ['i.xue.taobao.com/list.htm?firstCat=52274003@文体艺术', 'i.xue.taobao.com/list.htm?firstCat=52274003&secondCat=52272007||科学/文化', 'i.xue.taobao.com/list.htm?firstCat=52274003&secondCat=52272006||主持表演', 'i.xue.taobao.com/list.htm?firstCat=52274003&secondCat=52270005||声乐培训', 'i.xue.taobao.com/list.htm?firstCat=52274003&secondCat=54032129||茶艺/插花', 'i.xue.taobao.com/list.htm?firstCat=52274003&secondCat=52290007||其他文体培训', 'i.xue.taobao.com/list.htm?firstCat=52274003&secondCat=53978109||影视编导', 'i.xue.taobao.com/list.htm?firstCat=52274003&secondCat=52338003||体育', 'i.xue.taobao.com/list.htm?firstCat=52274003&secondCat=52310006||乐器培训', 'i.xue.taobao.com/list.htm?firstCat=52274003&secondCat=52326004||舞蹈', 'i.xue.taobao.com/list.htm?firstCat=52274003&secondCat=52284007||绘画书法'], ['i.xue.taobao.com/list.htm?firstCat=52328004@职业考试', 'i.xue.taobao.com/list.htm?firstCat=52328004&secondCat=52272005||司法考试', 'i.xue.taobao.com/list.htm?firstCat=52328004&secondCat=52320005||会计考试', 'i.xue.taobao.com/list.htm?firstCat=52328004&secondCat=52292007||教师资格证', 'i.xue.taobao.com/list.htm?firstCat=52328004&secondCat=52292006||公务员考试', 'i.xue.taobao.com/list.htm?firstCat=52328004&secondCat=53980119||银行/证券', 'i.xue.taobao.com/list.htm?firstCat=52328004&secondCat=52326003||IT认证', 'i.xue.taobao.com/list.htm?firstCat=52328004&secondCat=52300008||其他职业认证', 'i.xue.taobao.com/list.htm?firstCat=52328004&secondCat=52300006||建设工程考试', 'i.xue.taobao.com/list.htm?firstCat=52328004&secondCat=54014145||医疗'], ['i.xue.taobao.com/list.htm?firstCat=52310005@中小学辅导', 'i.xue.taobao.com/list.htm?firstCat=52310005&secondCat=53954102||少儿培训', 'i.xue.taobao.com/list.htm?firstCat=52310005&secondCat=52298007||高中', 'i.xue.taobao.com/list.htm?firstCat=52310005&secondCat=52282006||初中', 'i.xue.taobao.com/list.htm?firstCat=52310005&secondCat=52286008||中小学家长教育', 'i.xue.taobao.com/list.htm?firstCat=52310005&secondCat=52338004||小学', 'i.xue.taobao.com/list.htm?firstCat=52310005&secondCat=52316004||学科辅导'], ['i.xue.taobao.com/list.htm?firstCat=57232004@生活兴趣线上培训'], ['i.xue.taobao.com/list.htm?firstCat=52284006@生活百科', 'i.xue.taobao.com/list.htm?firstCat=52284006&secondCat=52282005||日常兴趣', 'i.xue.taobao.com/list.htm?firstCat=52284006&secondCat=57260001||摄影摄像', 'i.xue.taobao.com/list.htm?firstCat=52284006&secondCat=52306003||健康养生', 'i.xue.taobao.com/list.htm?firstCat=52284006&secondCat=54188002||其他生活百科培训', 'i.xue.taobao.com/list.htm?firstCat=52284006&secondCat=57262001||美术绘画', 'i.xue.taobao.com/list.htm?firstCat=52284006&secondCat=52294006||美容美妆'], ['i.xue.taobao.com/list.htm?firstCat=57226002@职业技能线上培训']]
'''
def getfaceage():
    url = "https://i.xue.taobao.com/list.htm?spm=a2174.7365761.0.0.l8eeIN"
    # url = "/home/hadoop/webcrawler/xue.html"
    print(url)
    headers = {"User-Agent",
               "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"}
    opener = urllib.request.build_opener()
    opener.addheaders = [headers]
    urllib.request.install_opener(opener)
    file = urllib.request.urlopen(url)
    data = str(file.read())
    print(data)
    # html1 = urllib.request.urlopen(url).read()
    # html1 = str(html1)
    # pat1 = '<div  '
    pat1 = '<div class="filters".+? <div class="sort-bar"'
    result1 = re.compile(pat1).findall(data)
    print(result1)
    result1 = result1[0]
    print(result1)
    pat2 = '<div class="filter-row.+? </div>'
    keclass = re.compile(pat2).findall(result1)
    print("----"*20)
    print(keclass)
    print("----" * 20)
    patspanurl = '<span class="cat".+? href="//(.+?)">(.+?)</a></span>'
    patliurl = '<li class="sm-item"><a href="//(.+?)">(.+?)</a></li>'
    alllist=[]
    spanlist = []
    lilist = []
    for subdetail in keclass:
        span = re.compile(patspanurl).findall(subdetail)
        li = re.compile(patliurl).findall(subdetail)
        print(subdetail)
        print(span)
        print(li)
        url = span[0][0]
        name = eval(repr(span[0][1]).replace("\\\\","\\")).encode('raw_unicode_escape').decode("gbk")
        spanlist.append(url+"@"+name)
        print(url)
        print(name)
        for sub in li:
            suburl = sub[0].replace("&amp;","&")
            subname = eval(repr(sub[1]).replace("\\\\", "\\")).encode('raw_unicode_escape').decode("gbk")
            lilist.append(suburl+"||"+subname)
        alllist.append(spanlist+lilist)
        print(spanlist)
        print(lilist)
        spanlist.clear()
        lilist.clear()
    print(alllist)
    return alllist

    # imglist = re.compile(pat2).findall(result1)
    # x = 1
    # for imgurl in imglist:
    #     if imgurl.endswith('.jpg'):
    #         imgname = "/home/hadoop/webcrawler/jdimg/"+str(page)+str(x)+".jpg"
    #         imgurl = "https://"+imgurl
    #         print(imgurl)
    #         print(imgname)
    #         try:
    #             urllib.request.urlretrieve(imgurl,filename=imgname)
    #         except urllib.error.URLError as e:
    #             if hasattr(e,"code"):
    #                 print(e.code)
    #                 x += 1
    #             if hasattr(e,"reason"):
    #                 x += 1
    #                 print(e.reason)
    #         except urllib.error.HTTPError as e:
    #             if hasattr(e,"code"):
    #                 print(e.code)
    #                 x += 1
    #             if hasattr(e,"reason"):
    #                 x += 1
    #                 print(e.reason)
    #     x += 1


getfaceage()
