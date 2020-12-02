import requests, json
from web_scraper import get_mentioned_tickers
import alpaca_trade_api as tradeapi

base_url = INSERT YOUR OWN
account_url = "{}/v2/account".format(base_url)
orders_url = "{}/v2/orders".format(base_url)
positions_url = "{}/v2/positions".format(base_url)
key_id = INSERT YOUR OWN
secret_key = INSERT YOUR OWN
header = {"APCA-API-KEY-ID": key_id, "APCA-API-SECRET-KEY": secret_key}
api = tradeapi.REST(key_id, secret_key)

def create_account():
    r = requests.get(account_url, headers = header)
    return json.loads(r.content)

def get_orders():
    r = requests.get(orders_url, headers = header)
    return json.loads(r.content)

def get_positions():
    r = requests.get(positions_url, headers = header)
    return json.loads(r.content)

def create_order(symbol, qty, side, type, time_in_force):
    data = {
        "symbol": symbol, 
        "qty": qty, 
        "side": side, 
        "type": type, 
        "time_in_force": time_in_force
    }
    r = requests.post(orders_url, json = data, headers = header) 
    return json.loads(r.content)

def get_price(ticker):
    barset = api.get_barset(ticker, 'day', limit=1)
    bars = barset[ticker][0].c
    return bars
    
# what it should look like
# x = ['GME', 'PLTR', 'TSLA', 'NKLA', 'CRSR', 'NIO', 'RKT', 'APHA']
# y = [77, 178, 12, 5, 4, 3, 3, 3]

x, y = get_mentioned_tickers()
total = sum(y)
amount = create_account()["portfolio_value"]
print(amount)

# Yeah there is supposed to be code here where you can just delete all your positions (which is fronwed upon) and then add your new ones but I'm too lazy right now

for i in range(len(x)):
    price = y[i] / total * int(amount)
    count = int(price // get_price(x[i]))
    print(price, count, x[i])
    response = create_order(x[i], count, "buy", "market", "gtc")


