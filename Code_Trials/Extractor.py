import tweepy
import csv

# Twitter API credentials
consumer_key = "YOUR_CONSUMER_KEY"
consumer_secret = "YOUR_CONSUMER_SECRET"
access_token = "YOUR_ACCESS_TOKEN"
access_token_secret = "YOUR_ACCESS_TOKEN_SECRET"

# Authenticate to Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Create API object
api = tweepy.API(auth)

# Function to scrape tweet and user details
def scrape_tweet_and_user_details(query, count):
    # Open CSV file for writing
    with open('twitter_data.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Username', 'Bio', 'Location', 'Followers Count', 'Friends Count', 'Tweet Content', 'Retweets', 'Likes'])

        # Scrape tweets based on the query
        tweets = tweepy.Cursor(api.search, q=query, lang="en", tweet_mode="extended").items(count)
        for tweet in tweets:
            username = tweet.user.screen_name
            bio = tweet.user.description
            location = tweet.user.location
            followers_count = tweet.user.followers_count
            friends_count = tweet.user.friends_count
            tweet_content = tweet.full_text
            retweets_count = tweet.retweet_count
            likes_count = tweet.favorite_count

            # Write details to the CSV file
            writer.writerow([username, bio, location, followers_count, friends_count, tweet_content, retweets_count, likes_count])

# Example usage: Scrape tweet and user details for a specific query and count
scrape_tweet_and_user_details(query='relationship', count=100)
