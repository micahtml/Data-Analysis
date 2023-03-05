import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import scipy.stats as stats

# Import the COVID-19 dataset from John Hopkins University
url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/' \
    'csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'
df = pd.read_csv(url)

# Clean and preprocess the data
df.dropna(inplace=True)
df = df.groupby(['Country/Region']).sum()

# Accommodate for the United States as a country
us_data = df.loc['US']
us_data.index = pd.to_datetime(us_data.index)
us_data = us_data.resample('D').sum().fillna(method='ffill')
df.drop('US', inplace=True)
df.loc['United States'] = us_data

# Perform exploratory data analysis
df_total = df.iloc[:, -1].sort_values(ascending=False)
df_total.plot(kind='bar', figsize=(15, 5))
plt.title('Total confirmed cases by country')
plt.xlabel('Country')
plt.ylabel('Confirmed cases')
plt.show()

# Perform statistical analysis
country1 = df.loc['Italy']
country2 = df.loc['United States']
t, p = stats.ttest_ind(country1, country2)
print('t-statistic:', t)
print('p-value:', p)

# Communicate your findings
fig = px.choropleth(df_total.reset_index(), locations='Country/Region', locationmode='country names',
                    color=df_total.values, hover_name='Country/Region', color_continuous_scale='Reds',
                    title='Total confirmed cases by country')
fig.show()
