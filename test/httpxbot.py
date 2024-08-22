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

    