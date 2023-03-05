import matplotlib.pyplot as plt
import pandas as pd

url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/' \
    'csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'
df = pd.read_csv(url)

# drop rows with missing data
df.dropna(inplace=True)

# aggregate the data at the country level
df = df.groupby(['United States']).sum()

# plot the total number of confirmed cases by country
df_total = df.iloc[:, -1].sort_values(ascending=False)
df_total.plot(kind='bar', figsize=(15, 5))
plt.title('Total confirmed cases by country')
plt.xlabel('Country')
plt.ylabel('Confirmed cases')
plt.show()
