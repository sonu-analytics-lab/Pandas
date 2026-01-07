import pandas as pd

df = pd.DataFrame({
    "OrderDate": ["2024-01-10", "2024-02-15", "2024-03-20"],
    "Sales": [5000, 7000, 6000]
})

# Convert to datetime

# df["OrderDate"] = pd.to_datetime(df["OrderDate"])
# print(df)

# 🔹 Step 2: Extract Date Parts (Very Common)

# df["Year"] = df["OrderDate"].dt.year
print(df)
#

# df["Year"] = df["OrderDate"].dt.year
# df["Month"] = df["OrderDate"].dt.month
# df["MonthName"] = df["OrderDate"].dt.strftime("%B")
# df["Day"] = df["OrderDate"].dt.day
# df["WeekDay"] = df["OrderDate"].dt.day_name()
