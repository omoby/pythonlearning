import requests
import re
from parsel import Selector

url = 'http://www.porters.vip/confusion/flight.html'
resp = requests.get(url)

sel = Selector(resp.text)
em  = sel.css('em.rel').extract()
# print(em)
for element in em:
    element = Selector(element)
    element_b = element.css('b').extract()
    # print(element_b)
    b1 = Selector(element_b.pop(0))
    b1_style = b1.css('b::attr("style")').get()

    b1_width = ''.join(re.findall('width:(.*)px;',b1_style))
    nubmer = int(int(b1_width) / 16)
    base_price = b1.css('i::text').extract()[:nubmer]
    # print(base_price)
    alternate_price = []
    for eb in element_b:
        eb = Selector(eb)
        style = eb.css('b::attr("style")').get()
        position = ''.join(re.findall('left:(.*)px',style))
        value = eb.css('b::text').get()
        alternate_price.append({'position':position,'value':value})

    # print(alternate_price)
    for al in alternate_price:
        position = int(al.get('position'))
        value = al.get('value')

        plus = True if position>=0 else False

        index = int(position / 16)
        base_price[index] = value
    print(base_price)