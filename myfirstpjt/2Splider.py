import scrapy

from myfirstpjt.items import MyfirstpjtItem


class MySpider(scrapy.Spider):
    name = 'farrell'
    allowed_domains = ['sina.com.cn']
    start_urls = (
        'https://news.sina.com.cn/c/xl/2020-04-11/doc-iircuyvh7132676.shtml',
        'https://news.sina.com.cn/c/2020-04-11/doc-iircuyvh7112886.shtml',
        'https://news.sina.com.cn/c/2020-04-11/doc-iirczymi5625991.shtml'
    )
    def parse(self, response):
        item = MyfirstpjtItem()
        item['url_name'] = response.xpath('/html/head/title/text()')
        print(item['url_name'])