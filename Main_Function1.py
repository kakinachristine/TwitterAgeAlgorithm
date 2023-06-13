import csv


def is_young_person(tweet):
    profile_keywords = ["teen", "student", "high school", "school", "university", "graduation", "youth", "gen z",
                        "millennial", "emoji", "slang", "pop culture", "video games", "social media",
                        "youth organization", "activism", "influencer", "content creator"]
    profile_description = tweet.get("Tweet", "").lower()
    if any(keyword in profile_description for keyword in profile_keywords):
        return True

    content_keywords = ["school", "exam", "homework", "lit", "squad", "flex", "fomo", "gucci", "clout", "savage",
                        "salty", "ghost", "extra", "mood", "basic", "vibes", "snack", "tea", "thirsty", "swag",
                        "lituation", "woke", "bet", "fam", "yolo", "bae", "on fleek", "slay", "no cap", "goat", "dm",
                        "ship", "tbt", "goals", "dope", "hella", "lurk", "shade", "triggered", "turn up", "snatched",
                        "lit af"]
    tweet_content = tweet.get("Tweet", "").lower()
    if any(keyword in tweet_content for keyword in content_keywords):
        return True

    if "rt @" in tweet_content.lower():
        return True

    if "reply" in tweet_content.lower():
        return True

    meme_keywords = ["meme", "viral", "trending", "dank", "hilarious", "funny", "lmao", "rofl", "meme culture",
                     "internet humor", "gifs", "vines", "reaction images", "pepe", "rickroll", "doge",
                     "spongebob memes", "shitposting", "wojak", "expanding brain meme"]
    if any(keyword in tweet_content.lower() for keyword in meme_keywords):
        return True

    expressive_keywords = ["obsessed", "aced"]
    if any(keyword in tweet_content for keyword in expressive_keywords):
        return True

    social_keywords = ["climate change", "equality", "intersectionality", "systemic racism", "lgbtq+ rights",
                       "feminism", "black lives matter", "climate justice", "indigenous rights", "body positivity",
                       "mental health awareness", "youth activism", "immigration rights", "human rights", "inclusivity",
                       "anti-discrimination", "activism", "social equality", "gender equality", "environmental justice",
                       "economic justice", "police brutality", "mass incarceration", "voting rights", "gun control",
                       "reproductive rights", "disability rights", "transgender rights", "access to education",
                       "income inequality", "healthcare access", "cultural appropriation", "racial profiling",
                       "anti-hate speech", "digital privacy", "fair trade", "youth engagement", "community organizing",
                       "peaceful protests"]
    if any(keyword in tweet_content.lower() for keyword in social_keywords):
        return True

    emoji_keywords = ["😂", "❤", "😍", "😭", "🙌", "🤔", "😊", "🙏", "🥺", "🤣", "🥰", "😒", "🤩", "🙈", "🤷‍♀️", "🔥",
                     "😎", "🤪"]
    if any(keyword in tweet_content for keyword in emoji_keywords):
        return True

    influencer_keywords = ["Beyoncé", "Jay-Z", "Prince Harry", "Meghan Markle", "David Beckham", "Victoria Beckham",
                           "Kim Kardashian", "Kanye West", "John Legend", "Chrissy Teigen", "Barack Obama",
                           "Michelle Obama", "Wizkid", "Tiwa Savage", "Diamond Platnumz", "Tanasha Donna",
                           "Justin Bieber", "Hailey Baldwin", "Selena Gomez", "The Weeknd", "Ariana Grande",
                           "Dalton Gomez", "Shawn Mendes", "Camila Cabello", "Zayn Malik", "Gigi Hadid",
                           "Emma Chamberlain", "David Dobrik", "James Charles", "Liza Koshy", "Brent Rivera",
                           "Lele Pons", "Davido", "Chioma"]
    if any(keyword in tweet_content for keyword in influencer_keywords):
        return True

    content_keywords = ["school", "exam", "homework", "lit", "squad", "flex", "fomo", "gucci", "clout", "savage",
                        "salty", "ghost", "extra", "mood", "basic", "vibes", "snack", "tea", "thirsty", "swag",
                        "lituation", "woke", "bet", "fam", "yolo", "bae", "on fleek", "slay", "no cap", "goat", "dm",
                        "ship", "tbt", "goals", "dope", "hella", "lurk", "shade", "triggered", "turn up", "snatched",
                        "lit af"]
    tweet_content = tweet.get("Tweet", "").lower()

    if any(keyword in tweet_content for keyword in content_keywords):
        return True

    slang_patterns = ["omg", "lol", "bff", "brb", "idk", "tbh", "fyi", "smh", "tbt", "irl", "af", "yolo", "fomo", "imo",
                      "ttyl", "nvm", "jk", "ikr", "hbu", "btw", "rn", "ftw", "irl", "fomo", "lmk", "ama", "tfw", "hbd",
                      "ily", "imo", "yolo", "np", "ngl", "gtg", "rofl", "tgif", "wyd", "wcw"]
    if any(pattern in tweet_content.lower() for pattern in slang_patterns):
        return True

    return False


tweets = []
with open("Relations1.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        tweet_date = row.get("Tweet date", "")
        tweet_text = row.get("Tweets", "")
        likes = row.get("Likes", "")
        retweets = row.get("Retweets", "")
        quote_status = row.get("Quote Status?", "")
        username = row.get("Username", "")
        screenname = row.get("Screenname", "")
        user_id = row.get("User ID", "")
        account_creation_date = row.get("Account creation date", "")
        followers = row.get("Followers", "")
        verified = row.get("Verified", "")
        tweet_country_location_name = row.get("Tweet country location name", "")
        tweet_country_location_code = row.get("Tweet country location code", "")
        tweet_city_location_fullname = row.get("Tweet city location fullname", "")
        tweet_city_location_name = row.get("Tweet city location name", "")
        tweet_location_type = row.get("Tweet location type", "")
        relations = row.get("Relations", "")

        tweets.append({
            "Tweet date": tweet_date,
            "Tweets": tweet_text,
            "Likes": likes,
            "Retweets": retweets,
            "Quote Status?": quote_status,
            "Username": username,
            "Screenname": screenname,
            "User ID": user_id,
            "Account creation date": account_creation_date,
            "Followers": followers,
            "Verified": verified,
            "Tweet country location name": tweet_country_location_name,
            "Tweet country location code": tweet_country_location_code,
            "Tweet city location fullname": tweet_city_location_fullname,
            "Tweet city location name": tweet_city_location_name,
            "Tweet location type": tweet_location_type,
            "Relations": relations
        })

# Load the tweets from the CSV file
tweets = []
with open("Relations1.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        tweets.append(row)

# Filter the young tweets
young_tweets = [tweet for tweet in tweets if is_young_person(tweet)]

# Write the filtered tweets to a new CSV file
columns = ["Tweet date", "Tweet", "Likes", "Retweets", "Quote Status?", "Username", "Screenname", "User ID",
           "Account creation date", "Followers", "Verified", "Tweet country location name",
           "Tweet country location code", "Tweet city location fullname", "Tweet city location name",
           "Tweet location type", "Relations"]

with open("sample1.csv", "w", encoding="utf-8", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=columns)
    writer.writeheader()
    writer.writerows(young_tweets)

# Print the filtered tweets
# with open("sample1.csv", "r", encoding="utf-8") as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)
