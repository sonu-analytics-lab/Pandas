import pandas as pd

data = {
    "Name": ["Ram", None, "Sonu", "Dhanshyam", "Aditi", "Jagdish", "Raj", "Simran"],
    "Age": [23, None, 26, 34, 23, 28, 22, 19],
    "Salary": [50000, None, 13000, 43000, 27000, 47000, 34000, 20000],
    "Performance Score": [85, None, 78, 92, 88, 95, 80, 90],
}

df = pd.DataFrame(data)
# print(df)

# Finding the missing values in the column

print(df.isnull().sum())
