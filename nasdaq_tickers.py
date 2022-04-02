# Creates a set of stock tickers in NASDAQ
def nasdaq_tickers():
    fin = open(r"C:\Users\User\Documents\Practice\wsb2.py\nasdaq.txt", 'r')
    tickers = set()
    fin.readline()
    for line in fin.readlines():
        line = line[2:]
        tickers.add(line[:line.index("|")])
    print("Done nasdaq")
    return tickers
