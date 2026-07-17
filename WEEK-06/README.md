# Books Scraper

## Features
- Fetches book pages
- Parses HTML using BeautifulSoup
- Extracts:
  - Title
  - Price
  - Availability
  - Rating
  - URL
- Cleans extracted data
- Robots Exclusion Protocol (REP) Compliance
- Uses a custom User-Agent
- Applies 1-second rate limiting
- Saves structured JSON

## Install
```bash
pip install -r requirements.txt
```

Run
```bash
python main.py
```