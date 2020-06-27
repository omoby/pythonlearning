import cx_Oracle

user = 'crawlm'
passwd = 'crawlm_Sd'
database = 'dcappdb'
host = '172.22.5.61'
port = '1526'
conn_info = user+"/"+passwd+"@"+host+":"+port+"/"+database

"""
python连接Oracle数据库的工具类
"""
class OracleUtil():
    """
    获取省份id的list
    """
    def get_mall_info(self,data):
        conn = cx_Oracle.connect(conn_info)
        #获取cursor游标
        cursor=conn.cursor()
        #数据库操作
        #1.查询
        query_sql='SELECT DISTINCT MALL_ID,MALL_NAME,MERCHANT_TYPE FROM  PDD_MALL WHERE MALL_ID=:1'
        result=cursor.execute(query_sql,data)
        mall_data = result.fetchall()
        #1.插入操作
        cursor.close()
        conn.close()
        return mall_data


    """
    插入店铺信息
    """
    def insert_mall_info(self,data):
        conn = cx_Oracle.connect(conn_info)
        # 获取cursor光标
        cursor = conn.cursor()
        # 数据库操作
        inser_sql = 'INSERT INTO PDD_MALL VALUES (:MALL_ID,:MALL_NAME,:MERCHANT_TYPE)'

        try:
            cursor.executemany(inser_sql, data)
            cursor.execute('commit')
            conn.commit()
        except cx_Oracle.IntegrityError as e:
            print('cx_Oracle.IntegrityError')
        cursor.close()
        conn.close()


