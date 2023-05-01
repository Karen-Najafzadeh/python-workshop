import pandas as pd

data = {"name":["BMW","KIA","Audi","volvo"],"model":[2015,2019,2022,2020],"country":["Germany","South Korea","Germany","Sweden"]}

df = pd.DataFrame(data)

#print(df['country'])

#print(df)
#print(df.loc[df['country']=='Germany'])
#print(df['country']=='Germany')
print(df)
#print(df.loc[0][2])
#print(df.iloc[0,2])
#print(df.iloc[1:4,0:3])
