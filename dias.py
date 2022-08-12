import pandas as pd

def dias(tweets):
    maxs = tweets.max(10, ['date'], skipna=True,)
    # df.nlargest(10, ['Weight']) 
    print(maxs)
