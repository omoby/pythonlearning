import random
import urllib


from MTStoreDetail.agent_pool import PROXY_POOL, MT_6_COOKIE, USER_AGENTS

'''
代理池工具类
'''
class AgentPoolUtil():
    '''
    从IP代理池获取一个代理IP
    '''
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
        cookie = random.choice(MT_6_COOKIE)
        proxy_ip = urllib.request.urlopen(proxy_pool_url).read().decode("utf-8").split("\n")[1]
        if ',' in proxy_ip:
            proxy_ip = proxy_ip.split(',')[0]
        if 'http' in proxy_ip:
            proxy_ip = proxy_ip.split('//')[1]
        proxy = {'https': proxy_ip, 'http': proxy_ip}
        return (user_agent,proxy,cookie)

    '''
    从user_agent池获取一个user_agent
    '''
    def  get_user_agent(self):
        return  random.choice(USER_AGENTS)

    '''
    从cookie池获取一个cookie
    '''
    def get_cookie(self):
        cookie = random.choice(MT_6_COOKIE)
        return cookie