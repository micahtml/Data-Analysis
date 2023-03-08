import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Define the URL for the NBA season stat leaders data
url = 'https://www.basketball-reference.com/leagues/NBA_2023_totals.html'

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

# Select the top 5 MVP candidates based on points, rebounds, and assists per game
df['PPG'] = df['PTS'] / df['G']
df['RPG'] = df['TRB'] / df['G']
df['APG'] = df['AST'] / df['G']
mvp_df = df[['Player', 'Pos', 'Age', 'Tm', 'PPG', 'RPG', 'APG']
            ].sort_values(['PPG', 'RPG', 'APG'], ascending=False).head(5)

# Print the top 5 MVP candidates
print('Top 5 MVP Candidates in NBA 2023 Season')
print(mvp_df)

# Create a bar chart of the top 5 MVP candidates
sns.set(style='whitegrid')
sns.barplot(x='Player', y='value', hue='variable', data=pd.melt(
    mvp_df[['Player', 'PPG', 'RPG', 'APG']], id_vars='Player'), palette='deep')
plt.title('Top 5 MVP Candidates in NBA 2023 Season')
plt.xlabel('Player')
plt.ylabel('Value')
plt.show()
