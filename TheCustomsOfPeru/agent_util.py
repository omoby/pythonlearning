import json
import random
import time
import urllib.request

from TheCustomsOfPeru.agent_pool import PROXY_POOL, USER_AGENTS

'''
代理池工具类
'''


class AgentPoolUtil():
    '''
    从IP代理池获取一个代理IP
    '''

    def get_high_proxy(self):
        proxy_pool_url = 'http://api.xdaili.cn/xdaili-api//newExclusive/getIp?spiderId=f25a98602abb42bf9c03e2ba59e7904b&orderno=DX20181184472xR7vEN&returnType=2&count=1&machineArea='
        proxy_ip = urllib.request.urlopen(proxy_pool_url).read()
        # print(proxy_ip.decode('utf-8'))
        proxy_ip = json.loads(proxy_ip)
        while proxy_ip['ERRORCODE'] != '0':
            time.sleep(15)
            proxy_ip = urllib.request.urlopen(proxy_pool_url).read()
            # print(proxy_ip.decode('utf-8'))
            proxy_ip = json.loads(proxy_ip)
        result = proxy_ip.get('RESULT')[0]
        # print(type(result))
        # print(result)
        port = result.get('port')
        ip = result.get('ip')
        proxy_ip = ip + ":" + port
        proxy = {'https': proxy_ip, 'http': proxy_ip}
        return proxy
    def get_proxy(self):
        proxy_pool_url = random.choice(PROXY_POOL)
        proxy_ip = urllib.request.urlopen(proxy_pool_url).read().decode("utf-8").split("\n")[1]
        if ',' in proxy_ip:
            proxy_ip = proxy_ip.split(',')[0]
        if 'http' in proxy_ip:
            proxy_ip = proxy_ip.split('//')[1]
        proxy = {'https': proxy_ip, 'http': proxy_ip}
        return proxy

    '''
    一次性获取user_agent,cookie、代理IP
    '''

    def get_agent_proxies(self):
        user_agent = random.choice(USER_AGENTS)
        proxy_pool_url = random.choice(PROXY_POOL)
        proxy_ip = urllib.request.urlopen(proxy_pool_url).read().decode("utf-8").split("\n")[1]
        # print(proxy_ip)
        if ',' in proxy_ip:
            proxy_ip = proxy_ip.split(',')[0]
        if 'http' in proxy_ip:
            proxy_ip = proxy_ip.split('//')[1]
        proxy = {'https': proxy_ip, 'http': proxy_ip}
        return (user_agent, proxy)

    '''
    从user_agent池获取一个user_agent
    '''

    def get_user_agent(self):
        return random.choice(USER_AGENTS)
