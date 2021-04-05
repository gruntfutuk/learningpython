"""look up some stock prices from ticker symbol
and save to a file <symbol>.txt"""

import requests
import bs4
from datetime import datetime
import time


class Stock:
    def __init__(self, symbol, url, filename, css_selector):
        self.symbol = symbol
        self.url = url
        self.filename = filename
        self.css_selector = css_selector
        self.get_price()

    @staticmethod
    def dateref():
        now = datetime.now()
        return now.strftime("%d/%m/%y")

    def write_file(self):
        with open(self.filename, "a") as f:
            f.write(f"\n{self.dateref()} - {self.real_price}")

    def get_price(self):
        try:
            res = requests.get(self.url)
        except (requests.ConnectionError, requests.exceptions.InvalidSchema) as e:
            print(e)
            self.real_price = None
        else:
            soup = bs4.BeautifulSoup(res.text, "html.parser")
            elems = soup.select(self.css_selector)
            data = str(elems)
            price = data
            price = price[123:10000]
            self.real_price = price.split("<")[0]
            self.write_file()

    def __str__(self):
        d3 = self.dateref()
        return f"{self.filename[:-4]} : ${self.real_price} - {d3}"


css_selector = "#quote-header-info > div.My\(6px\).Pos\(r\).smartphone_Mt\(6px\) > div.D\(ib\).Va\(m\).Maw\(65\%\).Ov\(h\) > div"
base_url = "https://uk.finance.yahoo.com/quote/"

stocks = []
while True:
    symbol = input("Enter symbol (or enter to exit): ").upper()
    if not symbol:
        break
    url = f"{base_url}{symbol}?p={symbol}"
    filename = f"{symbol}.txt"
    stocks.append(Stock(symbol, url, filename, css_selector))

for stock in stocks:
    print(stock)