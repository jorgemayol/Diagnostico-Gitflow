import pandas as pd
from pandas.io.json import json_normalize
import warnings
from retweeted.py import retweeted
from dias.py import dias
from hashtags.py import hashtags

warnings.filterwarnings("ignore")

##### Obtenido de https://www.kaggle.com/code/prathamsharma123/clean-raw-json-tweets-data #####

raw_tweets = pd.read_json(r'farmers-protest-tweets-2021-03-5.json', lines=True)
raw_tweets = raw_tweets[raw_tweets['lang']=='en']

users = json_normalize(raw_tweets['user'])
users.drop(['description', 'linkTcourl', 'displayname', 'descriptionUrls', 'verified'], axis=1, inplace=True)
users.rename(columns={'id':'userId', 'url':'profileUrl'}, inplace=True)
users = pd.DataFrame(users)
users.drop_duplicates(subset=['userId'], inplace=True)

# Add column for 'userId'
user_id = []
for user in raw_tweets['user']:
    uid = user['id']
    user_id.append(uid)
raw_tweets['userId'] = user_id

# Remove less important columns
cols = ['url', 'date', 'renderedContent', 'id', 'userId', 'replyCount', 'retweetCount', 'likeCount', 'quoteCount', 'source', 'media', 'retweetedTweet', 'quotedTweet', 'mentionedUsers']
tweets = raw_tweets[cols]
tweets.rename(columns={'id':'tweetId', 'url':'tweetUrl'}, inplace=True)

# Convert to DataFrame, remove duplicates and keep only English tweets

tweets = pd.DataFrame(tweets)
tweets.drop_duplicates(subset=['tweetId'], inplace=True)

###########################################################################
retweeted(tweets)
dias(tweets)
hashtags(tweets)