import json
import time
import sys

from TheCustomsOfPeru.detail_util  import get_json_data
from TheCustomsOfPeru.download_api import DownloadApiUtil

download_api = DownloadApiUtil()
def main():

    task_id = "12902"
    task_instance = "01faf68f-999c-4caa-b81b-4216c4728e92"
    index = 0
    data_size = 9
    while True:
        start = int(time.time())
        print(f'-----本次采集开始时间：{start}------')
        print("第[ %d ]次请求数据,请求[ %d ]条数据" % ((index + 1), data_size))
        data = download_api.get_url(task_id, task_instance, data_size)
        # print(data)
        code = data.get('code')
        if code == 10002 or code == 10003:
            print(data.get("msg"))
        else:
            success_url, body = get_json_data(data)
            # print(body)
            if body == 0:
                pass
            else:

                status = download_api.post_result(json.dumps(body))
                if status != 201:
                    print('上传失败[ %d ]条数据' % (body.get("total")))
                else:
                    print('上传成功[ %d ]条数据' % (body.get("total")))
        index += 1
        end = int(time.time())
        print(f'------本次采集结束时间：{end}------')
        print(f"++++++耗时{end - start}s+++++++")
        print('')

if __name__ == '__main__':
    main()