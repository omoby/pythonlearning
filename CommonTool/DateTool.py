import time


def get_timestamp():
    '''
    获取时间戳
    :return:
    '''
    return int(time.time() * 1000)


def get_date():
    '''
    获取格林尼治时间
    :return:
    '''
    from datetime import datetime
    GMT_FORMAT = '%a, %d %b %Y %H:%M:%S GMT'
    return datetime.utcnow().strftime(GMT_FORMAT)
