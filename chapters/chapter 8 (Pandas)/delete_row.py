import pandas as pd

df = pd.read_csv("dirtydata.csv")

# for column in df:
#     for value in df[column]:
#         print(value)

for row in df.index:
    if df["Duration"][row] >= 60:
        # print(df["Duration"][row])
        # print(row)
        df.drop(row,inplace=True)

df.drop(columns = ["Duration","Date"], inplace=True)

# How to Add Rows to a Pandas DataFrame
# https://www.statology.org/pandas-add-row-to-dataframe/
print(df)