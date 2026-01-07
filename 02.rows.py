import pandas as pd
df = pd.read_json("sample_Data.json")

print("Display first 10 rows")
print(df.head())

print("Display first 10 rows of last")
print(df.tail())
