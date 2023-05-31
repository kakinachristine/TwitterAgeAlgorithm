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

    # Check for language patterns or slang
    slang_patterns = ["omg", "lol", "bff"]
    if any(pattern in tweet_content for pattern in slang_patterns):
        return True

    # Check for engagement with youth-related accounts
    engagement_accounts = ["youthorg1", "celebteen2", "musician123"]
    for mention in tweet.get("username", []):
        if mention in engagement_accounts:
            return True

    # Check for media content related to youth
    if tweet.get("hashtag") and "youth" in tweet.get("hashtag"):
        return True

    return False


# Read tweets from the CSV file
tweets = []
with open("Code_Trials/lgbtq_hashtags.csv", "r", encoding="utf-8") as file:
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
with open("Code_Trials/young_tweets.csv", "w", encoding="utf-8", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=columns)
    writer.writeheader()
    writer.writerows(young_tweets)
