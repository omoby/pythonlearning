import json
import time
import sys


from download_api import DownloadApiUtil
from detail_util import get_json_data

download_api = DownloadApiUtil()
def main(argv):
    task_id = argv[1]
    task_instance = argv[2]
    data_size = 5
    if len(argv) == 4:
        input_data_size = int(argv[3])
        if input_data_size < 12:
            data_size = input_data_size
        else:
            data_size = 12
    index = 0
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
    main(sys.argv)