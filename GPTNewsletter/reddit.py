import praw
import os 

def get_tickers_and_comments():
    print('in get_tickers_and_comments')

    reddit = praw.Reddit(
        client_id=os.environ["reddit_id"],
        client_secret=os.environ["reddit_secret"],
        user=os.environ["reddit_user"],
        password=os.environ["reddit_pass"],
        user_agent=os.environ["reddit_user_agent"])
    
    print(reddit)