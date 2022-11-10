import pandas as pd


class SmartphonesPipeline:
    items = []

    def process_item(self, item, spider):
        self.items.append(item)
        return item

    def close_spider(self, spider):
        df = pd.DataFrame(self.items)
        result = df.value_counts()
        with open("result.csv", "w", encoding="utf-8") as file:
            file.write(result.to_csv())
        print(result)
