import pandas as pd

df = pd.read_csv("nba.csv", index_col= 'Name', usecols=['Name','Team', 'Salary'])

print(df.head(5))