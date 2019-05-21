import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst
from tutorial.items import QuoteItem

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            loader = ItemLoader(item=QuoteItem())
            loader.title_out = TakeFirst()
            loader.author_out = TakeFirst()
            loader.add_value('title', quote.css('span.text::text').get())
            loader.add_value('author', quote.css('span small::text').get())
            loader.add_value('tag_list', quote.css('div.tags a.tag::text').getall())
            yield loader.load_item()

        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
