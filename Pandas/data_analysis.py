import pandas as pd

df= pd.read_csv('Iris.csv')

print(df.head(8))

print(df.columns.tolist())

df.fillna(df.mean(numeric_only=True))
print(df)

df.dropna()
print(df)

df.groupby('Species')
print(df)

print(df.SepalLengthCm.mean())
print(df.SepalLengthCm.min())
print(df.SepalLengthCm.max())

