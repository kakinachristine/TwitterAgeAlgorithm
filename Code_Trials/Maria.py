import tweepy as tp
from TwitterAPI import TwitterAPI
import pandas as pd



consumer_key = "PLGoMzQmSV8ZJ0PcqSdR84XUA"
consumer_secret = "A3m7kzzyW5qdtCqICsDj3NBzt8J8X4kNEj5sXylbPSVNx91Le9"
access_token = "1116019884318756865-myPhb6wZEmJkjOko9FQUiWyRYxLgiN"
access_token_secret = "C9hQ19K7IXRhk1zB37QJbtAt4qy1r1TvC4XPkjubXYuVQ"


auth = tp.OAuthHandler(consumer_key, consumer_secret)
api = tp.API(auth, wait_on_rate_limit=True)
Api = TwitterAPI(consumer_key, consumer_secret, access_token, access_token_secret, api_version='2')
AUTH = tp.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
client = tp.API(AUTH)


keyword = "family"
num_tweets = 9000  # Number of tweets to scrape

tweets = tp.Cursor(api.search_tweets, q=keyword, lang="en", geocode = "1.2921,36.8219,700km", tweet_mode="extended").items(num_tweets)

tweet_data = []
for tweet in tweets:
    country_code = None
    country = None
    full_name = None
    name = None
    place_type = None

    if tweet.place is not None:
        if tweet.place.country_code is not None:
            country_code = tweet.place.country_code
        if tweet.place.country is not None:
            country = tweet.place.country
        if tweet.place.full_name is not None:
            full_name = tweet.place.full_name
        if tweet.place.name is not None:
            name = tweet.place.name
        if tweet.place.place_type is not None:
            place_type = tweet.place.place_type

    tweet_data.append({
        "Tweet date": tweet.created_at,
        "Tweets": tweet.full_text,
        "Likes": tweet.favorite_count,
        "Retweets": tweet.retweet_count,
        "Quote Status?": tweet.is_quote_status,
        "Username": tweet.user.name,
        "Screenname": tweet.user.screen_name,
        "User ID": tweet.user.id_str,
        # "Location": tweet.user.location,
        "Account creation date": tweet.user.created_at,
        "Followers": tweet.user.followers_count,
        "Verified": tweet.user.verified,
        "Tweet country location name": country,
        "Tweet country location code": country_code,
        "Tweet city location fullname": full_name,
        "Tweet city location name": name,
        "Tweet location type": place_type,
    })

df = pd.DataFrame(tweet_data)
df.head()
df.to_csv("family1.csv", index=False)

print("CSV file created successfully.")


