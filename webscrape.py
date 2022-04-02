import praw
import matplotlib.pyplot as plt
from praw.models import MoreComments
import nasdaq_tickers


# Iterates through only head comments 
def iter_top_level(comments):
    for top_level_comment in comments:
        if isinstance(top_level_comment, MoreComments):
            yield from iter_top_level(top_level_comment.comments())
        else:
            yield top_level_comment

def ticker_count():
    reddit = praw.Reddit(client_id = "uCybnV74Sk54kw", client_secret = "IvjLZyB77t2sJSJlSato2zTiEebZ1g", user_agent = "my useer agent")
    # People may use use words that happen to be real ticker names
    flagged_words = ["YOLO", "PUMP", "RH", "EOD", "IPO", "ATH", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", 
        "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "GDP"]
    ticker_set = nasdaq_tickers.nasdaq_tickers()
    tickers = {}
    # Enter the url of daily discussion post
    url = "https://www.reddit.com/r/wallstreetbets/comments/kt0a9h/daily_discussion_thread_for_january_08_2021/"
    submission = reddit.submission(url=url)
    # print(submission.title)

    counter = 0
    for comment in iter_top_level(submission.comments): 
        # set how many comments you want to search
        if counter == 400:
            break
        for word in comment.body.split():
            if word == word.upper() and word in ticker_set and word not in flagged_words:
                if word not in tickers:
                    tickers[word] = 1    
                tickers[word] += 1
        counter += 1
        if counter % 100 == 0:
            print("Progress: " + str(counter))
        # print(counter)
    return tickers

def show_pretty_graph(result):
    x = sorted(result, key = result.get, reverse = True)[:10]
    y = ([result[i] for i in x])
    # print(x)
    # print(y)
    # x_pos = [i for i, _ in enumerate(x)]
    # plt.bar(x_pos, y, color='blue')
    # plt.xlabel("Tickers")
    # plt.ylabel("Mentions")
    # plt.title("Wall Street Bets Index")
    # plt.xticks(x_pos, x)
    # plt.show()
    fig1, ax1 = plt.subplots()
    ax1.pie(y, labels=x, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.show()
    return x, y
