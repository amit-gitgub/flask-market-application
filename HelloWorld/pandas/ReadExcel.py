import pandas as pd

df = pd.read_csv("nba.csv", index_col='Name')

#print(df)
first = df.loc["Jae Crowder"]
second = df.loc["John Holland"]
#print(df.iloc[0])
dict = {'name':["aparna", "pankaj", "sudhir", "Geeku"],
        'degree': ["MBA", "BCA", "M.Tech", "MBA"],
        'score':[90, 40, 80, 98]}

df1 = pd.DataFrame(dict)
print(df1)

