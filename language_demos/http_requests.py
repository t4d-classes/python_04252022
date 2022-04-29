import requests
import re
import time
from datetime import datetime

html_re = re.compile(r'data-field="regularMarketPrice" data-trend="none" data-pricehint="2" value="(.*?)"')

def get_stock_price(stock_symbol):
    response = requests.get(f"https://finance.yahoo.com/quote/{stock_symbol}?p={stock_symbol}&.tsrc=fin-srch")
    return html_re.search(response.text).group(1)

my_stocks = ['AMZN','MSFT','AAPL','FB','TSLA','TWTR']


with open("stock_prices.txt", "a", encoding="UTF-8") as stock_prices_file:

    while True:

        try:
            
            stock_prices_file.write(str(datetime.now()) + "\n")
            for my_stock in my_stocks:
                stock_prices_file.write(f"{my_stock}: {get_stock_price(my_stock)}\n")
                stock_prices_file.flush()

            time.sleep(5)

        except KeyboardInterrupt as exc:

            break





