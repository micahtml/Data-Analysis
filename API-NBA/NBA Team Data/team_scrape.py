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
