from unittest.mock import inplace

import pandas as pd
df=pd.read_csv('Automobile.csv')
# col of the data and info about it
print(df.columns)
print("info about numerical col of data :\n",df.describe())
print("info about the data:\n",df.info())
# missing values=6 from col horsepower
print(df.isnull().sum())
df['horsepower'] = df['horsepower'].fillna(df['horsepower'].median())
# duplicate =none
print(df.duplicated().sum())
print('='*10)

