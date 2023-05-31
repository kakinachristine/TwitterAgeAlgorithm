import csv
import re


def is_young_person(tweet):
    # Check for keywords in the user's profile description
    profile_keywords = ["teen", "student", "high school"]
    profile_description = tweet.get("description", "").lower()
    if any(keyword in profile_description for keyword in profile_keywords):
        return True

    # Check for keywords in the tweet content
    content_keywords = ["school", "exam", "homework"]
    tweet_content = tweet.get("content", "").lower()
    if any(keyword in tweet_content for keyword in content_keywords):
        return True

    # Check for Retweets and Replies
    if "rt @" in tweet_content.lower():
        return True

    if "reply" in tweet_content.lower():
        return True

    # Check for Memes and Internet Culture
    meme_keywords = ["😂", "🎶"]
    if any(keyword in tweet_content for keyword in meme_keywords):
        return True

    # Check for Expressive Language
    expressive_keywords = ["obsessed", "aced"]
    if any(keyword in tweet_content for keyword in expressive_keywords):
        return True

    # Check for Social Justice and Activism
    social_keywords = ["climate change", "equality"]
    if any(keyword in tweet_content for keyword in social_keywords):
        return True

    # Check for memes
    meme_keywords = []
    if any(keyword in tweet_content for keyword in meme_keywords):
        return True

    # Check for mentions of influential individuals
    influencer_keywords = ["@celebrity", "@musician", "@athlete"]
    if any(keyword in tweet_content for keyword in influencer_keywords):
        return True

    return False


# Read tweets from the CSV file
tweets = []
with open("tweets.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        tweets.append(row)

# Filter and store young tweets
young_tweets = []
for tweet in tweets:
    if is_young_person(tweet):
        young_tweets.append(tweet)

# Define the column names for the new CSV file
columns = ["date", "id", "content", "username", "likeCount", "retweetCount", "location", "hashtag", "source"]

# Write young tweets to a new CSV file
with open("lgbtq_hashtags.csv", "w", encoding="utf-8", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=columns)
    writer.writeheader()
    writer.writerows(young_tweets)
