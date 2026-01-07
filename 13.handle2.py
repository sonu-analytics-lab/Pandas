# df.fillna(0, inplace=True)

import pandas as pd

data = {
    "Name": ["Ram", None, "Sonu", "Dhanshyam", "Aditi", "Jagdish", "Raj", "Simran"],
    "Age": [23, None, 26, 34, 23, 28, 22, 19],
    "Salary": [50000, None, 13000, 43000, 27000, 47000, 34000, 20000],
    "Performance Score": [85, None, 78, 92, 88, 95, 80, 90],
}

df = pd.DataFrame(data)
print(df)

# Finfilling the missing values in the column

# df.fillna(0, inplace=True)

# Filling the mean value in the column

df["Age"].fillna(df["Age"].mean(), inplace=True)  # mean age
df["Salary"].fillna(df["Salary"].mean(), inplace=True)  # mean Salary
df["Performance Score"].fillna(df["Performance Score"].mean(), inplace=True)

print(df)
