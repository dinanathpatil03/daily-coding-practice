import pandas as pd
from io import StringIO
# Converted JSON string to DataFrame
Data = '{"employee_name": "James", "email": "james@gmail.com", "job_profile": [{"title1":"Team Lead", "title2":"Sr. Developer"}]}'
df = pd.read_json(StringIO(Data))
print(df)
# converted String to DataFrame
print("Data Frame", df.to_json(orient='index'))
print("Data Frame", df.to_json(orient='records'))


df=pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data",header=None)
print(df.head())

df.to_csv("wine.csv")
