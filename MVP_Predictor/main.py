import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.basketball-reference.com/leagues/NBA_2022_per_game.html'
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    table = soup.find('table')
    players_stats = pd.read_html(str(table))[0]
    players_stats.drop(players_stats.tail(1).index, inplace=True)
    header = table.find('thead').find_all('th')
    new_header = []
    for column in header:
        new_header.append(column.text)
    players_stats.columns = new_header
    players_stats = players_stats.drop(['Rk'], axis=1)
    players_stats['MVP'] = players_stats['Player'].apply(
        lambda x: 1 if '*' in x else 0)
    y = players_stats[['MVP']]
    X = players_stats[['PTS', 'AST', 'TRB', 'FT', 'G', 'MP']]
    X = X.apply(pd.to_numeric)
    y = y.apply(pd.to_numeric)
else:
    print('Error: Response code', response.status_code)
