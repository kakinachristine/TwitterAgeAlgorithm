import tweepy as tp
from TwitterAPI import TwitterAPI
import pandas as pd

consumer_key = "PLGoMzQmSV8ZJ0PcqSdR84XUA"
consumer_secret = "A3m7kzzyW5qdtCqICsDj3NBzt8J8X4kNEj5sXylbPSVNx91Le9"
access_token = "1116019884318756865-myPhb6wZEmJkjOko9FQUiWyRYxLgiN"
access_token_secret = "C9hQ19K7IXRhk1zB37QJbtAt4qy1r1TvC4XPkjubXYuVQ"

auth = tp.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tp.API(auth, wait_on_rate_limit=True)

keyword = "religion"
num_tweets = 1000 # Number of tweets to scrape

tweets = tp.Cursor(api.search_tweets, q=keyword, lang="en", tweet_mode="extended").items(num_tweets)

tweet_data = []
for tweet in tweets:
    tweet_data.append({
        "Username": tweet.user.screen_name,
        "Text": tweet.full_text,
        "Date": tweet.created_at
    })

df = pd.DataFrame(tweet_data)
df.to_csv("religion.csv", index=False)

print("CSV file created successfully.")
