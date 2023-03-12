import pandas as pd
import requests
from bs4 import BeautifulSoup

url = 'https://www.basketball-reference.com/leagues/NBA_2023_per_game.html'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

table = soup.find('table', {'id': 'per_game_stats'})
headers = [th.text for th in table.select('tr th')]
rows = [[td.text for td in row.select('td')]
        for row in table.select('tr + tr')]

# Convert to DataFrame

df = pd.DataFrame(rows, columns=headers)