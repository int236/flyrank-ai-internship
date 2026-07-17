import time
import requests

from bs4 import BeautifulSoup

from config import *
from cleaner import *

def scrape_books():

    books = []

    for page in range(1, MAX_PAGES + 1):

        if page == 1:

            url = BASE_URL + "/"

        else:

            url = BASE_URL + f"/catalogue/page-{page}.html"

        print(f"Scraping {url}")

        response = requests.get(
            url,
            headers=HEADERS
        )

        soup = BeautifulSoup(
            response.text,
            "lxml"
        )

        articles = soup.find_all(
            "article",
            class_="product_pod"
        )

        for article in articles:

            title = clean_text(
                article.h3.a["title"]
            )

            price = clean_price(
                article.find(
                    "p",
                    class_="price_color"
                ).text
            )

            availability = clean_text(
                article.find(
                    "p",
                    class_="instock availability"
                ).text
            )

            rating = clean_rating(
                article.find(
                    "p",
                    class_="star-rating"
                )
            )

            relative = article.h3.a["href"]

            if relative.startswith("../"):

                relative = relative.replace("../", "")

            book_url = (
                BASE_URL
                + "/catalogue/"
                + relative
            )

            books.append({

                "title": title,
                "price": price,
                "availability": availability,
                "rating": rating,
                "url": book_url

            })

        time.sleep(DELAY)

    return books