import praw
from praw.models import MoreComments
import matplotlib.pyplot as plt

# Gets the top 100 common english words since some tickers have the same name as common words
def get_common():
    fin = open("common.txt", 'r')
    words = set()
    for x in fin.readlines():
        words.add(x[:-1])
    return words
    
# Creates set of tickers
def get_tickers():
    fin = open("nasdaqtraded.txt", 'r')
    tickers = set()
    temp = "0"
    fin.readline()
    while temp != "" and temp[0] != "F":
        temp = fin.readline().strip()
        try:
            temp1 = (temp[2:temp.index("|", 3)]).upper()
            tickers.add(temp1)
        except:
            pass
    return tickers
    
def iter_top_level(comments):
    for top_level_comment in comments:
        if isinstance(top_level_comment, MoreComments):
            yield from iter_top_level(top_level_comment.comments())
        else:
            yield top_level_comment
            

def get_data():
    reddit = praw.Reddit(client_id = ENTER YOUR OWN, client_secret = ENTER YOUR OWN, user_agent = ENTER YOUR OWN)
    counter = 0
    common_words = get_common()
    ticker_set = get_tickers()
    tickers = dict()

    sub = reddit.subreddit("wallstreetbets")
    for submission in sub.search('flair:"Daily Discussion"', limit = 1):
        print(submission.title)
        for comment in iter_top_level(submission.comments): 
            # set counter to how many comments you want to search
            if counter == 400:
                return tickers
            comment_set = set(comment.body.upper().split())
            similar = comment_set.intersection(ticker_set)
            for word in similar:
                if word.lower() in common_words:
                    continue
                if word not in tickers:
                    tickers[word] = 1
                else:
                    tickers[word] += 1
            counter += 1
    return tickers

def get_mentioned_tickers():
    result = get_data()
    x = []
    y = []
    
    # Threshold is how many mentions you want for a ticker to be considered
    threshold = 5
    for a, b in result.items():
    
        if b > threshold:
            x.append(a)
            y.append(b)
            
    final_x = x
    final_y = y
    
    # Can include the following if you want to prune the tickers yourself to check if there are tickers that are actually just a common word in there
    # for j in range(len(x)):
    #     user = input("Is " + x[j] + " an actual ticker? t or f (some tickers share names with common words)")
    #     if user == "t":
    #         final_x.append(x[j])
    #         final_y.append(y[j])
    
    # Can include if you want to see a bar graph
    # x_pos = [i for i, _ in enumerate(final_x)]
    # plt.bar(x_pos, final_y, color='blue')
    # plt.xlabel("Tickers")
    # plt.ylabel("Mentions")
    # plt.title("Wall Street Bets Index")
    # plt.xticks(x_pos, final_x)
    # plt.show()
    
    return final_x, final_y


