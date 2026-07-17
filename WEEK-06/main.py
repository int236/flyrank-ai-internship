import os
import json

from scraper import scrape_books
from robots import allowed

URL = "https://books.toscrape.com/"

if not allowed(URL):

    print("Scraping not allowed!")

    exit()

books = scrape_books()

os.makedirs(
    "output",
    exist_ok=True
)

with open(
    "output/books.json",
    "w",
    encoding="utf8"
) as f:

    json.dump(
        books,
        f,
        indent=4,
        ensure_ascii=False
    )

print()

print(f"Saved {len(books)} books")

print("Output:")
print("output/books.json")