import pandas as pd

df=pd.read_csv(r"name.csv")

print(df)

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
