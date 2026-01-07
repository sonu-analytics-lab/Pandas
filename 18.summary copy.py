import pandas as pd

data = {
    "Name": ['Arun', 'Varun', 'Karan', "Arjun", "Vijay"],
    "Age": [10, 20, 30, 31, 47, 23],
    "Salary": [10000, 8000, 7000, 16000, 16000]
}

df = pd.DataFrame(data)

avg_salary = df["Salary"].mean()

print(avg_salary)
