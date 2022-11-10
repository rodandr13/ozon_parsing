# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json
import pandas as pd
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class SmartphonesPipeline:
    def process_item(self, item, spider):
        return item

    def close_spider(self, spider):
        with open("result.json", "r", encoding="utf-8") as file:
            result = json.load(file)
        df = pd.DataFrame(result)
        print(df.value_counts())

