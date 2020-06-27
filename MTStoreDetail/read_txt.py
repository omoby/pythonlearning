import random
import uuid

from date_util import get_timestamp
from oracle_util import OracleUtil
conn = OracleUtil()

def get_txt_data():
    with open("test.txt","r") as f:
        # 为a+模式时，因为为追加模式，指针已经移到文尾，读出来的是一个空字符串。
        # ftext = f.read()  # 一次性读全部成一个字符串
        ftextlist = f.readlines() # 也是一次性读全部，但每一行作为一个子句存入一个列表
        return ftextlist
def get_cookie():
    cookie_pool = conn.get_cookie(0)
    cookie = random.choice(cookie_pool)
    c_id = cookie[0]
    c_value = cookie[1]
    print(type(cookie))
    print(c_id,c_value)
    # for sub_list in data:
        # print(type(sub_list))
        # print(sub_list)
    # print(type(data))
def update_cookie():
    data = '4da4ce14-5c18-4385-a243-23c71e70c98d'
    # update_sql = 'update MT_COOKIE set C_TIME={} where C_ID="{}"'.format(get_timestamp(), data)
    conn.update_cookie_time(data)
    # print(update_sql)
def insert_cookie():
    data = get_txt_data()
    insert_data = []
    index = 0
    for sub in data:
        c_id = str(uuid.uuid4())
        c_value = sub.strip()
        c_time = get_timestamp()
        insert_data.append((c_id, c_value, c_time))
        index += 1
        if index % 10 == 0:
            conn.insert_cookie(insert_data)
            insert_data = []
    if len(insert_data) > 0:
        conn.insert_cookie(insert_data)


def main():
    get_cookie()
    # update_cookie()
if __name__ == '__main__':
    main()