import  urllib.request

for i in range(1,100):
    try:
        file = urllib.request.urlopen("https://www.baidu.com", timeout=0.1)
        data = file.read()
        print(data)
    except Exception as e:
        print("出现异常："+str(e))