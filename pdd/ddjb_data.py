from pdd.agent_util import AgentPoolUtil
from pdd.date_util import get_timestamp
from pdd.mt_download_api import DownloadApiUtil


agent_pool_util = AgentPoolUtil()
def get_one_mall_data(url):
    import requests
    mall_id = url.split('?')[1].split('=')[1]
    url = "https://jinbao.pinduoduo.com/network/api/merchant/queryAllGoodsByMallId"

    querystring = {"mallId": mall_id, "pageNumber": "1", "pageSize": "100"}

    headers = {
        'pragma': "no-cache",
        'cookie': "_nano_fp=XpdbX0X8XpCqn5djl9_b_Bywp_CajUUhEuw6LCea; api_uid=rBUUYF7LJf2AL1tP9awcAg==; DDJB_PASS_ID=171536280ca22da9c6ea3f0d835e0bb3",
        'accept-encoding': "gzip, deflate, br",
        'accept-language': "zh-CN,zh;q=0.9",
        'user-agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36",
        'accept': "application/json, text/plain, */*",
        'cache-control': "no-cache,no-cache",
        'authority': "jinbao.pinduoduo.com",
        'referer': "https://jinbao.pinduoduo.com/promotion/store-promotion?keyword=890164712",
        'Postman-Token': "9d7e0ad1-6057-4b8c-8700-b170f91a8ae0"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    print(response.json())


'''
构造需要向download api提交的数据
'''
def get_json_data(data):
    json_data = data
    result_total = json_data.get('result').get('total')
    result_data = json_data.get('result').get('data')
    prev_data = []
    fail_url = []
    success_url = []
    fail_counter = 0
    for sub in result_data:

        content = get_one_mall_data(sub.get('url'))

        if 'not_exist' == content:
            fail_url.append((get_timestamp(),sub.get('url')))
            fail_counter += 1
            print('not_exist_counter=%d' % (fail_counter))
            if fail_counter % 3 == 0:
                global g_cookie
                g_cookie =  agent_pool_util.get_cookie()
                print('切换Cooki成功！')
        else:
            data = {
              "attemptCount": sub.get('attemptCount'),
              "content": content,
              "currentDepth": sub.get('currentDepth'),
              "downloadTime": get_timestamp(),
              "downloadTool": sub.get('downloadTool'),
              "failureCount": sub.get('failureCount'),
              "httpMethodName": sub.get('httpMethodName'),
              "httpStatus": 200,
              "markId": sub.get('markId'),
              "maxDepth": sub.get('maxDepth'),
              "other": {
                "additionalProp1": "string",
                "additionalProp2": "string",
                "additionalProp3": "string"
              },
              "parentTraceId": sub.get('parentTraceId'),
              "publishTime": sub.get('publishTime') if sub.get('publishTime') is not None else 0,
              "publisherId": sub.get('publisherId'),
              "purl": "0000",
              "responseHeaders": {
                  "X-API-TOKEN":'aaaa',
                  "connection":'Keep-Alive',
                  "user-agent": "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1;SV1)",
                  "Content-Type": "application/json"
              },
              "ruleId": sub.get('ruleId'),
              "taskId": sub.get('taskId'),
              "taskInstanceId": sub.get('taskInstanceId'),
              "traceId": sub.get('traceId'),
              "url": sub.get('url'),
              "urlType": sub.get('urlType')
            }
            prev_data.append(data)
            success_url.append((get_timestamp(),sub.get('url')))

    result_total = result_total - fail_counter

    if result_total == 0:
        return (success_url,result_total)
    else:
        return_data = {
            "data": prev_data,
            "total": result_total
        }
        # print(json.dumps(return_data))
        return (success_url,return_data)

api_util = DownloadApiUtil()


def main():
    task_id = '12361'
    task_instance = 'a7007725-9770-4a4d-bafd-d3c133c452a0'
    data_size = 3
    data = api_util.get_url(task_id,task_instance,data_size)
    print(data)

    # get_one_mall_data()
if __name__ == '__main__':
    main()