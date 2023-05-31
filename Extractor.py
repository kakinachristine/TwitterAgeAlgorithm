# Set your access token and access token secret here
# consumer_key = "hfUwEmVj1MBGVCzBYTruuJ5DM"
# consumer_secret = "f9DPSA5prXj1qPfHDZdFEP7CIcUtFFMA3akqbHiY6llgjuDi5l"
# access_token = "1324250489500950528-swRPRXUMqTPltEPUQXmiGUDdIRRJ8q"
# access_token_secret = "nP9Ku0YnwYx1zsBMZGzntppv6YXUwyKQPq07fsgcOO6BB"
import tweepy
import pandas as pd

from config import *
import tweepy
import datetime


# Set up Tweepy API credentials
consumer_key = "hfUwEmVj1MBGVCzBYTruuJ5DM"
consumer_secret = "f9DPSA5prXj1qPfHDZdFEP7CIcUtFFMA3akqbHiY6llgjuDi5l"
access_token = "1324250489500950528-swRPRXUMqTPltEPUQXmiGUDdIRRJ8q"
access_token_secret = "nP9Ku0YnwYx1zsBMZGzntppv6YXUwyKQPq07fsgcOO6BB"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication Successful")
except:
    print("Authentication Error")

client = tweepy.Client(consumer_key= consumer_key,consumer_secret= consumer_secret,access_token= access_token,access_token_secret= access_token_secret)
query = 'news'
tweets = client.search_recent_tweets(query=query, max_results=10)
for tweet in tweets.data:
    print(tweet.text)

