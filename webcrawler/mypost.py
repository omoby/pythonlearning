import urllib.request

import urllib.parse
url = "http://www.iqianyue.com/mypost"
postdata = urllib.parse.urlencode({
    "name":"ceo@iqianque.com",
    "pass":"aA123456"
}).encode("utf-8")

req = urllib.request.Request(url,postdata)

req.add_header('User-Agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36')
data = urllib.request.urlopen(req).read()
fhandle = open("/home/hadoop/webcrawler/4.html",'wb')
fhandle.write(data)
fhandle.close()