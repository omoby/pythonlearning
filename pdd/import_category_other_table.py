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
    获取所有店铺的信息
    """
    def get_mall_info_202004(self):
        conn = cx_Oracle.connect(conn_info)
        #获取cursor游标
        cursor=conn.cursor()
        #数据库操作
        #1.查询
        query_sql='SELECT DISTINCT SHOP_ID,SHOP_NAME from o6001_pl_202004 o4 ' \
                  'WHERE o4.SHOP_ID NOT IN (SELECT DISTINCT TASK_URL FROM PDD_MALL_ALL PMA)'
        result=cursor.execute(query_sql)
        mall_data = result.fetchall()
        #1.插入操作
        cursor.close()
        conn.close()
        return mall_data

    def get_mall_info_202003(self):
        conn = cx_Oracle.connect(conn_info)
        # 获取cursor游标
        cursor = conn.cursor()
        # 数据库操作
        # 1.查询
        query_sql = 'SELECT DISTINCT SHOP_ID,SHOP_NAME from o6001_pl_202003'
        result = cursor.execute(query_sql)
        mall_data = result.fetchall()
        # 1.插入操作
        cursor.close()
        conn.close()
        return mall_data

    def get_mall_info_pdd_mall(self):
        conn = cx_Oracle.connect(conn_info)
        # 获取cursor游标
        cursor = conn.cursor()
        # 数据库操作
        # 1.查询
        query_sql = 'SELECT DISTINCT MALL_ID,MALL_NAME from PDD_MALL PM ' \
                    'WHERE PM.MALL_ID NOT IN (SELECT DISTINCT MALL_ID FROM PDD_MALL_ALL PMA)'
        result = cursor.execute(query_sql)
        mall_data = result.fetchall()
        # 1.插入操作
        cursor.close()
        conn.close()
        return mall_data

    def get_mall_pdd_mall_all(self):
        conn = cx_Oracle.connect(conn_info)
        # 获取cursor游标
        cursor = conn.cursor()
        # 数据库操作
        # 1.查询
        query_sql = 'SELECT DISTINCT TASK_URL,MALL_NAME from PDD_MALL_ALL PMA ' \
                    'WHERE ROWNUM < 100'
        result = cursor.execute(query_sql)
        mall_data = result.fetchall()
        # 1.插入操作
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
        inser_sql = 'INSERT INTO PDD_MALL_ALL(TASK_URL,MALL_NAME) VALUES (:TASK_URL,:MALL_NAME)'

        try:
            cursor.executemany(inser_sql, data)
            cursor.execute('commit')
            conn.commit()
        except cx_Oracle.IntegrityError as e:
            print('cx_Oracle.IntegrityError')
        cursor.close()
        conn.close()

    def insert_mall_task_url(self, data):
        conn = cx_Oracle.connect(conn_info)
        # 获取cursor光标
        cursor = conn.cursor()
        # 数据库操作
        inser_sql = 'INSERT INTO PDD_MALL_TASK(TASK_URL,MALL_NAME) VALUES (:TASK_URL,:MALL_NAME)'

        try:
            cursor.executemany(inser_sql, data)
            cursor.execute('commit')
            conn.commit()
        except cx_Oracle.IntegrityError as e:
            print('cx_Oracle.IntegrityError')
        cursor.close()
        conn.close()
    '''
    获取店铺分类
    '''
    def delete_mall(self,data):
        conn = cx_Oracle.connect(conn_info)
        # 获取cursor游标
        cursor = conn.cursor()
        # 数据库操作
        # 1.查询
        query_sql = 'DELETE FROM PDD_MALL_ALL WHERE TASK_URL='+data
        result = cursor.execute(query_sql)
        # 1.插入操作
        cursor.close()
        conn.close()


oracle = OracleUtil()


def get_import_202003():
    mall_data = oracle.get_mall_info_202003()
    insert_data = []
    insert_trigger = 0
    for data in mall_data:
        mall_id = data[0]
        mall_name = data[1]
        insert_data.append((mall_id,mall_name))
        insert_trigger += 1
        if (insert_trigger % 100) == 0:
            oracle.insert_mall_info(insert_data)
            insert_data = []
            print(f'第[ {insert_trigger // 100} ]次导入数据，已经导入[ {insert_trigger} ]')
    if len(insert_data) != 0:
        oracle.insert_mall_info(insert_data)
        print(f'最后一次导入数据，已经导入[ {insert_trigger} ]')
    print('o6001_pl_202003表店铺数据导入完毕')


def get_import_202004():
    mall_data = oracle.get_mall_info_202004()
    print(len(mall_data))
    # mall_id_set = []
    insert_data = []
    insert_trigger = 0
    for data in mall_data:
        mall_id = data[0]
        mall_name = data[1]
        insert_data.append((mall_id, mall_name))
        insert_trigger += 1
        if insert_trigger % 100 == 0:
            oracle.insert_mall_info(insert_data)
            print(f'第[ {insert_trigger // 100} ]次导入数据，已经导入[ {insert_trigger} ]')
            insert_data = []
    if len(insert_data) != 0:
        oracle.insert_mall_info(insert_data)
        print(f'最后一次导入数据，已经导入[ {insert_trigger} ]')
    print('o6001_pl_202004表店铺数据导入完毕')

def get_import_pdd_mall():
    mall_data = oracle.get_mall_info_pdd_mall()
    print(len(mall_data))
def get_import_mall_task():
    prev_url = 'https://jinbao.pinduoduo.com/network/api/merchant/queryAllGoodsByMallId?mallId='
    mall_data = oracle.get_mall_pdd_mall_all()
    print(len(mall_data))
    insert_data = []
    for sub in mall_data:
        task_url = prev_url+str(sub[0])
        mall_name = sub[1]
        insert_data.append((task_url,mall_name))
    oracle.insert_mall_task_url(insert_data)

def main():
    # get_import_202003()
    # get_import_202004()
    # get_import_pdd_mall()
    get_import_mall_task()
if __name__ == '__main__':
    main()