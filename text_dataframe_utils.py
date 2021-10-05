"""
These are functions for creating and interacting with dataframes containing 
strings
"""

# imports
from ntpath import join
import pandas as pd
import glob
import os
import datetime


def multiple_csv_to_single_dataframe(folder):
    """Takes the name of a folder as a string. Combines .csv contents to
    single df. Using raw string (ie prefixing string wtih 'r') can solve
    Unicode issues"""
    joined_files = os.path.join(folder, "*.csv")
    globfiles = glob.glob(joined_files)
    df = pd.concat(map(pd.read_csv, globfiles), ignore_index=True)
    return df


if __name__ == "__main__":
    df = multiple_csv_to_single_dataframe(
        r"C:\Users\Benjamin\Documents\GitHub\Novel-Lesbian-Category-Finder")
    df.to_csv(f"all_lesbian_tweets_{datetime.date.today()}.csv")
