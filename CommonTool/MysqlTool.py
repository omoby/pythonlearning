import pymysql


class MysqlUtil():
    '''
    Mysql工具类
    '''

    def __init__(self, db_info):
        self.host = db_info['host']
        self.port = db_info['port']
        self.user = db_info['user']
        self.password = db_info['password']
        self.db = db_info['db']

    def mysql_config(self):
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

    def mysql_connect(self):
        '''
        获取连接句柄和游标
        :return:
        '''
        config = self.mysql_config()
        conn = pymysql.connect(host=config.get('host'),
                               port=config.get('port'),
                               user=config.get('user'),
                               password=config.get('password'),
                               db=config.get('db'),
                               charset='utf8',
                               )
        cursor = conn.cursor()
        return (conn, cursor)

    def insert_data(self, insert_sql, data):
        '''
        插入数据
        :param data:
        :return:
        '''
        conn, cursor = self.mysql_connect()
        try:
            # insert_sql = 'insert into user(user_name,user_age) values(%s,%s)'
            # data = (("user1", 10), ('user1', 12), ("user1", 15))
            affected_rows = cursor.executemany(insert_sql, data)
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
        conn, cursor = self.mysql_connect()
        try:
            # select_sql = 'select * from user'
            affected_rows = cursor.execute(select_sql)
            data = cursor.fetchall()
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
        conn, cursor = self.mysql_connect()

        try:
            # update_sql = 'update user set user_age= %s where user_name= %s'
            # data = (14, 'Tom')
            affected_rows = cursor.execute(update_sql, data)
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
        conn, cursor = self.mysql_connect()
        try:
            # delete_sql = 'delete from user where user_name=%s'
            # data = ('Tom')
            # or
            # delete_sql = 'delete from user'
            # data = None
            affected_rows = cursor.execute(delete_sql, data)
            conn.commit()
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()
        return affected_rows


info = {
    'host': '127.0.0.1',
    'port': 3306,
    'db': '',
    'user': '',
    'password': ''
}

mysql_util = MysqlUtil(info)

# data = (("user1", 10), ('user1', 12), ("user1", 15))

'''
 CREATE TABLE `user` (
  `user_name` varchar(40) DEFAULT NULL,
  `user_age` int(4) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1
'''


# data = (
#     ("Tom", 10), ("Joey", 12), ("Kanmi", 15), ('Tom', 10), ('Joey', 12), ('Kanmi', 15), ('user1', 13), ('user1', 13),
#     ('user1', 13))


def main():
    # mysql_util.insert_data('insert into user(user_name,user_age) values(%s,%s)',data)
    # data = mysql_util.select_data()
    # for sub in data:
    #     print(sub)
    # mysql_util.update_data((13, 'user1'))
    # mysql_util.delete_data('user1')
    # print(mysql_util.select_data('select * from user'))
    # print(mysql_util.update_data('update user set user_age= %s where user_name= %s', (15, 'Tom')))
    # print(mysql_util.select_data('select * from user'))
    print(mysql_util.delete_data('delete from user', None))


if __name__ == '__main__':
    main()
