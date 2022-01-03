import pandas as pd
text = "amit sheetal deepakhi Avyan, Ashita rajkumar pravesh"
list1 =[item for item in text.split()]
dict1 = {'Name': list1,
         'Age': [10,20,30,40,50,60]}
print(dict1)
df = pd.DataFrame(dict1)
print(df)


