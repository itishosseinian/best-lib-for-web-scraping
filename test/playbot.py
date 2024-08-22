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