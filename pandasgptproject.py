import pandas as pd

# Step 1: Create student data
data = {
    "Name": ["Rahul", "Anita", "Suresh", "Priya", "Amit"],
    "Maths": [78, 85, 45, 92, 60],
    "Science": [72, 88, 40, 95, 55],
    "English": [80, 90, 50, 85, 58]
}

# Step 2: Create DataFrame
df = pd.DataFrame(data)

# Step 3: Calculate Total and Average
df["Total"] = df[["Maths", "Science", "English"]].sum(axis=1)
df["Average"] = df["Total"] / 3

# Step 4: Assign Grades


def grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 50:
        return "C"
    else:
        return "Fail"


df["Grade"] = df["Average"].apply(grade)

# Step 5: Display all student data
print("Student Result Data:\n")
print(df)

# Step 6: Find Topper
topper = df.loc[df["Total"].idxmax()]
print("\nTopper:")
print(topper)

# Step 7: Find Failed Students
failed_students = df[df["Grade"] == "Fail"]
print("\nFailed Students:")
print(failed_students)

# Step 8: Save result to CSV file
df.to_csv("student_results.csv", index=False)
print("\nResults saved to student_results.csv")
