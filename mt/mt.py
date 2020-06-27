import random
import urllib


import cx_Oracle
import requests

from DPCrawler.config import PROXY_POOL
from DPCrawler.setting import USER_AGENTS

user = 'crawlm'
passwd = 'crawlm_Sd'
database = 'dcappdb'
host = '172.22.5.61'
port = '1526'
conn_info = user+"/"+passwd+"@"+host+":"+port+"/"+database
def get_agent_proxies():
    user_agent = random.choice(USER_AGENTS)
    proxy_ip = urllib.request.urlopen(PROXY_POOL).read().decode("utf-8").split("\n")[1]
    # print(proxy_ip)
    proxy = {'https': proxy_ip, 'http': proxy_ip}
    return (user_agent,proxy)

#python连接Oracle数据库的工具类
class OracleUtil():
    """
    获取省份id的list
    """
    def get_url(self):
        conn = cx_Oracle.connect(conn_info)
        # 获取cursor光标
        cursor = conn.cursor()
        # 数据库操作
        # 1.查询
        sql = "select distinct TASK_URL from o1255_task_url_202004 where rownum < 100000"

        result = cursor.execute(sql)
        data = result.fetchall()
        cursor.close()
        conn.close()

        return data


connection = OracleUtil()

def get_shop_info(url):

    user_agent,proxies = get_agent_proxies()
    # print(user_agent,proxies)
    headers = {
        'Host': 'i.meituan.com',
        'User-Agent': user_agent,
    }
    response = requests.get(url,headers=headers)
    status_code = response.status_code
    # print(status_code)
    return status_code

def main():
    data = connection.get_url()
    total = len(data)
    success = 0
    fail = 0
    for url_tuple in data:
        url = url_tuple[0]
        # print(url)
        status_code = get_shop_info(url)
        # print(status_code)
        if status_code == 200:
            success +=1
        else:
            fail += 1
    success_rate = float(success) / total
    fail_rate = float(fail) / total
    print(success)
    print(fail)
    print('total=%d,sucess_rate=%.2f,fail_reate=%.2f'%(total,success_rate,fail_rate))
if __name__ == '__main__':
    main()
    # get_agent_proxies()