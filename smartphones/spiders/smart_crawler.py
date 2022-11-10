from smartphones.items import SmartphonesItem

import scrapy
from scrapy.loader import ItemLoader


class SmartCrawlerSpider(scrapy.Spider):
    name = "smart_crawler"
    allowed_domains = ['ozon.ru']
    start_urls = [
        "https://www.ozon.ru/category/smartfony-15502/?sorting=rating"
    ]
    smartphone_links = []

    def parse(self, response, **kwargs):
        links = response.xpath(
            "//a[@class=\"tile-hover-target k8n\"]//@href"
        ).getall()
        next_page = response.xpath("//a[@class=\"_4-a1\"]//@href").get()
        for link in links:
            clear_link = link.split("?")[0]
            self.smartphone_links.append(response.urljoin(clear_link))
        if len(self.smartphone_links) <= 30:
            yield scrapy.Request(
                url=response.urljoin(next_page),
                callback=self.parse
            )
        else:
            for link in self.smartphone_links[0:30]:
                yield scrapy.Request(
                    url=link,
                    callback=self.parse_detail
                )

    def parse_detail(self, response):
        loader = ItemLoader(item=SmartphonesItem(), response=response)
        os_xpath = "//dt[span[contains(text(), 'Операционная')]]/following-sibling::dd"
        version_xpath = "//dt[span[contains(text(), 'Версия')]]/following-sibling::dd"

        loader.add_xpath("os", os_xpath)
        loader.add_xpath("version", version_xpath)

        item = loader.load_item()
        yield item
