import pandas as pd

# region1
df_region1 = pd.DataFrame({
    "cust_id": [1, 2],
    "name": ["Gopal", "Raju"]
})

# region2
df_region2 = pd.DataFrame({
    "cust_id": [3, 4],
    "name": ["Shyam", "Baburao"]
})


# concatenation vertically  axis = 0

df_concat = pd.concat([df_region1, df_region2], ignore_index=True)
print(df_concat)


# concatenation horizontal  axis = 1

df_concat = pd.concat([df_region1, df_region2], axis=1, ignore_index=True)
print(df_concat)
