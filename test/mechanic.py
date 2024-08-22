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