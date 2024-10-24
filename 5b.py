import pandas as pd

data={'usn': [1,2,3,4,5,6,7,8,9,10], 'Name': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']}

df=pd.DataFrame (data)

print(df.head())

print(df.tail())

print(df.head(2))

print(df.shape)

print(df.columns)

print(df.describe)

print(df.info())

print(df.iloc[1:6])

print(df.loc[1:6])

print(df.isnull().sum())

print(df.dtypes)
