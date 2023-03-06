import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.basketball-reference.com/leagues/NBA_2022_leaders.html'

# Send an HTTP GET request to the webpage
response = requests.get(url)

# Parse the HTML using Beautiful Soup
soup = BeautifulSoup(response.content, 'html.parser')

# Find the table containing the NBA season stat leaders data
table = soup.find('table', {'id': 'stats'})

# Extract the column headers from the table
headers = [th.get_text() for th in table.find('thead').find_all('th')]

# Extract the data rows from the table
data_rows = table.find('tbody').find_all('tr')
rows = []
for row in data_rows:
    cols = row.find_all('td')
    cols = [col.get_text() for col in cols]
    rows.append(cols)

# Create a pandas DataFrame from the extracted data
df = pd.DataFrame(rows, columns=headers)
print(df.head())
