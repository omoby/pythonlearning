import requests
from parsel import Selector
from urllib.parse import urljoin

from JSReverse.python3_js.agent_util import AgentPoolUtil

pool_util = AgentPoolUtil()
proxy = pool_util.get_proxy()
url = 'http://www.porters.vip:8202/'

resp = requests.get(url, proxies=proxy)
text = Selector(resp.text)
shops = text.css('.col-md-3 a::attr("href")').extract()

for s in shops:
    detail = urljoin(url, s)
    detail_resp = requests.get(detail, proxies=proxy)
    print(detail_resp.text)
