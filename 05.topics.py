'''
1.  how big  is your data
2. what are name of the columns
shapre and columns  
'''
import pandas as pd

data = {
    "Name": ["Ram", "Shyam", "Sonu", "Dhanshyam", "Aditi", "Jagdish", "Raj", "Simran"],
    "Age": [23, 27, 26, 34, 23, 28, 22, 19],
    "Salary": [50000, 20000, 13000, 43000, 27000, 47000, 34000, 20000],
    "Performance Score": [85, 90, 78, 92, 88, 95, 80, 90],
}

df = pd.DataFrame(data)
print(f"shape : {df.shape}")
print(f"Columns : {df.columns}")
