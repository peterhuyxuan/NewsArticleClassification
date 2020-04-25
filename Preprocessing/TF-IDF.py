import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import csv

df = pd.read_csv('training.csv')

vectorizer = TfidfVectorizer()

# give each word a tf-idf value
vectors = vectorizer.fit_transform(df['article_words'])

# get each article word as a feature
feature_names = vectorizer.get_feature_names()

dense = vectors.todense()

denselist = dense.tolist()

# turn the stuff into a datafram with the colunms as article words
df_tfidf = pd.DataFrame(denselist, columns=feature_names)

# append topic column

df_tfidf['topic'] = df['topic']


# encode categorical
cleanup_nums = {"topic": {"ARTS CULTURE ENTERTAINMENT": 1, "BIOGRAPHIES PERSONALITIES PEOPLE": 2, "DEFENCE": 3, "DOMESTIC MARKETS": 4,
                          "FOREX MARKETS": 5, "HEALTH": 6, "MONEY MARKETS": 7, "SCIENCE AND TECHNOLOGY": 8, "SHARE LISTINGS": 9, "SPORTS": 10}}


df_tfidf.replace(cleanup_nums, inplace=True)

# prepend article number column
art_no = df_tfidf['article_number']

df_art_no = pd.DataFrame(art_no)

df_art_no

df_art_no[df_tfidf.columns] = df_tfidf


df_full = df_art_no

########################

df = pd.read_csv('training.csv')

df2 = df[(df['article_number'].isin([1, 2]))]

print(df2)

vectorizer = TfidfVectorizer()

vectors = vectorizer.fit_transform(df2['article_words'])

feature_names = vectorizer.get_feature_names()

dense = vectors.todense()

denselist = dense.tolist()

df3 = pd.DataFrame(denselist, columns=feature_names)

df3['topic'] = df2['topic']

art_no = df2['article_number']

df_art_no = pd.DataFrame(art_no)

print(df_art_no)

df_art_no[df3.columns] = df3


cleanup_nums = {"topic": {"ARTS CULTURE ENTERTAINMENT": 1, "BIOGRAPHIES PERSONALITIES PEOPLE": 2, "DEFENCE": 3, "DOMESTIC MARKETS": 4,
                          "FOREX MARKETS": 5, "HEALTH": 6, "MONEY MARKETS": 7, "SCIENCE AND TECHNOLOGY": 8, "SHARE LISTINGS": 9, "SPORTS": 10}}

df_art_no.replace(cleanup_nums, inplace=True)

df_full = df_art_no

print(df_full)
