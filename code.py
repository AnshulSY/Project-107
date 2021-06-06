import pandas as pd 
import csv
import plotly.graph_objects as go
import statistics

df = pd.read_csv(r"data.csv")
a = df.groupby("level")["attempt"].mean()
print(a)
fig = go.Figure(go.Bar(x=a,y=['level1','level2','level3','level4'],orientation='h'))
fig.show()