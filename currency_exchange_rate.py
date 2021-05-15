import requests
from bs4 import BeautifulSoup
import time


class Currency:
    DOLLAR_RUB = "https://bit.ly/2QuwGpq"
    headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0"}

    current_converted_price = 0
    difference = 5

    def __init__(self):
        self.current_converted_price = float(self.get_currency_price().replace(",", "."))

    def get_currency_price(self):
        full_page = requests.get(self.DOLLAR_RUB, headers=self.headers)

        soup = BeautifulSoup(full_page.content, "html.parser")
        convert = soup.find_all("span", {"class": "DFlfde SwHCTb"})
        return convert[0].text

    def check_currency(self):
        currency = float(self.get_currency_price().replace(",", "."))
        if currency >= self.current_converted_price + self.difference:
            print("The exchange rate went up.")
        elif currency <= self.current_converted_price + self.difference:
            print("The exchange rate went down.")
        print("Current exchange rate: 1 dollar = " + str(currency) + " rubles")
        time.sleep(30)
        self.check_currency()


currency = Currency()
currency.check_currency()
