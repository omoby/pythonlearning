import json
import time
import sys

from MTStoreDetail.crawl_util import get_json_data
from MTStoreDetail.mt_download_api import DownloadApiUtil
from MTStoreDetail.oracle_util import OracleUtil

download_api = DownloadApiUtil()
connection = OracleUtil()
def main():

    task_id = "1261"
    task_instance = "fd302c3d-468c-4494-9e70-5b0628e80366"
    index = 0
    data_size = 3
    while True:
        print("第[ %d ]次请求数据,每次请求[ %d ]条数据" % ((index+1),data_size))
        # time.sleep(1)
        data = download_api.get_url(task_id,task_instance,data_size)
        # print(data)
        code = data.get('code')
        if code == 10002 or code == 10003:
            print(data.get("msg"))
        else:
            success_url,body = get_json_data(data)
            # print(body)
            if body == 0:
                pass
            else:

                status = download_api.post_result(json.dumps(body))
                if status != 201:
                   connection.mark_not_exit_url(success_url)
                   print('上传失败[ %d ]条数据' %(body.get("total")))
                else:
                    print('上传成功[ %d ]条数据' % (body.get("total")))
        index += 1
        print("")

if __name__ == '__main__':
    main()