# API Key HPHNf4Y5hN74riiNrHufoz47e
#  API Key Secret lkC8IAdsO8G0z7f7AuBXsA3pu3qY0OTkhNdPPDNDCUD9GuOAAh
# Access Token 1324250489500950528-4cR4ihK4SNFmjY7nQlz2LHpJ9UtG5M
#  Access Token Secret 3pby55CciYfzT0l2oPOzV0NWubT5fRiDx4MQlpL3FGv6X

import csv
import snscrape.modules.twitter as sntwitter
import tweepy

# Twitter API credentials
consumer_key = "HPHNf4Y5hN74riiNrHufoz47e"
consumer_secret = "lkC8IAdsO8G0z7f7AuBXsA3pu3qY0OTkhNdPPDNDCUD9GuOAAh"
access_token = "1324250489500950528-4cR4ihK4SNFmjY7nQlz2LHpJ9UtG5M"
access_token_secret = "3pby55CciYfzT0l2oPOzV0NWubT5fRiDx4MQlpL3FGv6X"


# Configure authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Initialize the Twitter API client
api = tweepy.API(auth)

# Define the username to scrape
username = "Beyonce"

# Define keywords for age-related analysis
age_keywords = ["13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35"]
education_keywords = ["student", "graduate", "school", "college"]
occupation_keywords = ["intern", "junior", "job title"]
topic_keywords = ["gaming", "music", "sports", "pop culture"]
milestone_keywords = ["driver's license", "prom", "graduation"]

# Extract user information
user = api.get_user(username)
bio = user.description

# Check for age-related keywords in the bio
has_age_keywords = any(keyword in bio for keyword in age_keywords)

# Check for education-related keywords in the bio
has_education_keywords = any(keyword in bio for keyword in education_keywords)

# Check for occupation-related keywords in the bio
has_occupation_keywords = any(keyword in bio for keyword in occupation_keywords)

# Extract tweets using snscrape
tweets = []
for i, tweet in enumerate(sntwitter.TwitterUserScraper(username).get_items()):
    tweets.append(tweet.content)
    if i == 19:  # Limit the number of tweets for demonstration purposes
        break

# Analyze interests and hobbies from tweets
interests = set()
for tweet in tweets:
    for keyword in topic_keywords:
        if keyword in tweet.lower():
            interests.add(keyword)

# Analyze conversation topics and milestones from tweets
conversation_topics = set()
milestones = set()
for tweet in tweets:
    for keyword in topic_keywords:
        if keyword in tweet.lower():
            conversation_topics.add(keyword)
    for keyword in milestone_keywords:
        if keyword in tweet.lower():
            milestones.add(keyword)

# Estimate age based on user's bio
estimated_ages = []
for keyword in age_keywords:
    if keyword in bio:
        age = int(keyword)
        if age >= 13 and age <= 35:
            estimated_ages.append(age)

# Write the extracted data to a CSV file
filename = "extracted_data.csv"
header = ["Username", "Bio: Has Age Keywords", "Bio: Has Education Keywords", "Bio: Has Occupation Keywords",
          "Interests and Hobbies", "Conversation Topics", "Milestones", "Estimated Ages"]

with open(filename, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(header)
    writer.writerow([username, has_age_keywords, has_education_keywords, has_occupation_keywords,
                     ', '.join(interests), ', '.join(conversation_topics), ', '.join(milestones), ', '.join(map(str, estimated_ages))])

print("Data extracted and stored in", filename)