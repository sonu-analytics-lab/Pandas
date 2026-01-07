import pandas as pd

data = {
    "Name": ["Ram", "Shyam", "Sonu", "Dhanshyam", "Aditi", "Jagdish", "Raj", "Simran"],
    "Age": [23, 27, 26, 34, 23, 28, 22, 19],
    "Salary": [50000, 20000, 13000, 43000, 27000, 47000, 34000, 20000],
    "Performance Score": [85, 90, 78, 92, 88, 95, 80, 90],
}

df = pd.DataFrame(data)
print(df)
# adding column via assignment df["ColumnName"] = datapoints

df["Bonus"] = df['Salary']*0.1
print(df)

# using insert() method df.insert(loc,"columname",some_data_points)
df.insert(0, "Employee_ID", [101, 102, 103, 104, 105, 106, 107, 108])
print(df)
