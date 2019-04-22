# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LeFangcourseItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    course_url = scrapy.Field()
    company = scrapy.Field()
    price = scrapy.Field()
    user = scrapy.Field()
    pass
