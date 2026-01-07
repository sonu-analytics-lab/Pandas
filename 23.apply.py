import pandas as pd

df = pd.DataFrame({
    "Name": ["Sonu", "Amit", "Rahul"],
    "Salary": [50000, 60000, 55000]
})

# df["Salary"] = df["Salary"].apply(lambda x: x + 5000)
# df["Salary"] = df["Salary"]+5000


df["Category"] = df["Salary"].apply(
    lambda x: "High" if x >= 55000 else "Low")

print(df)
