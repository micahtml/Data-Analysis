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
numeric_cols = ['G', 'MP', 'FG', 'FGA', '3P', '3PA', 'FT', 'FTA', 'ORB', 'DRB', 'TRB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS']
df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, errors='coerce')

# Select the top 5 MVP candidates and sort by points in descending order
mvp_candidates = df[['Player', 'PTS', 'TRB', 'AST']].sort_values('PTS', ascending=False).head(5)

# Create a bar chart of the top 5 MVP candidates' key stats
fig, ax = plt.subplots()
bar_width = 0.2
opacity = 0.8
index = [0, 1, 2]

pts = ax.bar(index, mvp_candidates['PTS'], bar_width, alpha=opacity, color='b', label='PTS')
trb = ax.bar(index + bar_width, mvp_candidates['TRB'], bar_width, alpha=opacity, color='g', label='TRB')
ast = ax.bar(index + 2*bar_width, mvp_candidates['AST'], bar_width, alpha=opacity, color='r', label='AST')

ax.set_xlabel('Player')
ax.set_ylabel('Stat')
ax.set_title('Top 5 MVP Candidates Key Stats')
ax.set_xticks(index + bar_width)
ax.set_xticklabels(mvp_candidates['Player'])
ax.legend()

plt.show()
