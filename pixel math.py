import pandas as pd
import plotly.graph_objects as py
import csv

df=pd.read_csv("data2.csv")
sdf=df.loc[df["student_id"]=="TRL_xsl"]
print(sdf)
print(sdf.groupby("level")["attempt"].mean())
#print(df.groupby("student_id").count())

fig=py.Figure(py.Scatter(x=sdf.groupby("level")["attempt"].mean(),y=["level1","level2","level3","level4"],orientation="h"))
fig.show()
