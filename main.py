import pandas as pd
import plotly_express as px


df = pd.read_excel("reward_data.xlsx")
df["Date"] = pd.to_datetime(df['Earned On'])

df = df.groupby('Date').size().reset_index(name='Count')

fig = px.line(df, "Date", "Count", line_shape='spline')
fig.show()