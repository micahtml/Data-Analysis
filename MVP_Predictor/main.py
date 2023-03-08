import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.metrics import accuracy_score

# Step 1: Data Collection
url = 'https://www.reference-basketball.com/stats/players'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Extract the required data from the webpage
table = soup.find('table')
data = []
headers = []
for row in table.find_all('tr'):
    cells = row.find_all('td')
    if len(cells) > 0:
        data.append([cell.text.strip() for cell in cells])
    else:
        headers = [cell.text.strip() for cell in row.find_all('th')]

# Convert the extracted data into a pandas dataframe
data = pd.DataFrame(data, columns=headers)

# Step 2: Data Cleaning and Preprocessing
# Clean and preprocess the data as needed
# For example, convert string columns to numeric
numeric_cols = ['points', 'rebounds', 'assists',
                'free_throws_made', 'games_played', 'minutes_played']
for col in numeric_cols:
    data[col] = pd.to_numeric(data[col], errors='coerce')
data.dropna(inplace=True)

# Step 3: Exploratory Data Analysis
# Use seaborn and matplotlib to create visualizations of the data
sns.pairplot(data[numeric_cols])
plt.show()

# Step 4: Feature Selection
# Select the most relevant features for predicting the MVP award winner
selected_features = ['points', 'rebounds', 'assists', 'free_throws_made', 'games_played', 'minutes_played']
X = data[selected_features]
y = data['MVP']

# Step 5: Model Training
# Train a linear regression model on the selected features
model = LinearRegression()
model.fit(X, y)

# Step 6: Model Evaluation
# Evaluate the performance of the model using accuracy_score or other relevant metrics
y_pred = model.predict(X)
accuracy = accuracy_score(y, y_pred.round())
print('Accuracy:', accuracy)

# Step 7: Model Deployment
# Deploy the model to make predictions on new data
new_data = pd.read_csv('new_data.csv')
X_new = new_data[selected_features]
y_pred = model.predict(X_new)
# Output the predicted MVP award winner
print('Predicted MVP:', y_pred[0])
