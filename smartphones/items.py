# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import TakeFirst, MapCompose
from w3lib.html import remove_tags

def clear_version(value):
    result = value.replace("(EMUI 12)", "").replace(".x", "").strip()
    return result.split()[-1]


class SmartphonesItem(scrapy.Item):
    os = scrapy.Field(
        output_processor=TakeFirst()
    )
    version = scrapy.Field(
        input_processor=MapCompose(remove_tags, clear_version),
        output_processor=TakeFirst()
    )