# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GetertongItem(scrapy.Item):
    title = scrapy.Field()
    detailUrl = scrapy.Field()
    content = scrapy.Field()
    imageUrl = scrapy.Field()
    detailcontent = scrapy.Field()
