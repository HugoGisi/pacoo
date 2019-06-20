import scrapy
from ..items import PacoItem


class CrSpider(scrapy.Spider):
    name = 'cr'
    start_urls = [
        'http://quotes.toscrape.com/'
    ]

    def parse(self, response):
        zitate = response.css('div.quote')
        items = PacoItem()

        for z in zitate:
            title = z.css('span.text::text').extract()
            autor = z.css('.author::text').extract()
            items['title'] = title
            items['autor'] = autor

            yield items
