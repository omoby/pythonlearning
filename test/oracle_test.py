

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
    def get_province_id(self):
        conn = cx_Oracle.connect(conn_info)
        #获取cursor游标
        cursor=conn.cursor()
        #数据库操作
        #1.查询
        sql='select distinct province_id from dianping_province where province_id > 14 order by province_id'
        result=cursor.execute(sql)
        data = result.fetchall()
        province_id_list = []
        for i in data:    #循环遍历，查询得到的结果集
            # print(i)
            province_id_list.append(i[0])
        #1.插入操作
        cursor.close()
        conn.close()
        return province_id_list

    """
    获取城市id的list
    """
    def get_city_info(self,province_id):
        conn = cx_Oracle.connect(conn_info)
        # 获取cursor光标
        cursor = conn.cursor()
        # 数据库操作
        # 1.查询
        sql = "select distinct city_id, city_en_name from dianping_city where province_id="+str(province_id)

        result = cursor.execute(sql)
        data = result.fetchall()
        city_id_list = []
        for i in data:  # 循环遍历，查询得到的结果集
            city_id_list.append(i)
        # 1.插入操作
        cursor.close()
        conn.close()
        return city_id_list
    """
    获取城市的分区id的list
    """
    def get_region_id(self,city_id):
        conn = cx_Oracle.connect(conn_info)
        # 获取cursor光标
        cursor = conn.cursor()
        # 数据库操作
        # 1.查询
        sql = "select distinct region_id from dianping_region where city_id=" + str(city_id)

        result = cursor.execute(sql)
        data = result.fetchall()
        region_id_list = []
        for i in data:  # 循环遍历，查询得到的结果集
            region_id_list.append(i[0])
        # 1.插入操作
        cursor.close()
        conn.close()
        return region_id_list
    def get_crawed_region_id(self):
        conn = cx_Oracle.connect(conn_info)
        # 获取cursor光标
        cursor = conn.cursor()
        # 数据库操作
        # 1.查询
        sql = "select distinct region_id from dianping_record"

        result = cursor.execute(sql)
        data = result.fetchall()
        region_id_list = []
        for i in data:  # 循环遍历，查询得到的结果集
            region_id_list.append(i[0])
        # 1.插入操作
        cursor.close()
        conn.close()
        return region_id_list

    def get_main_category_id(self):
        conn = cx_Oracle.connect(conn_info)
        # 获取cursor光标
        cursor = conn.cursor()
        # 数据库操作
        # 1.查询
        sql = "select distinct main_category_id from dianping_main_category "

        result = cursor.execute(sql)
        data = result.fetchall()
        main_category_id_list = []
        for i in data:  # 循环遍历，查询得到的结果集
            main_category_id_list.append(i[0])
        # 1.插入操作
        cursor.close()
        conn.close()
        return main_category_id_list

    def get_main_category(self):
        conn = cx_Oracle.connect(conn_info)
        # 获取cursor光标
        cursor = conn.cursor()
        # 数据库操作
        # 1.查询
        sql = "select * from dianping_main_category where rownum < 10"

        result = cursor.execute(sql)
        data = result.fetchall()
        # main_category_id_list = []
        # for i in data:  # 循环遍历，查询得到的结果集
            # main_category_id_list.append(i[0])
        # 1.插入操作
        cursor.close()
        conn.close()
        return data

    def get_sub_category_id(self):
        conn = cx_Oracle.connect(conn_info)
        # 获取cursor光标
        cursor = conn.cursor()
        # 数据库操作
        # 1.查询
        sql = "select distinct sub_category_id from dianping_sub_category "

        result = cursor.execute(sql)
        data = result.fetchall()
        sub_category_id_list = []
        for i in data:  # 循环遍历，查询得到的结果集
            sub_category_id_list.append(i[0])
        # 1.插入操作
        cursor.close()
        conn.close()
        return sub_category_id_list

    """
    插入商店的大类
    """
    def insert_main_category(self,data):
        conn = cx_Oracle.connect(conn_info)
        # 获取cursor光标
        cursor = conn.cursor()
        # 数据库操作
        # 1.查询
        param=[]
        for sub in data:
            param.append((sub.category_id, sub.category_name.encode('utf-8')))
        print(param)
        inser_sql = 'insert into dianping_main_category values(:main_category_id,:main_category_name)'

        try:
            cursor.executemany(inser_sql, param)
        except cx_Oracle.IntegrityError as e:
            pass
        cursor.execute('commit')
        conn.commit()
        cursor.close()
        conn.close()
    """
    获取店铺分类的种类id的list
    """
    def insert_sub_category(self, data):
        conn = cx_Oracle.connect(conn_info)
        # 获取cursor光标
        cursor = conn.cursor()
        # 数据库操作
        # 1.查询
        param = []
        for sub in data:
            param.append((sub.sub_category_id,sub.main_category_id,sub.sub_category_name.encode('utf-8')))
        print(param)
        inser_sql = 'insert into dianping_sub_category values(:sub_category_id,:main_category_id,:sub_category_name)'
        try:
            cursor.executemany(inser_sql, param)
        except cx_Oracle.IntegrityError as e:
            pass
        cursor.execute('commit')
        conn.commit()
        cursor.close()
        conn.close()

    """
    插入采集数据记录
    """
    def insert_record(self, data):
        conn = cx_Oracle.connect(conn_info)
        # 获取cursor光标
        cursor = conn.cursor()
        # 数据库操作
        # 1.查询
        param = []
        for sub in data:
            param.append((sub.row_key,sub.region_id,sub.sub_category_id,sub.record_num))
        print(param)
        inser_sql = 'insert into dianping_record values(:row_key,:region_id,:sub_category_id,:record_num)'
        try:
            cursor.executemany(inser_sql, param)
        except cx_Oracle.IntegrityError as e:
            pass
        cursor.execute('commit')
        conn.commit()
        cursor.close()
        conn.close()



if __name__=='__main__':
    connection = OracleUtil()
    list = connection.get_province_id()
    main_category_list = connection.get_main_category_id()
    crowed_region_list =connection.get_crawed_region_id()
    print(main_category_list)
    print(crowed_region_list)
    index = 0
    while index < 1:
        province_id = list[index]
        index += 1
        print(province_id)
        city_list = connection.get_city_info(province_id)
        city_len = len(city_list)
        print(city_len)
        city_list.sort()
        for city in city_list:
            print(city)
