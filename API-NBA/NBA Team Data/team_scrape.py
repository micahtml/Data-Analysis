import pandas as pd
from sportsipy.nba.teams import Teams

# Collect team data: Use the Teams class from the API client library to collect NBA team data. For example, the following code will collect team data for the 2021-2022 season:
teams = Teams(year='2022')

# Save the data: Once you've collected the team data, you can save it to a file for later analysis. For example, you could save the data to a CSV file using the pandas library:
data = []
for team in teams:
    data.append({
        'Team': team.name,
        'Wins': team.wins,
        'Losses': team.losses,
        'Win Percentage': team.win_loss_percentage,
        'Points Per Game': team.points_per_game,
        'Assists Per Game': team.assists_per_game,
        'Rebounds Per Game': team.rebounds_per_game
    })

df = pd.DataFrame(data)
df.to_csv('nba_team_data.csv', index=False)

# Remove duplicates: Check for and remove any duplicate records in your dataset, if any exist. This can be done using the drop_duplicates() method in pandas:
df = df.drop_duplicates()

# Handle missing values: Check for any missing or null values in your dataset and decide how to handle them. Depending on the situation, you could either fill in missing values with a default value or drop records with missing values. This can be done using the fillna() and dropna() methods in pandas:

# fill missing values with 0
df = df.fillna(0)

# drop records with missing values
df = df.dropna()
