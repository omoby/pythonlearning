import cx_Oracle


class OracleUtil():
    '''
    python连接Oracle数据库的工具类
    '''

    def __init__(self, db_info):
        self.host = db_info['host']
        self.port = db_info['port']
        self.user = db_info['user']
        self.password = db_info['password']
        self.db = db_info['db']

    def oracle_config(self):
        """
        mysql config
        :return:
        """
        infor = {
            "host": self.host,
            "port": self.port,
            "db": self.db,
            "user": self.user,
            "password": self.password,

        }
        return infor

    def oracle_connect(self):
        '''
        获取连接句柄和游标
        :return:
        '''
        config = self.oracle_config()
        conn_info = config['user'] + "/" + config['password'] + "@" + config['host'] + ":" + config['port'] + "/" + \
                    config['db']
        conn = cx_Oracle.connect(conn_info)
        cursor = conn.cursor()
        return (conn, cursor)

    def insert_data(self, insert_sql, data):
        '''
        插入数据
        :param data:
        :return:
        '''
        conn, cursor = self.oracle_connect()
        try:
            # insert_sql = 'insert into test_py(name,age) values(:NAME,:AGE)'
            # data = [('3', '33'), ('3', '44')]
            cursor.executemany(insert_sql, data)
            affected_rows = cursor.rowcount
            conn.commit()
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()
        return affected_rows

    def select_data(self, select_sql):
        '''
        查询数据
        :return:
        '''
        conn, cursor = self.oracle_connect()
        try:
            cursor.execute(select_sql)
            data = cursor.fetchall()
            conn.commit()
            affected_rows = len(data)
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()
        return (affected_rows, data)

    def update_data(self, update_sql, data):
        '''
        更新数据
        :param data:
        :return:
        '''
        conn, cursor = self.oracle_connect()
        try:
            # update_sql = 'update test_py set name= :1 where age=:2'
            cursor.execute(update_sql, data)
            affected_rows = cursor.rowcount
            conn.commit()
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()
        return affected_rows

    def delete_data(self, delete_sql, data):
        '''
        删除数据
        :param data:
        :return:
        '''
        conn, cursor = self.oracle_connect()
        try:
            # delete_sql = 'delete from test_py where name= :1'
            # data = ('3',)
            cursor.execute(delete_sql, data)
            affected_rows = cursor.rowcount
            conn.commit()
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()
        return affected_rows


db_info = {
    'user': '',
    'password': '',
    'db': '',
    'host': '',
    'port': ''
}
oralce = OracleUtil(db_info)


def main():
    # select_sql = 'select * from test_py'
    # affected_rows, data = oralce.select_data(select_sql)
    # print(affected_rows)
    # print(data)
    # update_sql = 'update test_py set name= :1 where age=:2'
    # update_data = ('4', '33')
    # print(oralce.select_data('select * from test_py'))
    # print(oralce.update_data(update_sql, update_data))
    # print(oralce.select_data('select * from test_py'))

    # insert_sql = 'insert into test_py(name,age) values(:NAME,:AGE)'
    # data = [('3', '33'), ('3', '44')]
    # print(oralce.select_data('select * from test_py'))
    # print(oralce.insert_data(insert_sql, data))
    # print(oralce.select_data('select * from test_py'))
    delete_sql = 'delete from test_py where name= :1'
    delete_data = ('3',)
    print(oralce.select_data('select * from test_py'))
    print(oralce.delete_data(delete_sql, delete_data))
    print(oralce.select_data('select * from test_py'))


if __name__ == '__main__':
    main()
