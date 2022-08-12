import pandas as pd

def hashtags(tweets):
    maxs = tweets.max(10, ['retweetedTweet'], skipna=True)
    print(maxs)
