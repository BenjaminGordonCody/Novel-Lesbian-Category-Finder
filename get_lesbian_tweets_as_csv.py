import snscrape.modules.twitter as sntwitter
import pandas as pd
from datetime import date, timedelta

# # Creating list to append tweet data to
tweets_list2 = []

# Using TwitterSearchScraper to scrape data and append tweets to list
search_term = '"lesbian"'
negative_terms = "-xxx -porn -erotic"


def yesterday():
    day = timedelta(days=1)
    today = date.today()
    yesterday = today - day
    return yesterday


string = f"{search_term} {negative_terms} since:{yesterday()}"

for i, tweet in enumerate(sntwitter.TwitterSearchScraper('lesbian since').get_items()):
    if i > 1000:
        break
    tweets_list2.append(
        [tweet.date, tweet.id, tweet.content, tweet.user.username])

# Creating a dataframe from the tweets list above
tweets_df2 = pd.DataFrame(tweets_list2, columns=[
                          'Datetime', 'Tweet Id', 'Text', 'Username'])

tweets_df2.to_csv(f"{date.today()}.csv")
