import urllib.request

keywd = "hello"
url = "https://www.baidu.com/s?wd="+keywd
print(url)
req = urllib.request.Request(url)
data = urllib.request.urlopen(req).read()
fhander = open("/home/hadoop/webcrawler/3.html","wb")
fhander.write(data)
fhander.close()