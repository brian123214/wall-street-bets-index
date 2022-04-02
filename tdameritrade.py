

# code from https://github.com/alexgolec/tda-api/blob/master/examples/birthday_dividends.py

import atexit
import datetime
import dateutil
import httpx
import sys
import tda

API_KEY = 'XXXXXX'
REDIRECT_URI = 'https://localhost:8080/'
TOKEN_PATH = 'ameritrade-credentials.json'


def make_webdriver():
    # Import selenium here because it's slow to import
    from selenium import webdriver

    driver = webdriver.Chrome()
    atexit.register(lambda: driver.quit())
    return driver


# Create a new client
def buyyyy(API_KEY, REDIRECT_URI, TOKEN_PATH):
    client = tda.auth.easy_client(
    API_KEY,
    REDIRECT_URI,
    TOKEN_PATH,
    make_webdriver)


    
    # Build the order spec and place the order
    order = tda.orders.equities.equity_buy_market(symbol, 1)

    r = client.place_order(account_id, order)
    assert r.status_code == httpx.codes.OK, r.raise_for_status()
