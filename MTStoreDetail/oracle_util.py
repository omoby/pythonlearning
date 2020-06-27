import cx_Oracle

user = 'crawlm'
passwd = 'crawlm_Sd'
database = 'dcappdb'
host = '172.22.5.61'
port = '1526'
conn_info = user+"/"+passwd+"@"+host+":"+port+"/"+database

'''
python连接Oracle数据库的工具类
'''
class OracleUtil():
    """
    保存采集失败店铺的url
    """
    def mark_not_exit_url(self,data):
        conn = cx_Oracle.connect(conn_info)
        cursor = conn.cursor()
        inser_sql = 'insert into MT_PAGE_NOT_EXIST_URL values(:ROW_KEY,:TASK_URL)'
        try:
            cursor.executemany(inser_sql, data)
            cursor.execute('commit')
            conn.commit()
            print('保存采集失败连接成功！')
        except cx_Oracle.IntegrityError as e:
            print(e)
        except cx_Oracle.DatabaseError as e:
            print(e)
        cursor.close()
        conn.close()


