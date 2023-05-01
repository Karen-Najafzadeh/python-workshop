# first calculate the Duration/Pulse ratio and add it as a column to the DataFrame with the name 'ratio', then find the row that corresponds to the largest value.
import pandas as pd

df = pd.read_csv('data.csv')

Ratio = []
for i in df.index :
  Ratio.append((df.loc[i , 'Duration']/df.loc[i,'Pulse']))

df["ratio"] = Ratio

print(df.iloc[df[['ratio']].idxmax()])