import pandas as pd

def retweeted(tweets):
    maxs = tweets.max(10, ['retweetedTweet'], skipna=True)
    print(maxs)
