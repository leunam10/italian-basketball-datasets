"""

This script is used to create the csv file containin all the statistics for all the 
teams from 1987-88 to 2023-24 LBA championships. 
The final dataset is also joined with the 'team_playoff_final_winner_1987-88_2023-24' 
csv file containing information about the partecipants to the playoff, the two teams
that played the final playoff game and the team that won the season.

"""

import pandas as pd
import os, sys
import re

path = os.path.dirname(os.path.abspath("teams_dataset_creation.py"))
path_in = os.path.join(path, "originals")
path_out = os.path.join(path, "finals")
filename_out = "teams_stats_2003-2004_2023-2024.csv"

# create the empty final dataframe
final_df = pd.DataFrame()

# cycle over all the teams csv files
for filename in os.listdir(path_in):
    if("teams" in filename):
        # reading csv file
        df = pd.read_csv(os.path.join(path_in, filename))

        # create the final dataframe 
        final_df = pd.concat([final_df, df])


# changing the position of the 'year' column
col = final_df.pop('Year')
final_df.insert(1, 'Year', col)


print("")
print(f"final datframe shape: {final_df.shape}")
print(final_df.head())

print("")
print(f"saving final dataframe as csv file: {os.path.join(path_out, filename_out)}")
final_df.to_csv(os.path.join(path_out, filename_out), index=False)
