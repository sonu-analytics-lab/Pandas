# sorting
# sorting data 1 column sor_values()
# df.sort_values(by="Column Name",True/False, inplace = True)

import pandas as pd

data = {
    "Name": ['Arun', 'Varun', 'Karan'],
    "Age": [10, 20, 30],
    "Salary": [10000, 8000, 7000]
}

df = pd.DataFrame(data)
df.sort_values(by=["Age", "Salary"], ascending=[True, False], inplace=True)
print(df)
