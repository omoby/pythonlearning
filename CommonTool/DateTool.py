import math
import time


def get_timestamp():
    '''
    获取时间戳,1597911621403
    :return:
    '''
    return int(time.time() * 1000)


def get_date():
    '''
    获取格林尼治时间, Thu, 20 Aug 2020 08:19:39 GMT
    :return:
    '''
    from datetime import datetime
    GMT_FORMAT = '%a, %d %b %Y %H:%M:%S GMT'
    return datetime.utcnow().strftime(GMT_FORMAT)


'''
#!/usr/bin/python3

import time

# 格式化成2016-03-20 11:45:39形式
print (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# 格式化成Sat Mar 28 22:24:24 2016形式
print (time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))

# 将格式字符串转换为时间戳
a = "Sat Mar 28 22:24:24 2016"
print (time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y")))
'''


def get_date_time():
    '''
    获取时间格式化时间，2020-08-20 08:18:18
    :return: 当前时间
    '''
    from datetime import datetime
    GMT_FORMAT = '%Y-%m-%d %H:%M:%S'
    return time.strftime(GMT_FORMAT, time.localtime())


def get_time_interval(start_timestamp=None, end_timestamp=None):
    '''
    计算两个时间戳的时间间隔，1hour(s) 3minute(s) 10second(s)
    :param start_timestamp: 开始时间戳
    :param end_timestamp: 结束时间戳
    :return:
    '''
    if start_timestamp is None:
        start_timestamp = 0
    if end_timestamp is None:
        end_timestamp = time.time()
    if start_timestamp > end_timestamp:
        return f'start_timestamp[{start_timestamp}] must be less than end_timestamp[{end_timestamp}]'
    if len(str(start_timestamp)) > 10:
        start_timestamp = int(start_timestamp // math.pow(10, len(str(start_timestamp)) - 10))
    if len(str(end_timestamp)) > 10:
        end_timestamp = int(end_timestamp // math.pow(10, len(str(end_timestamp)) - 10))
    seconds_interval = end_timestamp - start_timestamp
    if seconds_interval < 60:
        return str(seconds_interval) + ' second(s)'
    elif seconds_interval > (60 * 60):
        seconds = seconds_interval % 60
        minute_interval = seconds_interval // 60
        minutes = minute_interval % 60
        hours = minute_interval // 60
        return f'{hours} hour(s) {minutes} minute(s) {seconds} second(s)'
    else:
        seconds = seconds_interval % 60
        minute_interval = seconds_interval // 60
        return f'{minute_interval} minute(s) {seconds} second(s)'


'''
python中时间日期格式化符号：

%y 两位数的年份表示（00-99）
%Y 四位数的年份表示（000-9999）
%m 月份（01-12）
%d 月内中的一天（0-31）
%H 24小时制小时数（0-23）
%I 12小时制小时数（01-12）
%M 分钟数（00=59）
%S 秒（00-59）
%a 本地简化星期名称
%A 本地完整星期名称
%b 本地简化的月份名称
%B 本地完整的月份名称
%c 本地相应的日期表示和时间表示
%j 年内的一天（001-366）
%p 本地A.M.或P.M.的等价符
%U 一年中的星期数（00-53）星期天为星期的开始
%w 星期（0-6），星期天为星期的开始
%W 一年中的星期数（00-53）星期一为星期的开始
%x 本地相应的日期表示
%X 本地相应的时间表示
%Z 当前时区的名称
%% %号本身
'''
