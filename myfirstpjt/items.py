# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MyfirstpjtItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url_name = scrapy.Field()
    url_key = scrapy.Field()
    url_cr = scrapy.Field()
    url_addr = scrapy.Field()

    # pass
