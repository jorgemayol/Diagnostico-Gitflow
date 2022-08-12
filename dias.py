import pandas as pd

def dias(tweets):
    maxs = tweets.max(10, ['date'], skipna=True)
    print(maxs)
