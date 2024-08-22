import scrapy
from scrapy.crawler import CrawlerProcess

class QuotesSpider(scrapy.Spider):
    name = "quotes_spider"
    custom_settings = {
        'ROBOTSTXT_OBEY': False  # Disable obeying robots.txt
    }
    
    start_urls = ['https://quotes.toscrape.com/']

    def parse(self, response):
        quotes = response.css('div.quote')
        
        for quote in quotes:
            text = quote.css('span.text::text').get()
            author = quote.css('span small.author::text').get()
            tags = quote.css('div.tags a.tag::text').getall()

            print(f"Quote: {text}")
            print(f"Author: {author}")
            print(f"Tags: {', '.join(tags)}")
            print("-" * 40)        

process = CrawlerProcess()
process.crawl(QuotesSpider)
process.start()