"""
These are functions for creating and interacting with dataframes containing 
strings
"""

# imports
from ntpath import join
import string as str_constants
import datetime

import pandas as pd
import glob
import os


def multiple_csv_to_single_dataframe(folder):
    """Takes the name of a folder as a string. Combines .csv contents to
    single df. Using raw string (ie prefixing string wtih 'r') can solve
    Unicode issues"""
    joined_files = os.path.join(folder, "*.csv")
    globfiles = glob.glob(joined_files)
    df = pd.concat(map(pd.read_csv, globfiles), ignore_index=True)
    return df


def remove_punctuation(string):
    for character in str_constants.punctuation:
        string = string.replace(character, '')
    return string


def index_of_search_term_in_string(string):
    """returns what it says if term is present, otherwise returns None"""
    pass


def count_word_occurences_around_search_term(df):
    """returns df. col 1 is every word that has buttressed the search term, 
    col 2 is how many times it has appeared"""
    pass


if __name__ == "__main__":
    df = multiple_csv_to_single_dataframe(
        r"C:\Users\Benjamin\Documents\GitHub\Novel-Lesbian-Category-Finder\Data")
    df.to_csv(f"all_lesbian_tweets_{datetime.date.today()}.csv")
