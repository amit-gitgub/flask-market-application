import pandas as pd

# Creating new dataframe
initial_data = {'First_name': ['Ram', 'Mohan', 'Tina', 'Jeetu', 'Meera'],
                'Last_name': ['Kumar', 'Sharma', 'Ali', 'Gandhi', 'Kumari'],
                'Marks': [12, 52, 36, 85, 55]}

df = pd.DataFrame(initial_data)
result = []
print(df)
for val in df['Marks']:
    if val >= 33:
        result.append("pass")

    elif val < 33:
        result.append("fail")


df["result"] = result

print(df)
