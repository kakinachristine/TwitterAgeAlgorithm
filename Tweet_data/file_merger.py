import pandas as pd


# merging family

df1 = pd.read_csv('../junk_file/Family1.csv')
df2 = pd.read_csv('../junk_file/Family2.csv')
df3 = pd.read_csv('../junk_file/Family3.csv')
df4 = pd.read_csv('../junk_file/Family4.csv')
df5 = pd.read_csv('../junk_file/Family5.csv')

family_df = pd.concat([df1, df2, df3, df4, df5], ignore_index=True)

# Assuming you want to change the column headers to ['Column1', 'Column2', 'Column3', 'Column4', 'Column5']
family_df.columns = ['Name', 'Username', 'Date_Posted', 'Tweet', 'Reply_Count', 'Retweet_Count', 'Like_Count']
# Add the 'relations' column and fill it with 'family'
family_df['Relations'] = 'family'
print(family_df)

family_df.to_csv('family.csv', index=False)


# merging love

df1 = pd.read_csv('../junk_file/LoveOne.csv')
df2 = pd.read_csv('../junk_file/Love2.csv')
df3 = pd.read_csv('../junk_file/Love3.csv')
df4 = pd.read_csv('../junk_file/Love4.csv')
df5 = pd.read_csv('../junk_file/Love5.csv')
df6 = pd.read_csv('../junk_file/Love6 (1).csv')
df7 = pd.read_csv('../junk_file/Love7.csv')
df8 = pd.read_csv('../junk_file/Love8.csv')
df9 = pd.read_csv('../junk_file/Love9.csv')

love_df = pd.concat([df1, df2, df3, df4, df5, df6, df7, df8, df9], ignore_index=True)

# Assuming you want to change the column headers to ['Column1', 'Column2', 'Column3', 'Column4', 'Column5']
love_df.columns = ['Name', 'Username', 'Date_Posted', 'Tweet', 'Reply_Count', 'Retweet_Count', 'Like_Count']
# Add the 'relations' column and fill it with 'family'
love_df['Relations'] = 'love'
print(love_df)

love_df.to_csv('love.csv', index=False)


# merging friends

df1 = pd.read_csv('../junk_file/FriendshipOne.csv')
df2 = pd.read_csv('../junk_file/FriendshipTwo.csv')
df3 = pd.read_csv('../junk_file/FriendshipThree.csv')
df4 = pd.read_csv('../junk_file/FriendshipFour.csv')
df5 = pd.read_csv('../junk_file/FriendshipFive.csv')
df6 = pd.read_csv('../junk_file/FriendshipSix.csv')
df7 = pd.read_csv('../junk_file/FriendshipSeven.csv')

friends_df = pd.concat([df1, df2, df3, df4, df5, df6, df7], ignore_index=True)

# Assuming you want to change the column headers to ['Column1', 'Column2', 'Column3', 'Column4', 'Column5']
friends_df.columns = ['Name', 'Username', 'Date_Posted', 'Tweet', 'Reply_Count', 'Retweet_Count', 'Like_Count']
# Add the 'relations' column and fill it with 'family'
friends_df['Relations'] = 'friendship'
print(friends_df)
friends_df.to_csv('friends.csv', index=False)



# merging all relations

df1 = pd.read_csv('friends.csv')
df2 = pd.read_csv('love.csv')
df3 = pd.read_csv('family.csv')

all_df = pd.concat([df1, df2, df3], ignore_index=True)
all_df.to_csv('Relations.csv', index=False)