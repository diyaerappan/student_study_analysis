
import pandas as pd
import matplotlib.pyplot as plt

# Sample student dataset
data = {
    "Student": ["Asha", "Rahul", "Diya", "Kiran", "Meera",
                "Arjun", "Priya", "Rohan", "Anu", "Vikram"],
    "Study_Hours": [2, 3, 5, 1, 6, 4, 7, 2, 5, 3],
    "Attendance": [70, 75, 85, 60, 95, 80, 98, 65, 90, 78],
    "Marks": [45, 55, 72, 35, 88, 68, 95, 42, 80, 60]
}

df = pd.DataFrame(data)

# Calculate statistics
average_marks = df["Marks"].mean()
pass_mark = 40
passed = (df["Marks"] >= pass_mark).sum()
pass_percentage = passed / len(df) * 100

top_student = df.loc[df["Marks"].idxmax()]

print("===== STUDENT STUDY ANALYSIS =====")
print(df.to_string(index=False))

print("\n===== SUMMARY =====")
print(f"Total students: {len(df)}")
print(f"Average marks: {average_marks:.2f}")
print(f"Students passed: {passed}")
print(f"Pass percentage: {pass_percentage:.1f}%")
print(
    f"Top student: {top_student['Student']} "
    f"with {top_student['Marks']} marks"
)

# Correlation between study hours and marks
correlation = df["Study_Hours"].corr(df["Marks"])
print(f"Study hours and marks correlation: {correlation:.2f}")

# Visualize study hours vs marks
plt.figure(figsize=(8, 5))
plt.scatter(df["Study_Hours"], df["Marks"])
plt.title("Study Hours vs Exam Marks")
plt.xlabel("Study Hours per Day")
plt.ylabel("Exam Marks")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("study_hours_vs_marks.png")
plt.show()

# Export dataset
df.to_csv("student_study_data.csv", index=False)

print("\nCSV dataset saved successfully!")
print("Graph saved as study_hours_vs_marks.png")
