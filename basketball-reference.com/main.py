import pandas as pd
import matplotlib.pyplot as plt

# Define the URL for the NBA season stat leaders data
url = 'https://www.basketball-reference.com/leagues/NBA_2022_totals.html'

# Use pandas to read the HTML table into a DataFrame
df = pd.read_html(url)[0]

# Remove the "Rk" column
df.drop('Rk', axis=1, inplace=True)

# Rename the "Unnamed: 1" column to "Player"
df.rename(columns={'Unnamed: 1': 'Player'}, inplace=True)

# Remove the last 2 rows (total and league average)
df.drop(df.tail(2).index, inplace=True)

# Remove duplicates
df.drop_duplicates(inplace=True)

# Remove any rows where all columns are empty
df.dropna(how='all', inplace=True)

# Convert the relevant columns to numeric data type
numeric_cols = ['G', 'MP', 'FG', 'FGA', '3P', '3PA', 'FT', 'FTA',
                'ORB', 'DRB', 'TRB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS']
df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, errors='coerce')

# Select the top 10 scorers and sort by points in descending order
df = df[['Player', 'Pos', 'Age', 'Tm', 'PTS']].sort_values(
    'PTS', ascending=False).head(10)

# Create a bar chart of the top scorers
plt.bar(df['Player'], df['PTS'])
plt.title('Top 10 Scorers in NBA 2022 Season')
plt.xlabel('Player')
plt.ylabel('Total Points')
plt.show()

# Select the top performers in each major stat category
rebounds_leader = df[['Player', 'TRB']].sort_values(
    'TRB', ascending=False).iloc[0]
assists_leader = df[['Player', 'AST']].sort_values(
    'AST', ascending=False).iloc[0]
steals_leader = df[['Player', 'STL']].sort_values(
    'STL', ascending=False).iloc[0]
blocks_leader = df[['Player', 'BLK']].sort_values(
    'BLK', ascending=False).iloc[0]

# Create a bar chart of the rebounds leader
plt.bar(rebounds_leader['Player'], rebounds_leader['TRB'])
plt.title('Rebounds Leader in NBA 2022 Season')
plt.xlabel('Player')
plt.ylabel('Total Rebounds')
plt.show()

# Create a bar chart of the assists leader
plt.bar(assists_leader['Player'], assists_leader['AST'])
plt.title('Assists Leader in NBA 2022 Season')
plt.xlabel('Player')
plt.ylabel('Total Assists')
plt.show()

# Create a bar chart of the steals leader
plt.bar(steals_leader['Player'], steals_leader['STL'])
plt.title('Steals Leader in NBA 2022 Season')
plt.xlabel('Player')
plt.ylabel('Total Steals')
plt.show()

# Create a bar chart of the blocks leader
plt.bar(blocks_leader['Player'], blocks_leader['BLK'])
plt.title('Blocks Leader in NBA 2022 Season')
plt.xlabel('Player')
plt.ylabel('Total Blocks')
plt.show()
