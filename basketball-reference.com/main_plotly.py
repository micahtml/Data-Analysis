import pandas as pd
import plotly.express as px

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

# Select the top 5 MVP candidates based on points, rebounds, and assists
df['MVP_Score'] = df['PTS'] + df['TRB'] + df['AST']
mvp_df = df[['Player', 'Pos', 'Age', 'Tm', 'PTS', 'TRB', 'AST',
             'MVP_Score']].sort_values('MVP_Score', ascending=False).head(5)

# Create a bar chart of the top 5 MVP candidates with their stats
fig = px.bar(mvp_df, x='Player', y=[
             'PTS', 'TRB', 'AST'], title='Top 5 MVP Candidates in NBA 2023 Season')
fig.update_layout(barmode='group')
fig.show()
