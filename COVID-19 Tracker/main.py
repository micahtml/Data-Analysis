import plotly.express as px
import scipy.stats as stats
import matplotlib.pyplot as plt
import pandas as pd

url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/' \
    'csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'
df = pd.read_csv(url)

# drop rows with missing data
df.dropna(inplace=True)

# aggregate the data at the country level
df = df.groupby(['Country/region']).sum()

# plot the total number of confirmed cases by country
df_total = df.iloc[:, -1].sort_values(ascending=False)
df_total.plot(kind='bar', figsize=(15, 5))
plt.title('Total confirmed cases by country')
plt.xlabel('Country')
plt.ylabel('Confirmed cases')
plt.show()


# perform a t-test to compare the total number of confirmed cases between two countries
country1 = df.loc['US']
country2 = df.loc['China']
t, p = stats.ttest_ind(country1, country2)
print('t-statistic:', t)
print('p-value:', p)


# create a choropleth map to visualize the total number of confirmed cases by country
fig = px.choropleth(df_total.reset_index(), locations='Country/Region', locationmode='country names',
                    color=df_total.values, hover_name='Country/Region', color_continuous_scale='Reds',
                    title='Total confirmed cases by country')
fig.show()
