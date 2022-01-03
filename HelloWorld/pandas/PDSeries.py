import pandas as pd

df = pd.read_csv("nba.csv", index_col= 'Name', usecols=['Name','Team', 'Salary'])

print(df.head(5))

#print(df['Name'])
sr = pd.Series(df['Name'])
df['Name'] = df['Name'].astype(str)

#print(df['Name'])

for index, row in df.iterrows():
    for data in row:
        if data =="Jordan Hill":
            #row.to_csv("Jordan_Hill.csv")
            print(type(row))
