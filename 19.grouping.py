
import pandas as pd

data = {
    "Name": ['Arun', 'Varun', 'Karan', "Arjun", "Vijay"],
    "Age": [30, 20, 30, 31, 47],
    "Salary": [10000, 8000, 7000, 16000, 13000]
}

df = pd.DataFrame(data)

# grouped = df.groupby("Age")["Salary"].sum()
grouped = df.groupby(["Age", "Name"])["Salary"].sum()

print(grouped)
