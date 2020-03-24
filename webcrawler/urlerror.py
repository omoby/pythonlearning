import urllib.request
import urllib.error

try:
    data = urllib.request.urlopen("http://blog.csdnsss.net")
    print(data)
except urllib.error.HTTPError as e:
    print(e.code)
    print(e.reason)
except urllib.error.URLError as e:
    # print(e.code)
    print(e.reason)