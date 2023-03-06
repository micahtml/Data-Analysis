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

# This code will load your NBA team data into a pandas DataFrame, create a dictionary mapping statistical categories to the corresponding DataFrame columns, and then iterate over the statistical categories to create a bar chart showing the top player for each category.

# The sort_values() method is used to sort the DataFrame by the statistical column in descending order, and then the bar() method is used to create a bar chart of the top player for the statistical category. The title() method is used to set the title of the chart, the xticks() method is used to rotate the x-axis labels for better visibility, and the show() method is used to display the chart.

# This code will create a bar chart for each statistical category, showing the team and player leading in that category. You can use these charts to gain insights into player performance and identify which players are leading in each statistical category.
