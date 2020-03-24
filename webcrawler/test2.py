s = 'cdp\nd'
result = eval(repr(s).replace('\\', '@'))
print(result)

string4 = "\\xc8\\xd5\\xb3\\xa3\\xd0\\xcb\\xc8\\xa4"
result2 = eval(repr(string4).replace("\\\\","\\"))
# print(result2)
# print(type(result2))
ss = result2.encode('raw_unicode_escape')
print(type(ss))
print(ss)
sss = ss.decode("gbk")
print(sss)
