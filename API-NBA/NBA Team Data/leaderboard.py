import pandas as pd
import matplotlib.pyplot as plt

# Load the NBA team data
df = pd.read_csv('nba_team_data.csv')

# Create a dictionary of statistical categories and the corresponding DataFrame columns
stats_dict = {
    'Points Per Game': 'Points Per Game',
    'Assists Per Game': 'Assists Per Game',
    'Rebounds Per Game': 'Rebounds Per Game',
    'Steals Per Game': 'Steals Per Game',
    'Blocks Per Game': 'Blocks Per Game'
}

# Iterate over the statistical categories and create a bar chart showing the top player for each category
for stat_name, stat_col in stats_dict.items():
    # Sort the DataFrame by the statistical column in descending order
    sorted_df = df.sort_values(by=stat_col, ascending=False)

    # Create a bar chart of the top player for the statistical category
    plt.bar(sorted_df['Team'], sorted_df[stat_col])
    plt.title(stat_name)
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()
