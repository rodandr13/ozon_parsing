import scrapy
import pprint

from smartphones.items import SmartphonesItem


class SmartCrawlerSpider(scrapy.Spider):
    name = "smart_crawler"
    allowed_domains = ['ozon.ru']
    start_urls = ["https://www.ozon.ru/category/smartfony-15502/?sorting=rating"]
    smartphone_links = []
    base_url = "https://www.ozon.ru"
    os_ver = []

    def parse(self, response, **kwargs):
        links = response.xpath("//a[@class=\"tile-hover-target k8n\"]//@href").getall()
        next_page = response.xpath("//a[@class=\"_4-a1\"]//@href").get()
        for link in links:
            clear_link = link.split("?")[0]
            self.smartphone_links.append(response.urljoin(clear_link))
        if len(self.smartphone_links) <= 100:
            yield scrapy.Request(
                url=response.urljoin(next_page),
                callback=self.parse
            )
        else:
            for link in self.smartphone_links:
                yield scrapy.Request(
                    url=link,
                    callback=self.parse_detail
                )

    def parse_detail(self, response):
        items = SmartphonesItem()
        os = response.xpath("//dt[span[contains(text(), 'Операционная')]]/following-sibling::dd/a/text()").get()
        version = response.xpath("//dt[span[contains(text(), 'Версия')]]/following-sibling::dd/a/text()").get()
        if not version:
            version = response.xpath("//dt[span[contains(text(), 'Версия')]]/following-sibling::dd/text()").get()
        #self.os_ver.append({os, version, response.url})
        #print(len(self.os_ver))
        #print(self.os_ver)
        for val in self.os_ver:
            print(val)
        items["os"] = os
        items["version"] = version
        yield items