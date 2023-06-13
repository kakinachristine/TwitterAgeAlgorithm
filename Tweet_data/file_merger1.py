import pandas as pd


# merging family

df1 = pd.read_csv('../junk_file/fAmily6.csv')
df2 = pd.read_csv('../junk_file/fAmily7.csv')
df3 = pd.read_csv('../junk_file/fAmily8.csv')
df4 = pd.read_csv('../junk_file/fAmily9.csv')

family_df = pd.concat([df1, df2, df3, df4], ignore_index=True)

# Add the 'relations' column and fill it with 'family'
family_df['Relations'] = 'family'

print(family_df)

family_df.to_csv('familyship1.csv', index=False)


# merging love

df1 = pd.read_csv('../junk_file/love1.csv')

love_df = pd.concat([df1], ignore_index=True)

# Add the 'relations' column and fill it with 'family'
love_df['Relations'] = 'love'
print(love_df)

love_df.to_csv('loveship1.csv', index=False)


# merging friends

df1 = pd.read_csv('../junk_file/friends1.csv')
df2 = pd.read_csv('../junk_file/friends2.csv')
df3 = pd.read_csv('../junk_file/friends3.csv')

friends_df = pd.concat([df1, df2, df3], ignore_index=True)

# Add the 'relations' column and fill it with 'family'
friends_df['Relations'] = 'friendship'
print(friends_df)
friends_df.to_csv('friendship1.csv', index=False)



# merging all relations

df1 = pd.read_csv('friendship1.csv')
df2 = pd.read_csv('loveship1.csv')
df3 = pd.read_csv('familyship1.csv')

all_df = pd.concat([df1, df2, df3], ignore_index=True)
all_df.to_csv('Relations1.csv', index=False)