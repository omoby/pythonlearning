import scrapy

class MyFirstSpider(scrapy.Spider):
    name = 'farrell'
    allowed_domains = ['iqianyue.com']
    start_urls = ('https://www.iqianyue.com/')
    def parse(self,response):
        pass