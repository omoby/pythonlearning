import json
import http.client

from date_util import get_date, get_timestamp
from encrypt_util import get_secret

user = "inspur"

'''
使用download api工具类
'''
class DownloadApiUtil():
    '''
    使用download api获取需要采集的任务链接
    '''
    def get_url(self,task_id,task_intance,data_size):

        date = get_date()
        aut = 'hmac username="'+user+'", algorithm="hmac-sha256", headers="date", signature="'+get_secret(date)+'"'
        headers  ={
            'Date': date,
            'Authorization': aut,
            'X-API-TOKEN': 'sadb',
            'connection': 'Keep-Alive',
            'Accept': 'application/json',
            'user-agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1;SV1)'
        }
        # 与服务器建立链接
        server_url = '172.22.5.243:30080'
        conn = http.client.HTTPConnection(server_url)
        # 向服务器发送请求
        method = "GET"
        request_url = "http://172.22.5.243:30080/download-api/v1/requests/"+task_id+"/"+task_intance+"?user=" + user+"&size="+str(data_size)+"&ts=" + str(get_timestamp())
        # print(url)
        conn.request(method=method, url=request_url, headers=headers)
        # 获取响应消息体
        response = conn.getresponse()
        data = response.read()
        return (json.loads(data.decode("utf8")))

    '''
    使用download api将采集的数据上传到采集任务
    '''
    def  post_result(self,body):
        date = get_date()

        aut = 'hmac username="' + user + '", algorithm="hmac-sha256", headers="date", signature="' + get_secret(date) + '"'
        headers = {
            'Date': date,
            'Authorization': aut,
            'X-API-TOKEN': 'sadb',
            'connection': 'Keep-Alive',
            'Content-Type': 'application/json',
            'Accept':'application/json',
            'user-agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1;SV1)'
        }
        # 与服务器建立链接
        server_url = '172.22.5.243:30080'
        conn = http.client.HTTPConnection(server_url)
        # 向服务器发送请求
        method = "POST"
        post_url = 'http://172.22.5.243:30080/download-api/v1/results?ts='+str(get_timestamp())+"&user="+user
        # print(url)
        conn.request(method=method, url=post_url, body=body, headers=headers)
        # 获取响应消息体
        response = conn.getresponse()
        status = response.status
        data = response.read()
        # print(data.decode("utf8"))
        return status

