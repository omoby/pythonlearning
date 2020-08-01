import pymysql


class MysqlUtil():
    '''
    Mysql工具类
    '''

    def mysql_config(self):
        """
        mysql config
        :return:
        """
        infor = {
            "host": "127.0.0.1",
            "port": 3306,
            "user": "root",
            "password": "root",
            "db": "testdb",
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
                               # charset='utf8',
                               )
        cursor = conn.cursor()
        return (conn, cursor)

    def insert_data(self, data):
        '''
        插入数据
        :param data:
        :return:
        '''
        conn, cursor = self.mysql_connect()
        # print(data)
        try:
            insert_sql = 'insert into user(user_name,user_age) values(%s,%s)'
            # print(insert_sql)
            affected_rows = cursor.executemany(insert_sql, data)
            conn.commit()
            print(f'成功插入[{affected_rows}]条数据！')
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()

    def select_data(self):
        '''
        查询数据
        :return:
        '''
        conn, cursor = self.mysql_connect()
        try:
            select_sql = 'select user_name, user_age from  user'
            get_rows = cursor.execute(select_sql)
            data = cursor.fetchall()
            print(f'查询到[{get_rows}]条数据！')
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()
        return data

    def update_data(self, data):
        '''
        更新数据
        :param data:
        :return:
        '''
        conn, cursor = self.mysql_connect()

        try:
            update_sql = 'update user set user_age= %s where user_name= %s'
            affected_rows = cursor.execute(update_sql, data)
            conn.commit()
            print(f'更新了[{affected_rows}]条数据！')
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()

    def delete_data(self, data):
        '''
        删除数据
        :param data:
        :return:
        '''
        conn, cursor = self.mysql_connect()
        try:
            delete_sql = 'delete from user where user_name=%s'
            affected_rows = cursor.execute(delete_sql, data)
            conn.commit()
            print(f'删除[{affected_rows}]条数据成功！')
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()


mysql_util = MysqlUtil()
data = (("user1", 10), ('user1', 12), ("user1", 15))

'''
 CREATE TABLE `user` (
  `user_name` varchar(40) DEFAULT NULL,
  `user_age` int(4) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1
'''


def main():
    # mysql_util.insert_data(data)
    # data = mysql_util.select_data()
    # for sub in data:
    #     print(sub)
    mysql_util.update_data((13, 'user1'))
    # mysql_util.delete_data('user1')


if __name__ == '__main__':
    main()
