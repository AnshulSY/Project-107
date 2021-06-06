import pandas as pd 
import csv
import plotly.graph_objects as go 
import statistics

#reads data file
df = pd.read_csv(r"data.csv")

#filters student ID
studentId = df.loc[df["student_id"]=="TRL_abc"]

#takes mean of attempt for studentId TRL_abc
a = studentId.groupby("level")["attempt"].mean()
print(a)