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
filename_out = "teams_stats_1987-1988_2023-2024.csv"

stats_list = ["2pt", "3pt", "assist", 
              "blocks", "evaluation", "fouls_done", 
              "fouls_drawn", "ft", "lost", 
              "plus_minus", "points", "rebounds",
              "rebounds_def", "rebounds_off", "stolen",
              "total_shoots"]

stat_check = False

# reading the 'team_playoff_winner_1987-88_2023-24' csv file
team_playoff_winner_df = pd.read_csv(os.path.join(path_in, "teams_playoff_final_winner_1987-88_2023-24.csv"))

# create the empty final dataframe
final_df = pd.DataFrame()

count = 0
# cycle over all the teams csv files
for filename in os.listdir(path_in):
    if("teams" in filename and "playoff" not in filename):
        # reading csv file
        df = pd.read_csv(os.path.join(path_in, filename))

        # extract year from the Team column
        df['Year'] = df['Squadra'].apply(lambda x: re.search(r'\((\d{4})\)', x).group(1))
        df['Squadra'] = df['Squadra'].apply(lambda x: re.sub(r'\(\d{4}\)\s*', '', x))

        # drop not used columns
        df.drop(["#", "Giocate", "Min"], axis=1, inplace=True)

        # changing the position of the 'year' column
        col = df.pop('Year')
        df.insert(1, 'Year', col)

        for stat in stats_list:
            if(stat in filename):
                # rename columns
                if("vs" not in filename):
                    df.rename(columns={"Squadra": "Team", 
                                       "Totale": "Total_"+stat, 
                                       "Media" : "Avg_"+stat,
                                       "40 Min" : "Avg_"+stat+"_40min"}, inplace=True)
                if("vs" in filename):
                    df.rename(columns={"Squadra": "Team", 
                                       "Totale": "Total_"+stat+"_vs", 
                                       "Media" : "Avg_"+stat+"_vs",
                                       "40 Min" : "Avg_"+stat+"_vs_40min"}, inplace=True)

                break
        
        # creating the new dataframe
        if(count == 0):
            final_df["Team"] = df["Team"]
            final_df["Year"] = df["Year"]
        
        if("vs" in filename):
            final_df["Total_"+stat+"_vs"] = df["Total_"+stat+"_vs"]
            final_df["Avg_"+stat+"_vs"] = df["Avg_"+stat+"_vs"]
            final_df["Avg_"+stat+"_vs_40min"] = df["Avg_"+stat+"_vs_40min"]
        if("vs" not in filename):
            final_df["Total_"+stat] = df["Total_"+stat]
            final_df["Avg_"+stat] = df["Avg_"+stat]
            final_df["Avg_"+stat+"_40min"] = df["Avg_"+stat+"_40min"]

        count += 1


for year in team_playoff_winner_df["year"].unique():
    for team in team_playoff_winner_df["teams"].unique():

        print(team, year)
        print(final_df.loc[(final_df["Year"] == year) & (final_df["Team"] == team)])
        quit()

