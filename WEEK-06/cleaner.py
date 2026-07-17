import re

def clean_price(price):
    number = re.findall(r"[\d.]+", price)[0]
    return float(number)
def clean_text(text):

    return text.strip()


def clean_rating(tag):

    classes = tag.get("class")

    for c in classes:

        if c != "star-rating":
            return c

    return "Unknown"