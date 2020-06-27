

from importlib import reload
import  cx_Oracle
from urllib import request
from urllib.parse import quote



user = 'crawlm'
passwd = 'crawlm_Sd'
database = 'dcappdb'
host = '172.22.5.61'
port = '1526'
conn_info = user+"/"+passwd+"@"+host+":"+port+"/"+database

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
        sql = "select distinct TASK_URL from o1255_task_url_202004 where rownum < 10"

        result = cursor.execute(sql)
        data = result.fetchall()
        cursor.close()
        conn.close()
        return data



if __name__=='__main__':
    connection = OracleUtil()
    data = connection.get_url()
    for url_tuple in data:
        url = url_tuple[0]
        print(url)
