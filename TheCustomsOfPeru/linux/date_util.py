import time

'''
获取时间戳
'''


def get_timestamp():
    return int(time.time() * 1000)


'''
获取格林尼治时间
'''


def get_date():
    from datetime import datetime
    GMT_FORMAT = '%a, %d %b %Y %H:%M:%S GMT'
    return datetime.utcnow().strftime(GMT_FORMAT)
