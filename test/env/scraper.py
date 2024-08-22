import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com/"

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

quotes = soup.find_all(class_="quote")

for quote in quotes:
    text = quote.find(class_="text").get_text()

    author = quote.find(class_="author").get_text()

    tags = [tag.get_text() for tag in quote.find_all(class_="tag")]

    print(f"Quote: {text}")
    print(f"Author: {author}")
    print(f"Tags: {', '.join(tags)}")
    print("-" * 40)
#########################################################################################
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

# Run Scrapy Spider
process = CrawlerProcess()
process.crawl(QuotesSpider)
process.start()

#############################################################################
import mechanicalsoup

browser = mechanicalsoup.StatefulBrowser()
url = "https://quotes.toscrape.com/"
browser.open(url)

soup = browser.page

quotes = soup.find_all(class_="quote")

for quote in quotes:
    text = quote.find(class_="text").get_text()
    author = quote.find(class_="author").get_text()
    tags = [tag.get_text() for tag in quote.find_all(class_="tag")]

    print(f"Quote: {text}")
    print(f"Author: {author}")
    print(f"Tags: {', '.join(tags)}")
    print("-" * 40)

browser.close()
###########################################################
import httpx
from bs4 import BeautifulSoup


url = "https://quotes.toscrape.com/"

response = httpx.get(url)

status_code = response.status_code
print(f"Status Code: {status_code}")

soup = BeautifulSoup(response.text, 'html.parser')

quotes = soup.find_all(class_="quote")

for quote in quotes:

    text = quote.find(class_="text").get_text()
    
    author = quote.find(class_="author").get_text()
    
    tags = [tag.get_text() for tag in quote.find_all(class_="tag")]
    
    print(f"Quote: {text}")
    print(f"Author: {author}")
    print(f"Tags: {', '.join(tags)}")
    print("-" * 40)
###################################################################
from playwright.sync_api import sync_playwright


playwright = sync_playwright().start()

browser = playwright.chromium.launch()
page = browser.new_page()

page.goto('https://quotes.toscrape.com/')

quotes = page.query_selector_all('.quote')

for quote in quotes:
    text = quote.query_selector('.text').text_content()
    author = quote.query_selector('.author').text_content()
    tags = [tag.text_content() for tag in quote.query_selector_all('.tag')]

    # Print the results
    print(f"Quote: {text}")
    print(f"Author: {author}")
    print(f"Tags: {', '.join(tags)}")
    print("-" * 40)

browser.close()
playwright.stop()
#playwright install // playwright install-deps  it dwonloads driver automatically and dependecies






