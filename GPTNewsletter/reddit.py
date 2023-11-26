import praw
import os
from config import SUBBREDDITS_TO_QUERY
import traceback
import string

def remove_punctuation(word):

    punc_remove_list = [char in char in word if char not in string.punctuation]

def get_tickers_and_comments(log):
    print('in get_tickers_and_comments')


    try:
        reddit = praw.Reddit(
            client_id=os.environ["reddit_id"],
            client_secret=os.environ["reddit_secret"],
            user_agent=os.environ["reddit_user_agent"])

        print(reddit)

        word_collection = []

        log.info(f"looping through these subreddits: {SUBBREDDITS_TO_QUERY}")
        for subreddit_name in SUBBREDDITS_TO_QUERY:
            log.info(f"checking submissions in this subreddit: {subreddit_name}")

            subreddit = reddit.subreddit(subreddit_name)
            for submission in subreddit.hot(limit=5):
                log.info(f"\n====> Here is the SUBMISSION TITLE: {submission.title}")
                word_collection.extend(submission.title.split())

                # Load all MoreComments objects in the submission
                submission.comments.replace_more(limit=None)

                # Iterate through all comments, including those from MoreComments
                for comment in submission.comments.list():
                    log.info(f"HERE IS A COMMENT: {comment.body}")
                    word_collection.extend(comment.body.split())

        # we would have a collection of 
        for word in word_collection

    except Exception as e:
        log.error(f"Error in get_tickers_and_comments: {e}")
        log.error(f"Traceback for get_tickers_and_comments error: {traceback.format_exc()}")

if __name__ == "__main__":
    get_tickers_and_comments(None)  # Replace None with your logger instance
