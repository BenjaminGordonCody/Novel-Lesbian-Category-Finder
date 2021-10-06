"""This func retrieves 1000 tweets containing the word "lesbian" that have been 
made since yesterday"""

# imports
import snscrape.modules.twitter as sntwitter
import pandas as pd
from datetime import date, timedelta
from time import localtime

# # Creating list to append tweet data to
tweets_list2 = []

# define terms of search
search_term = "lesbian"
negative_terms = "-xxx -porn -erotic"


def yesterday():
    day = timedelta(days=1)
    today = date.today()
    yesterday = today - day
    return yesterday


string = f'+"{search_term}" {negative_terms} since:{yesterday()} -RT'

for i, tweet in enumerate(sntwitter.TwitterSearchScraper(string).get_items()):
    if i > 3:
        break
    tweets_list2.append(
        [tweet.date, tweet.id, tweet.content, tweet.user.username])

# Creating a dataframe from the tweets list above
tweets_df2 = pd.DataFrame(tweets_list2, columns=[
                          'Datetime', 'Tweet Id', 'Text', 'Username'])

tweets_df2.to_csv(f"{date.today()}_{localtime().tm_hour}.csv")
