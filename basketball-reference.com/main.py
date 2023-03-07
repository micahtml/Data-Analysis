import pandas as pd
import plotly.graph_objs as go

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
numeric_cols = ['G', 'MP', 'FG', 'FGA', '3P', '3PA', 'FT', 'FTA', 'ORB', 'DRB', 'TRB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS']
df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, errors='coerce')

# Calculate a new "MVP score" column
df['MVP score'] = (df['PTS'] / df['FGA']) + (df['TRB'] / df['DRB']) + (df['AST'] / df['TOV'])

# Select the top 5 MVP candidates and sort by MVP score in descending order
mvp_candidates = df[['Player', 'Pos', 'Age', 'Tm', 'PTS', 'TRB', 'AST', 'MVP score']].sort_values('MVP score', ascending=False).head(5)

# Create a bar chart of the top MVP candidates
fig = go.Figure(data=[
    go.Bar(name='Points', x=mvp_candidates['Player'], y=mvp_candidates['PTS']),
    go.Bar(name='Rebounds', x=mvp_candidates['Player'], y=mvp_candidates['TRB']),
    go.Bar(name='Assists', x=mvp_candidates['Player'], y=mvp_candidates['AST'])
])
fig.update_layout(
    barmode='group', title='Top 5 MVP Candidates in NBA 2022-23 Season')
fig.show()
