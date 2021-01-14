import time
import os

import pandas as pd
from pandas_ods_reader import read_ods

# load a sheet "reddit_post_per_day.ods" based on its index (1 based)
sheet_idx = 1
df_posts = read_ods("reddit_post_per_day.ods", sheet_idx)

df_posts['year'] = pd.DatetimeIndex(df_posts["date"]).year
df_posts['month'] = pd.DatetimeIndex(df_posts["date"]).month
df_posts['day'] = pd.DatetimeIndex(df_posts["date"]).day

# Gather Number of Daily Posts for 2019
df_posts_2019 = df_posts[df_posts["year"] == 2019]
filename = './données_projet_soleil/posts_per-day_2019.csv'
df_posts_2019.to_csv(filename)

# Gather Number of Daily Posts for 2020
df_posts_2020 = df_posts[df_posts["year"] == 2020]
filename = './données_projet_soleil/posts_Per_Day_2020.csv'
df_posts_2020.to_csv(filename)


# load a sheet "reddit_comments_per_day .ods" based on its index (1 based)
sheet_idx = 1
df_comments = read_ods("reddit_comments_per_day .ods", sheet_idx)

df_comments['year'] = pd.DatetimeIndex(df_comments["date"]).year
df_comments['month'] = pd.DatetimeIndex(df_comments["date"]).month
df_comments['day'] = pd.DatetimeIndex(df_comments["date"]).day

# Gather Number of Comments for 2019
df_comments_2019 = df_comments[df_comments["year"] == 2019]
filename = './données_projet_soleil/Comments_Per_Day_2019.csv'
df_comments_2019.to_csv(filename)

# Gather Number of Comments for 2020
df_comments_2020 = df_comments[df_comments["year"] == 2020]
filename = './données_projet_soleil/Comments_Per_Day_2020.csv'
df_comments_2020.to_csv(filename)

for i in (df_comments_2020, df_comments_2019, df_posts_2019, df_posts_2020):
    print (i.shape)
    print (i.info())
