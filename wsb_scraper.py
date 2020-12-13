import praw
from praw.models import MoreComments
import matplotlib.pyplot as plt

# Creates a set of stock tickers in NASDAQ
def get_tickers():
    fin = open("nasdaqtraded.txt", 'r')
    tickers = set()
    fin.readline()
    for line in fin.readlines():
        line = line[2:]
        tickers.add(line[:line.index("|")])
    return tickers

# Iterates through only head comments 
def iter_top_level(comments):
    for top_level_comment in comments:
        if isinstance(top_level_comment, MoreComments):
            yield from iter_top_level(top_level_comment.comments())
        else:
            yield top_level_comment

def get_data():
    reddit = praw.Reddit(client_id = "ENTER OWN", client_secret = "ENTER OWN", user_agent = "ENTER OWN")
    counter = 0
    # People may use use words that happen to be real ticker names
    flagged_words = ["YOLO", "PUMP", "RH", "EOD", "IPO", "ATH", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", 
        "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    ticker_set = get_tickers()
    tickers = {}
    sub = reddit.subreddit("wallstreetbets")
    for submission in sub.search('flair:"Daily Discussion"', limit = 1):
        print(submission.title)
        for comment in iter_top_level(submission.comments): 
            # set how many comments you want to search
            if counter == 1000:
                return tickers
            for word in comment.body.split():
                if word == word.upper() and word in ticker_set and word not in flagged_words:
                    if word not in tickers:
                        tickers[word] = 1
                    else:
                        tickers[word] += 1
            counter += 1
            counter += 1
    return tickers

def popularTickers():
    result = get_data()
    print(result)
    x = []
    y = []
    for a, b in result.items():
        # Can change value to see choose the threshold stock mention count 
        if b > 0:
            x.append(a)
            y.append(b)
    # If you want to see a plot of the number of mentioned tickers
    # x_pos = [i for i, _ in enumerate(x)]
    # plt.bar(x_pos, y, color='blue')
    # plt.xlabel("Tickers")
    # plt.ylabel("Mentions")
    # plt.title("Wall Street Bets Index")
    # plt.xticks(x_pos, x)
    # plt.show()
    return x, y
