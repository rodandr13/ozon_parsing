import scrapy


class SmartCrawlerSpider(scrapy.Spider):
    name = 'smart_crawler'
    allowed_domains = ['ozon.ru']
    start_urls = ['http://ozon.ru/']

    def parse(self, response):
        pass
