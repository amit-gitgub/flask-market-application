import pandas as pd

data1 =  pd.Series([2,4,6,8], index=[0,1,2,3])
data2 = pd.Series([2,2,2], index=[0,1,2])

print(data1.__mul__(data2))