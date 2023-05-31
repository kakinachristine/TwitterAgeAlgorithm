# search queries

# topics
# search_query = "relationships with loved ones OR family OR friends OR dating OR breakups OR " \
#                "relationship milestones OR love languages OR long-distance relationships OR relationship goals" \
#                " OR communication OR conflict resolution OR online dating OR LGBTQ+ relationships OR relationship" \
#                " advice OR relationship humor OR intimacy and romance OR relationship self-care OR relationship" \
#                " red flags"



# hashtags
# search_query = "#love OR #relationships OR #romance OR #couplegoals OR #soulmate OR #truelove OR " \
#                "#relationshipgoals OR #happycouple OR #lovequotes OR #lovestory OR #friendship OR" \
#                # " #bestfriends OR #bffs OR #friendsforever OR #friendshipgoals OR #friendslikefamily OR" \
#                " #truefriends OR #friendshipquotes OR #friendshipday OR #squadgoals OR #family OR " \
#                "#familytime OR #familylove OR #familygoals OR #familyfirst OR #familyisforever OR" \
#                " #familymatters OR #familybonds OR #familymemories OR #familyquotes"


# FOR THE ALGORITHM

#######################emojis
# meme_keywords = ["😂", "❤️", "😍", "😭", "🙌", "🤔", "😊", "🙏", "🥺", "🤣", "🥰", "😒", "🤩", "🙈", "🤷‍♀️", "🔥", "😎", "🤪"]
# if any(keyword in tweet_content for keyword in meme_keywords):
#     return True

############################abbreviations and word patterns

# slang_patterns = ["omg", "lol", "bff", "brb", "idk", "tbh", "fyi", "smh", "tbt", "irl", "af", "yolo", "fomo", "imo", "ttyl", "nvm", "jk", "ikr", "hbu", "btw", "rn", "ftw", "irl", "fomo", "lmk", "ama", "tfw", "hbd", "ily", "imo", "yolo", "np", "ngl", "gtg", "rofl", "tgif", "wyd", "wcw"]
# if any(pattern in tweet_content.lower() for pattern in slang_patterns):
#     return True

##########################memes
# Check for memes
# meme_keywords = ["meme", "viral", "trending", "dank", "hilarious", "funny", "lmao", "rofl", "meme culture", "internet humor", "gifs", "vines", "reaction images", "pepe", "rickroll", "doge", "spongebob memes", "shitposting", "wojak", "expanding brain meme"]
# if any(keyword in tweet_content.lower() for keyword in meme_keywords):
#     return True


#######################words they use
# # Check for keywords in the tweet content
# content_keywords = ["school", "exam", "homework", "lit", "squad", "flex", "fomo", "gucci", "clout", "savage", "salty", "ghost", "extra", "mood", "basic", "vibes", "snack", "tea", "thirsty", "swag", "lituation", "woke", "bet", "fam", "yolo", "bae", "on fleek", "slay", "no cap", "goat", "dm", "ship", "tbt", "goals", "dope", "hella", "lurk", "shade", "triggered", "turn up", "snatched", "lit af"]
# tweet_content = tweet.get("content", "").lower()
# if any(keyword in tweet_content for keyword in content_keywords):
#     return True


#################social  activitism and justice
# # Check for Social Justice and Activism
# social_keywords = ["climate change", "equality", "intersectionality", "systemic racism", "lgbtq+ rights", "feminism", "black lives matter", "climate justice", "indigenous rights", "body positivity", "mental health awareness", "youth activism", "immigration rights", "human rights", "inclusivity", "anti-discrimination", "activism", "social equality", "gender equality", "environmental justice", "economic justice", "police brutality", "mass incarceration", "voting rights", "gun control", "reproductive rights", "disability rights", "transgender rights", "access to education", "income inequality", "healthcare access", "cultural appropriation", "racial profiling", "anti-hate speech", "digital privacy", "fair trade", "youth engagement", "community organizing", "peaceful protests"]
# if any(keyword in tweet_content.lower() for keyword in social_keywords):
#     return True


#################### couple goals in africa and global
# Check for mentions of influential individuals
# influencer_keywords = ["@celebrity", "@musician", "@athlete", "Beyoncé", "Jay-Z", "Prince Harry", "Meghan Markle", "David Beckham", "Victoria Beckham", "Kim Kardashian", "Kanye West", "John Legend", "Chrissy Teigen", "Barack Obama", "Michelle Obama", "Wizkid", "Tiwa Savage", "Diamond Platnumz", "Tanasha Donna", "Justin Bieber", "Hailey Baldwin", "Selena Gomez", "The Weeknd", "Ariana Grande", "Dalton Gomez", "Shawn Mendes", "Camila Cabello", "Zayn Malik", "Gigi Hadid", "Emma Chamberlain", "David Dobrik", "James Charles", "Liza Koshy", "Brent Rivera", "Lele Pons", "Davido", "Chioma"]
# if any(keyword in tweet_content for keyword in influencer_keywords):
#     return True




########################## a bit on profile
# Check for keywords in the user's profile description
# profile_keywords = ["teen", "student", "high school", "school", "university", "graduation", "youth", "gen z", "millennial", "emoji", "slang", "pop culture", "video games", "social media", "youth organization", "activism", "influencer", "content creator"]
# profile_description = tweet.get("description", "").lower()
# if any(keyword in profile_description for keyword in profile_keywords):
#     return True








