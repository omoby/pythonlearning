import re
import urllib.request
import urllib.error
import csv
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
"""
抓取课程splider
"""
'''
获取淘宝教育课程首页的内容，包括所有课程分类列表
课程列表首页：url = "https://i.xue.taobao.com/list.htm?spm=a2174.7365761.0.0.l8eeIN"
所有课程分类列表：
[['i.xue.taobao.com/list.htm?firstCat=52272004@学历教育', 'i.xue.taobao.com/list.htm?firstCat=52272004&secondCat=53934130||专升本', 'i.xue.taobao.com/list.htm?firstCat=52272004&secondCat=52276007||技校', 'i.xue.taobao.com/list.htm?firstCat=52272004&secondCat=52284021||其他学历'], ['i.xue.taobao.com/list.htm?firstCat=57206007@语言学习线上培训'], ['i.xue.taobao.com/list.htm?firstCat=52302004@技能培训', 'i.xue.taobao.com/list.htm?firstCat=52302004&secondCat=57254001||职业管理', 'i.xue.taobao.com/list.htm?firstCat=52302004&secondCat=52286007||其他技能', 'i.xue.taobao.com/list.htm?firstCat=52302004&secondCat=57090002||驾驶技能', 'i.xue.taobao.com/list.htm?firstCat=52302004&secondCat=52274005||专业设计', 'i.xue.taobao.com/list.htm?firstCat=52302004&secondCat=52296008||影音制作', 'i.xue.taobao.com/list.htm?firstCat=52302004&secondCat=52294005||IT技能', 'i.xue.taobao.com/list.htm?firstCat=52302004&secondCat=57280001||it编程'], ['i.xue.taobao.com/list.htm?firstCat=52334002@外语课程', 'i.xue.taobao.com/list.htm?firstCat=52334002&secondCat=56498006||留学游学', 'i.xue.taobao.com/list.htm?firstCat=52334002&secondCat=52288005||英语四六级', 'i.xue.taobao.com/list.htm?firstCat=52334002&secondCat=53936148||英语入门', 'i.xue.taobao.com/list.htm?firstCat=52334002&secondCat=57256001||小语种', 'i.xue.taobao.com/list.htm?firstCat=52334002&secondCat=54016122||GRE/GMAT', 'i.xue.taobao.com/list.htm?firstCat=52334002&secondCat=53952113||PETS', 'i.xue.taobao.com/list.htm?firstCat=52334002&secondCat=52274004||商务英语', 'i.xue.taobao.com/list.htm?firstCat=52334002&secondCat=52322003||其他语言', 'i.xue.taobao.com/list.htm?firstCat=52334002&secondCat=53958136||SAT', 'i.xue.taobao.com/list.htm?firstCat=52334002&secondCat=52312003||雅思托福', 'i.xue.taobao.com/list.htm?firstCat=52334002&secondCat=52374015||英语口语', 'i.xue.taobao.com/list.htm?firstCat=52334002&secondCat=53944149||汉语培训'], ['i.xue.taobao.com/list.htm?firstCat=52274003@文体艺术', 'i.xue.taobao.com/list.htm?firstCat=52274003&secondCat=52272007||科学/文化', 'i.xue.taobao.com/list.htm?firstCat=52274003&secondCat=52272006||主持表演', 'i.xue.taobao.com/list.htm?firstCat=52274003&secondCat=52270005||声乐培训', 'i.xue.taobao.com/list.htm?firstCat=52274003&secondCat=54032129||茶艺/插花', 'i.xue.taobao.com/list.htm?firstCat=52274003&secondCat=52290007||其他文体培训', 'i.xue.taobao.com/list.htm?firstCat=52274003&secondCat=53978109||影视编导', 'i.xue.taobao.com/list.htm?firstCat=52274003&secondCat=52338003||体育', 'i.xue.taobao.com/list.htm?firstCat=52274003&secondCat=52310006||乐器培训', 'i.xue.taobao.com/list.htm?firstCat=52274003&secondCat=52326004||舞蹈', 'i.xue.taobao.com/list.htm?firstCat=52274003&secondCat=52284007||绘画书法'], ['i.xue.taobao.com/list.htm?firstCat=52328004@职业考试', 'i.xue.taobao.com/list.htm?firstCat=52328004&secondCat=52272005||司法考试', 'i.xue.taobao.com/list.htm?firstCat=52328004&secondCat=52320005||会计考试', 'i.xue.taobao.com/list.htm?firstCat=52328004&secondCat=52292007||教师资格证', 'i.xue.taobao.com/list.htm?firstCat=52328004&secondCat=52292006||公务员考试', 'i.xue.taobao.com/list.htm?firstCat=52328004&secondCat=53980119||银行/证券', 'i.xue.taobao.com/list.htm?firstCat=52328004&secondCat=52326003||IT认证', 'i.xue.taobao.com/list.htm?firstCat=52328004&secondCat=52300008||其他职业认证', 'i.xue.taobao.com/list.htm?firstCat=52328004&secondCat=52300006||建设工程考试', 'i.xue.taobao.com/list.htm?firstCat=52328004&secondCat=54014145||医疗'], ['i.xue.taobao.com/list.htm?firstCat=52310005@中小学辅导', 'i.xue.taobao.com/list.htm?firstCat=52310005&secondCat=53954102||少儿培训', 'i.xue.taobao.com/list.htm?firstCat=52310005&secondCat=52298007||高中', 'i.xue.taobao.com/list.htm?firstCat=52310005&secondCat=52282006||初中', 'i.xue.taobao.com/list.htm?firstCat=52310005&secondCat=52286008||中小学家长教育', 'i.xue.taobao.com/list.htm?firstCat=52310005&secondCat=52338004||小学', 'i.xue.taobao.com/list.htm?firstCat=52310005&secondCat=52316004||学科辅导'], ['i.xue.taobao.com/list.htm?firstCat=57232004@生活兴趣线上培训'], ['i.xue.taobao.com/list.htm?firstCat=52284006@生活百科', 'i.xue.taobao.com/list.htm?firstCat=52284006&secondCat=52282005||日常兴趣', 'i.xue.taobao.com/list.htm?firstCat=52284006&secondCat=57260001||摄影摄像', 'i.xue.taobao.com/list.htm?firstCat=52284006&secondCat=52306003||健康养生', 'i.xue.taobao.com/list.htm?firstCat=52284006&secondCat=54188002||其他生活百科培训', 'i.xue.taobao.com/list.htm?firstCat=52284006&secondCat=57262001||美术绘画', 'i.xue.taobao.com/list.htm?firstCat=52284006&secondCat=52294006||美容美妆'], ['i.xue.taobao.com/list.htm?firstCat=57226002@职业技能线上培训']]
'''
def getfaceage():
    url = "https://i.xue.taobao.com/list.htm?spm=a2174.7365761.0.0.l8eeIN"

    headers = {'user-agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.9 Safari/537.36'}
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
        print('facepageurl: ' + url)
        print(data)
        print(e.reason)

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
    return alllist


'''
拆分每一个大类中的小类
['i.xue.taobao.com/list.htm?firstCat=52272004@学历教育', 'i.xue.taobao.com/list.htm?firstCat=52272004&secondCat=53934130||专升本', 'i.xue.taobao.com/list.htm?firstCat=52272004&secondCat=52276007||技校', 'i.xue.taobao.com/list.htm?firstCat=52272004&secondCat=52284021||其他学历'], ['i.xue.taobao.com/list.htm?firstCat=57206007@语言学习线上培训']
'''
def getdetailpage(listall):
    # 从课程类列表中取出一类课程
    for item in listall:
        i = 0
        #取出课程的大类
        prev = item[i]
        #获取大类的名称的url和大类名称
        prevurl = prev.split("@")[0]
        prevname = prev.split("@")[1]
        i += 1
        # 如果大类中没有中类，大类的长度为1.直接便利大类
        if len(item)==1:
            analysiscourselist(prevurl,0,0,prevname,"")

        # 如果大类中有中类，大类的长度大于1.便利中类
        else:
            while i < len(item):
                sub = item[i]
                suburl = sub.split("||")[0]
                subname = sub.split("||")[1]
                analysiscourselist(suburl,0,0,prevname,subname)
                i += 1


'''
将爬去的数据保存到csv文件中
datalist:写如文件的数据
writetype:写入的文件的类型 ‘w’:打开文件用于写入，文件有数据就覆盖，‘a’:打开文件用于写入数据，如果存在数据就追加
'''
def saveascsv(datalist,writetype):
    csvpath = "D:\\pycharmproject\\pythonlearning\\file\\xueedusplider.csv"
    with open(csvpath, writetype,newline='',encoding='gbk') as f:
        writer = csv.writer(f)
        # 将列表的每条数据依次写入csv文件， 并以逗号分隔
        writer.writerow(datalist)
        # if len(datalist)==0 or datalist.pop()=='':
        #     writer.close()
        # else:
        #     writer.writerrows(datalist)
        #     writer.close()

'''
获取学员评论总数
由于评论总数是异步请求的，在爬去课程详情页时还没有加载到评论的条数
'''
def getcommentcount(url,suburl):
    req = urllib.request.Request(suburl)
    # 添加header信息
    req.add_header('user-agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.9 Safari/537.36')
    # 由于请求的连接是建立在详情页上面的，需要在header上添加详情页的信息，否则请求不到数据
    req.add_header("Referer",url)
    file = ''
    try:
        file = urllib.request.urlopen(req)
    except urllib.error.HTTPError as e:
        print('commentcountpreurl: '+url)
        print(e.reason)
    # 匹配评论数的正则表达式
    patcommenttotal = '"totalFull":(\d+)'
    data = file.read()
    try:
        data = data.decode("gbk")
        commenttotal = re.compile(patcommenttotal).findall(data)
        return commenttotal[0]
    except UnicodeDecodeError as e:
        print(suburl)
        print(data)
        print(e.reason)
        return -1


'''
解析每一个中类的列表页面
https://i.xue.taobao.com/detail.htm?courseId=57528
大专本科在线提升
大专本科在线提升
免费
||
https://i.xue.taobao.com/detail.htm?courseId=50335
单片机毕业设计
单片机毕业设计
免费
'''
def analysiscourselist(url,pagenum,pageindex,prevname,subname):
    pageurl = "https://"
    if pageindex != 0:
        pageurl = pageurl + url+"&page="+str(pageindex)
    else:
        pageurl = pageurl+url
    # 添加请求课程列表页的header信息
    headers = {'user-agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.9 Safari/537.36'}
    opener = urllib.request.build_opener()
    opener.addheaders = [headers]
    urllib.request.install_opener(opener)
    file = ''
    try:
        file = urllib.request.urlopen(pageurl)
    except urllib.error.HTTPError as e:
        print('pageurl: '+pageurl)
        print(e.reason)
    data = file.read()
    try:
        data = data.decode("gbk")

        # 匹配每一个列表页的正则表达式
        patpagenum =  '<span class="num">1</span>/(\d+)'
        if(pagenum==0):
            pagenumlist = re.compile(patpagenum).findall(data)
            pagenum = int(pagenumlist[0])

        # 匹配页面中的每一门课程正则表达式
        patcourselist = '(<div class="course ">|<div class="course course-right">)([\s\S]+?)</div>\\r\\n\s*</div>\\r\\n\s*</div>'
        # 获取到页面上的课程列表的div
        pagelist = re.compile(patcourselist).findall(data)

        # 匹配课程列表div中的课程地址正则表达式
        patcourseulr = '<div class="name">\\r\\n\s*<a href="(//.+?)"'
        # 匹配课程围观数正则表达式
        patregistcount = '<span class="peo">[\s\S]+?(\d+)[\s\S]+?</span>'

        # 遍历每一页的课程列表
        for sub in pagelist:
            value = sub[1]
            # 获取到课程地址['https://i.xue.taobao.com/detail.htm?courseId=48092']
            courseurllsit = re.compile(patcourseulr).findall(value)
            # 获取到围观数['40']
            registcountlist = re.compile(patregistcount).findall(value)

            # 存在课程地址继续遍历课程详情页面
            if len(courseurllsit) == 1:
                courseurl = "https:" + courseurllsit[0]
                headers = {'user-agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.9 Safari/537.36'}
                opener = urllib.request.build_opener()
                opener.addheaders = [headers]
                urllib.request.install_opener(opener)
                file = ''
                try:
                    file = urllib.request.urlopen(courseurl)
                except urllib.error.HTTPError as e:
                    print('courseurl: '+courseurl)
                    print(e.reason)
                data = file.read()
                try:
                    data = data.decode("gbk")

                    # 匹配现价正则表达式
                    patoriginPrice = '"originPrice":"(\d*\.?\d*)"'
                    # 匹配原价正则表达式
                    patpriceYuan = '"priceYuan":"(\d*\.?\d*)"'
                    # 匹配课程是否是免费正则表达式
                    patfreee  = '"freeCourse":(.+?),'
                    # 匹配课程订单正则表达式
                    patordercount = '"orderCount":(\d*\.?\d*)'
                    # 匹配讲师url正则表达式
                    patteatcherurl = '"teacherDetailUrl":"//(.+?)"'
                    # 匹配讲师简介正则表达式
                    patteatcherintro = '"teacherIntro":"(.+?)"'
                    # 匹配讲师昵称正则表达式
                    patteatchernick = '"teacherNick":"(.+?)"'
                    # 匹配评论详情页面url正则表达式
                    patcommenturl = '"evCommonApi":"//([\s\S]*?)"'
                    # 匹配店铺名正则表达式
                    patshopname = '"shopName":"(.+?)"'
                    # 匹配店铺url正则表达式
                    patshopurl = '"shopUrl":"//(.+?)"'
                    # 匹配课程名正则表达式
                    patcoursename = '"title":"(.+?)"'

                    #  现价['1.00']
                    pricelist = re.compile(patpriceYuan).findall(data)
                    # 原价['1.00']
                    delpricelist = re.compile(patoriginPrice).findall(data)
                    # 是否免费['true'] or ['false']
                    freelist = re.compile(patfreee).findall(data)
                    # 学习人数['23']
                    ordercountlist = re.compile(patordercount).findall(data)
                    # 讲师url[’‘]
                    teatcherurllist = re.compile(patteatcherurl).findall(data)
                    # 讲师简介[]
                    teatcherintrolist = re.compile(patteatcherintro).findall(data)
                    # 讲师昵称[]
                    teatchernicklist = re.compile(patteatchernick).findall(data)
                    # 评论详情页地址[]
                    commenturllist = re.compile(patcommenturl).findall(data)
                    # 店铺名称[]
                    shopnamelist = re.compile(patshopname).findall(data)
                    # 店铺url
                    shopurllist = re.compile(patshopurl).findall(data)
                    # 课程名称
                    coursenamelist = re.compile(patcoursename).findall(data)

                    courseurl='https:'+courseurllsit[0]
                    coursename = coursenamelist[0]
                    ordercount = ordercountlist[0]
                    commentcount=''

                    if len(commenturllist)==0 or commenturllist[0]=='':
                        commentcount = 0
                    else:
                        commenturl ='https://'+ commenturllist.pop(0)
                        commentcount = getcommentcount(courseurl, commenturl)

                    shopname=''
                    shopurl=''
                    if len(shopnamelist)!=0 and shopnamelist[0] !='':
                        shopname='机构：'+shopnamelist[0]
                        shopurl ='https://'+ shopurllist[0]
                    elif len(teatchernicklist)!=0 and teatchernicklist[0] != '':
                        shopname = '讲师：'+teatchernicklist[0]
                        shopurl = 'https://'+ teatcherurllist[0]

                    registcount = registcountlist[0]
                    delprice = 0.00
                    if len(delpricelist)!=0 and delpricelist[0]!='':
                        delprice = delpricelist[0]

                    newprice =-1
                    if freelist.pop(0)=='false':
                        newprice = pricelist[0]

                    row=[courseurl,coursename,ordercount,commentcount,shopname,shopurl,prevname,subname,registcount,delprice,newprice]
                    saveascsv(row,'a')
                except UnicodeDecodeError as e:
                    print(courseurl)
                    print(data)
                    print(e.reason)
    except UnicodeDecodeError as e:
        print(pageurl)
        print(data)
        print(e.reason)
        # return -1
    # 分类列表中有多页
    if pagenum > 1:
        index=0
        if(pageindex == 0):
            index = 2
        else:
            index = pageindex +1
        if index <= pagenum:
            analysiscourselist(url,pagenum,index,prevname,subname)

listall = getfaceage()
title = ['courseUrl','courseName','orderCount','commentCount','shopName','shopUrl','extensiveClass','concreteClass','registCount','originPrice','newPrice']
saveascsv(title,'w')
getdetailpage(listall)
# analysiscourselist("i.xue.taobao.com/list.htm?firstCat=57206007",32,31,"语言学习线上培训",'')