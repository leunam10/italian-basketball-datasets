# italian-basketball-datasets

This repository contains datasets (in CSV format) with statistics from the Italian LBA (Lega Basket A) championship. The datasets have been divided into two categories:

- Originals: The raw datasets as downloaded, located in the _originals_ folder.
- Finals: The cleaned and manipulated datasets, located in the _finals_ folder. These datasets are ready for direct use in statistical analysis.

This repository contains some datasets (as csv files) with the statistics of the italian LBA (Lega Basket A) championship.
In the _originals_ folder it is possible to find the datasets as downloaded.
In the _finals_ folder it is possible to find the datasets manipulated: ideally these datasets can be used directly for statistical analysis.

The data for the teams and players cover the seasons from from 2003-2004 to 2023-2024.

The dataset _teams_playoff_final_winner_1987-88_2023-24_, located in the _originals_ folder, contains detailed information for each team from the 1987 to 2023 seasons. It includes whether a team qualified for the playoffs, reached the playoff final, and if they ultimately won the championship. This file it is merged with the team statistcs to obtain a single dataset with all the information for the teams.

## Datasets
### Players Dataset
The cleaned and manipulated players datasets have the following headers:
__Player	MVP	Team	GP	MPG	PPG	FGM	FGA	FG%	3PM	3PA	3P%	FTM	FTA	FT%	ORB	DRB	RPG	APG	SPG	BPG	TOV	PF__

- Player: Name of the player.
- MVP: Whether the player was the MVP (Most Valuable Player) of the regular season.
- Team: The name of the team where the player played that season.
- GP: Number of games played.
- MPG: Minutes per game.
- PPG: Points per game.
- FGM: Field goals made.
- FGA: Field goals attempted.
- FG%: Field goal percentage.
- 3PM: Three-point field goals made.
- 3PA: Three-point field goals attempted.
- 3P%: Three-point field goal percentage.
- FTM: Free throws made.
- FTA: Free throws attempted.
- FT%: Free throw percentage.
- ORB: Offensive rebounds.
- DRB: Defensive rebounds.
- RPG: Rebounds per game.
- APG: Assists per game.
- SPG: Steals per game.
- BPG: Blocks per game.
- TOV: Turnovers.
- PF: Personal fouls

### Teams Dataset
The cleaned and manipulated team datasets have the following headers:
** Team	Year Playoff Finalist Winner GP	MPG	PPG	FGM	FGA	FG%	3PM	3PA	3P%	FTM	FTA	FT%	ORB	DRB	RPG	APG	SPG	BPG	TOV	PF **

- Team: The name of the team.
- Year: The season year.
- Playoff: Indicates if the team qualified for the playoffs.
- Finalist: Indicates if the team reached the playoff final.
- Winner: Indicates if the team won the playoff (and thus the championship).

The other statistcs are the same of the players dataset.

### Data Sources
All data have been collected from the following sources:

- [RealGM](https://basketball.realgm.com)
- [Wikipedia](https://it.wikipedia.org/)
