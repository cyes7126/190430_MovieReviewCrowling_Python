import pandas as pd
df= pd.read_csv("./movieTest.csv")
point = df['point']
title=df['title']
report=df['report']

p1 = pd.concat([point, title, report],axis=1)
print(p1)