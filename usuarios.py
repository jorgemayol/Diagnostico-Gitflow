import pandas as pd

def usuarios(tweets):
    maxs = tweets.max(10, ['userId'], skipna=True)
    print(maxs)
