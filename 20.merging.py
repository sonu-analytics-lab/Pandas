# pd.merge(df1, df2, on="column_name", how="type of join")

import pandas as pd

df_customers = pd.DataFrame({
    "Customer_id": [1, 2, 3],
    "Name": ["Ramesh", "Suresh", "Kalpesh"]
})

# order dataframe
df_orders = pd.DataFrame({
    "Customer_id": [1, 2, 4],
    "Oreder_Amount": [240, 450, 350]
})


df_merged = pd.merge(df_customers, df_orders, on="Customer_id", how="inner")
print("Inner Join")
print(df_merged)

df_merged = pd.merge(df_customers, df_orders, on="Customer_id", how="outer")
print("Outer Join")
print(df_merged)

df_merged = pd.merge(df_customers, df_orders, on="Customer_id", how="left")
print("Left Join")
print(df_merged)

df_merged = pd.merge(df_customers, df_orders, on="Customer_id", how="right")
print("Right Join")
print(df_merged)
