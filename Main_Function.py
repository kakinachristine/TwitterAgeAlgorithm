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
with open("Relations.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        name = row.get("Name", "")
        username = row.get("Username", "")
        date = row.get("Date_Posted", "")
        tweet = row.get("Tweet", "")
        reply_count = row.get("Reply_Count", "")
        retweet_count = row.get("Retweet_Count", "")
        like_count = row.get("Like_Count", "")
        relations = row.get("Relations", "")
        tweets.append({
            "Name": name,
            "Username": username,
            "Date_Posted": date,
            "Tweet": tweet,
            "Reply_Count": reply_count,
            "Retweet_Count": retweet_count,
            "Like_Count": like_count,
            "Relations": relations
        })

young_tweets = []
for tweet in tweets:
    if is_young_person(tweet):
        young_tweets.append(tweet)

columns = ["Name", "Username", "Date_Posted", "Tweet", "Reply_Count", "Retweet_Count", "Like_Count", "Relations"]

with open("sample.csv", "w", encoding="utf-8", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=columns)
    writer.writeheader()
    writer.writerows(young_tweets)
