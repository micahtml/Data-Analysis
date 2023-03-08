import plotly
import pandas as pd

# excel_file = 'malachi_data_tracker.xlsx'
# df = pd.read_excel(excel_file)
# print(df)

# size = [20, 40, 60, 80, 100, 80, 60, 40, 20, 40]

# import plotly.graph_objs as go

# data = [go.Scatter( x=df['Behavior'], y=df['Date'], mode='markers',
#         marker=dict(
#         size=size,
#         sizemode='area',
#         sizeref=2.*max(size)/(40.**2),
#         sizemin=4))]


# fig = go.Figure(data)
# fig.show()

import plotly.express as px

excel_file = 'malachi_data_tracker.xlsx'
df = pd.read_excel(excel_file)
print(df)

size = [20, 40, 60, 80, 100, 80, 60, 40, 20, 40]

df['Duration'] = df['Duration'].astype(float)
fig = px.scatter(df, x='Date', y='Behavior', color='Possible Trigger', hover_name='Weekday')
fig.show()
