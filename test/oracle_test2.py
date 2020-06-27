#OracleHelper.py
import cx_Oracle as oracle
from tutorial.poHelper import dbconfig
#import os
# 增加环境变量,配合读取配置信息访问oracle
#os.environ['NLS_LANG'] = dbconfig.NLS_LANG
#os.environ['path'] = dbconfig.ORACLE_PATH  #这个路径看况填写

class OracleHelper():
    def __init__(self):
        self.dsn_tns = oracle.makedsn(dbconfig.ORACLE_HOST, dbconfig.ORACLE_PORT,
                             dbconfig.ORACLE_SID)
    def getConnect(self):
        # 建立连接
        self.connect = oracle.connect(user=dbconfig.ORACLE_USER, password=dbconfig.ORACLE_PASSWORD, dsn=self.dsn_tns,threaded=True,events = True)
        return self.connect

_oracleManager = OracleHelper()

#获取连接
def getConn():
    """ 获取数据库连接 """
    return _oracleManager.getConnect()

#查询所有
def fetchall(sql,param=[]):
    return _execute_query_by_sql_param(sql,param=param)

#查询一条记录
def fetchone(sql,param=[]):
    sql = get_complete_sql(sql, param)
    sql = "select * from ( %s ) where rownum = 1" % sql
    result = _execute_query_by_sql_param(sql=sql)
    return result

#增加
def insert(sql,param=[]):
    sql = get_complete_sql(sql, param)
    result = _execute_commit(sql)
    return result

#修改
def update(sql,param=[]):
    sql = get_complete_sql(sql, param)
    result = _execute_commit(sql)
    return result

#插入两条记录
def insertTwo(sql1, sql2, param1, param2):
    result1 = insert(sql1,param1)
    result2 = insert(sql2,param2)
    result = result1 + result2
    return result

#删除
def delete(sql, param):
    sql = get_complete_sql(sql, param)
    result = _execute_commit(sql)
    return result

#执行多个sql修改
def executemany(sql,params):
    count = 0
    for item in params:
        result = update(sql=sql,param=item)
        count += result
    return count


#执行带参查询
def _execute_query_by_sql_param(sql,param=[]):
    sql = get_complete_sql(sql, param)
    result = _execute_query_oracle_sql(sql=sql)
    return result

def _execute_commit(sql):
    result = 0
    try:
        # 获取链接
        connect = getConn()
        # 获取游标
        cursor = connect.cursor()
        # 执行修改
        cursor.execute(sql)
        #返回结果
        result = cursor.rowcount
        # 提交数据
        connect.commit()
    except Exception as e:
        print(e)
    finally:
        close_oracle(cursor, connect)
    return result

#执行不带参查询
def _execute_query_oracle_sql(sql):
    result = []
    try:
        #获取链接
        connect = getConn()
        #获取游标
        cursor = connect.cursor()
        #执行查询
        cursor.execute(sql)
        #获取数据 ，可以有多种方式 fetchall()，fetchmang(N)(N 为正整数),fetchone()
        result = cursor.fetchall()
        # count = cursor.rowcount
        # print("Total:", count)
    except Exception as e:
        print(e)
    finally:
        close_oracle(cursor,connect)
    return result

#关闭链接
def close_oracle(cursor,connect):
    try:
        if cursor != None:
            cursor.close()
        if connect != None:
            connect.close()
    except Exception as  e:
        print(e)

#改变参数方法
def chang_list_param_to_tuple(param=[]):
    param_list = []
    for item in param:
        param_list.append("'%s'" % item)
    return tuple(param_list)

#获得拼接好的sql
def get_complete_sql(sql,param=[]):
    param = chang_list_param_to_tuple(param=param)
    sql = sql % param
    print(sql)
    return sql


if __name__ == '__main__':
    # sql = "select * from vc_user where instr(real_name,%s)>0"
    # param = ["张"]
    sql = "update po_monitor_lexicon set BINARY_SYSTEM = :1 ,IS_CRAWLED='N' where monitor_key = '金蝶办公'"
    param = [['0'],['2'],['3']]
    # result = _execute_many(sql,param)
    # result = fetchall(sql,param)
    # print(result)
    # result = fetchone(sql,param)
    # print(result)