import urllib.request
import http.cookiejar
url = 'https://news.163.com/20/0409/11/F9P524V4000189FH.html'
cjar = http.cookiejar.CookieJar()

proxy = urllib.request.ProxyHandler({'http':'127.0.0.1:8888'})
opener = urllib.request.build_opener(proxy,urllib.request.HTTPHandler,urllib.request.HTTPCookieProcessor(cjar))

urllib.request.install_opener(opener)

data = urllib.request.urlopen(url).read()
fhandler = open('D:/pycharmproject/pythonlearning/file/4.html','wb')
fhandler.write(data)
fhandler.close()