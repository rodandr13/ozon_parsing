# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SmartphonesItem(scrapy.Item):
    os = scrapy.Field()
    version = scrapy.Field()
