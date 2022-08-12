import pandas as pd

def hashtags(tweets):
    maxs = tweets.max(10, ['retweetedTweet'], skipna=True,)
    # df.nlargest(10, ['Weight']) 
    print(maxs)
