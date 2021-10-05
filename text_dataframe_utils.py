"""
These are functions for creating and interacting with dataframes containing 
strings
"""

# imports
from ntpath import join
import pandas as pd
import glob
import os


def multiple_csv_to_single_dataframe(folder):
    """Takes the name of a folder that contains CSV, combines .csv contents
    to single df"""
    joined_files = os.path.join(folder, "*.csv")
    globfiles = glob.glob(joined_files)
    df = pd.concat(map(pd.read_csv, globfiles), ignore_index=True)
    print(df)


if __name__ == "__main__":
    multiple_csv_to_single_dataframe(
        r"C:\Users\Benjamin\Documents\GitHub\Novel-Lesbian-Category-Finder")
