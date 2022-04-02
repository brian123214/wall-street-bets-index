import alpaca_trade_api as tradeapi

### ALPACA TRADING SITE
api = tradeapi.REST(
        'PYOUR KEY',
        'YOUR SECRERT KEY',
        'https://paper-api.alpaca.markets', api_version='v2'
    )

def create_order(ticker, qty, side='buy', type='market'):
    api.submit_order(
        symbol=ticker,
        qty=qty,
        side='buy',
        type='market',
        time_in_force='gtc'
    )
    # print("Order: " + ticker)

def clear_all_positions():
    # api.cancel_all_orders()
    all_positions = api.list_positions()
    print(all_positions)

def buying_power():
    account = api.get_account()
    return account.buying_power

# create_order("TSLA", 6)
# clear_all_positions()
