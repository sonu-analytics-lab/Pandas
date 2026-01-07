import pandas as pd

df = pd.DataFrame({
    "Name": ["Sonu", "Amit", "Rahul"],
    "Salary": [50000, 60000, 55000]
})

# # increase salary by10%
# df["Salary"] = df["Salary"].map(lambda x: x*1.10)
# print(df)


df["Grade"] = ["A", "B", "A"]

# Map Grade values
df["Grade"] = df["Grade"].map({"A": "Excellent", "B": "Good"})

print(df)
