import pandas as pd

# data fetching throw csv file
df = pd.read_csv("data.csv")

# fetching first 5 rows
print(df.head(5))

# fetching last 5 rows
print(df.tail(5))

# entire statics
print(df.describe())

# data types for rows
print(df.dtypes)

# isnull()
print(df.isnull().any(axis=1))
print(df.isnull().any())
print(df.isnull().sum())

# missing values replaced with 0
print(df.fillna(0))

# rename column in the data
df = df.rename(columns={"Date": "Sales Date"})
replace = df.rename(columns={"Sales Date": "Sales-Date"})
df = df.rename(columns={"Sales Date": "Sales-Date"})
print(replace.head())
print(df.head())

# change datatypes
df["Value_new"]=df["Value"].fillna(df["Value"].mean()).astype(int)
print(df.head())

# using apply()
df["Value_new"] = df["Value"].apply(lambda x:x*2)
print(df.head())

# Data Aggregating and Grouping
group_mean = df.groupby("Product")["Value"].mean()
print(group_mean)
group_sum = df.groupby(["Product", "Region"])["Value"].sum()
print(group_sum)
group_aggregate = df.groupby("Region")["Value"].agg(["mean", "sum", "count"])
print(group_aggregate)