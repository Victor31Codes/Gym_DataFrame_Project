import pandas as pd

path = r'C:\Users\Manolo\OneDrive\Documentos\Gym_DataFrame_Project\daily_gym_attendance_workout_data.csv'
df_gym_attendance = pd.read_csv(path)

print(df_gym_attendance.head())

columns_names_gym_attendance = df_gym_attendance.columns
print("The columns for this DataFrame are:\n", columns_names_gym_attendance)

rows_gym_attendance, columns_gym_attendance = df_gym_attendance.shape
print("The rows number in this df is:",rows_gym_attendance)
print("The columns number in this df is:",columns_gym_attendance)

summary = df_gym_attendance.describe().head()
print("These is the summary of the columns in the df:\n", summary)

mean_age_gym_attendance = df_gym_attendance['age'].mean()
print("This is the age mean of the people that workout on the gym ",mean_age_gym_attendance)

median_calories_burned = df_gym_attendance['calories_burned'].median()
print("This is the median of the people that workout on the gym ",median_calories_burned)

sum_gym_attendance_calories_burned = df_gym_attendance["calories_burned"].sum()
print("The total sum of calories burned on the gym:",sum_gym_attendance_calories_burned)
count_gym_attendance = df_gym_attendance.count()
print("The total count of the values on gym attendance:",count_gym_attendance)

min_value = df_gym_attendance['age'].min()
print("The age of the youngest person training on the gym is:", min_value,"years old")

max_value = df_gym_attendance['workout_duration_minutes'].max()
print("The highest time that a person takes training in minutes is:", max_value,"minutes")

mem = df_gym_attendance['membership_type']
member_id = df_gym_attendance["member_id"]
annual_membership = mem.get(member_id)
print(df_gym_attendance)
print(annual_membership)


