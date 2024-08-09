"""

This script is used to join all the 'players' datasets in one dataset. 
The new dataset will contains all the players for all the seasons from 
2003-04 to 2023-24 championships.
The new dataset will be saved into the 'originals' folder of this repository.

"""

import pandas as pd
import os
import sys

path = os.path.dirname(os.path.abspath("players_dataset_creation.py"))
path_in = os.path.join(path, "originals")
path_out = os.path.join(path, "finals")

# create the final dataframe that contains all the player dataframes
final_df = pd.DataFrame()

# cycle over all the players csv files in 'originals' folder
for filename in os.listdir(path_in):
    if("players" in filename):
        file_path = os.path.join(path_in, filename)

        # get the year from filename
        year = int(filename.split("_")[1])

        # read the csv file into a pandas df
        print(f"read dataset: {filename}")
        df = pd.read_csv(file_path)

        # drop the # column
        df.drop(["#"], axis=1, inplace=True)

        # adding column for the season year
        df["year"] = year
        # concatenate the dataframes
        final_df = pd.concat([final_df, df])

col = final_df.pop('year')
final_df.insert(1, 'year', col)
print("")
print(f"final datframe shape: {final_df.shape}")
print(final_df.head())
