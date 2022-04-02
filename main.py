import matplotlib.pyplot as plt
import random
import webscrape
import alpaca
import td_ameritrade


# Chad Mode
def chad(names, counts):
    #print(31231)
    #print(names)
    # print(len(names))
    for i in range(len(names)):
        alpaca.create_order(names[i], random.randint(2, 10))
        #print("hi")
    # print(3213213)

# Gambler Mode
def gambler(names, platform_mode = "alpaca"):
    random_idx = random.randint(0, len(names))
    max_quantity = 0
    if platform_mode == "alpaca":
        alpaca.create_order(names[random_idx], 1000)
    if platform_mode == "TD":
        REFRESH_TOEKN=input("REFRESH_TOEKN")
        CONSUMER_KEY=input("CONSUMER_KEY")
        ACCOUNT_ID=input("ACCOUNT_ID")
        td_ameritrade.buyyyy(names)

# Danger Mode
def danger():
    gambler("TD")
    pass



top_tickers = webscrape.ticker_count()
# print(top_tickers)
show_graph = input("Want to see today's pretty graph? Y or N")
if show_graph == "Y":
    final_ticker, final_count = webscrape.show_pretty_graph(top_tickers)
total_sum = sum(final_count)
print(final_ticker)
# while True:
mode = input("Enter your mode on how to lose money:\n1. Chad Mode (enter 1)\n2. Gambler Mode (enter 2)\n3. DANGER MODE (enter 3)")

if mode == '1':
    chad(final_ticker, final_count)
if mode == '2':
    gambler(final_ticker, final_count)
if mode == '3':
    danger(final_ticker, final_count)


mode = input("Enter your mode on how to lose money:\n1. Chad Mode (enter 1)\n2. Gambler Mode (enter 2)\n3. DANGER MODE (enter 3)")

if mode == '1':
    chad(final_ticker, final_count)
if mode == '2':
    gambler(final_ticker, final_count)
if mode == '3':
    danger(final_ticker, final_count)


mode = input("Enter your mode on how to lose money:\n1. Chad Mode (enter 1)\n2. Gambler Mode (enter 2)\n3. DANGER MODE (enter 3)")

if mode == '1':
    chad(final_ticker, final_count)
if mode == '2':
    gambler(final_ticker, final_count)
if mode == '3':
    danger(final_ticker, final_count)

