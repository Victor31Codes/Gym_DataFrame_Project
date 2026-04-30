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

#We are gonna get the specific value of the membership_type using the member_id with the get() function
mem = df_gym_attendance['membership_type']
member_id = df_gym_attendance["member_id"]
annual_membership = mem.get(member_id[51])
print(df_gym_attendance)
print(annual_membership)

#iloc and loc usage on the dataframe

first_row = df_gym_attendance.iloc[0]
print("Accessing to the first info on the DataFrame\n", first_row)#This is with iloc

fifth_row = df_gym_attendance.loc[5]
print("Accessing to the first info on the DataFrame\n", fifth_row)#This is with loc

row_0_to_5 = df_gym_attendance.iloc[:6]
print("Accessing to the row 0 to 5 info on the DataFrame\n", row_0_to_5)#This is with iloc

row_0_to_5 = df_gym_attendance.loc[:5]
print("Accessing to the row 0 to 5 info on the DataFrame\n", row_0_to_5)#This is with loc

cardio_info = df_gym_attendance.loc[:,['member_id','workout_type']]
print("We are gonna filter the all rows just for two columns\n",cardio_info)


#Identify the nulls on the DataFrame
checking_nulls = df_gym_attendance.isna().sum()
print("The columns that are null are the following ones:\n", checking_nulls)

#Refilling with mean on the null spaces (there is no null spaces)
mean_calories_burned = df_gym_attendance["calories_burned"].mean()
refill_mean_spaces = df_gym_attendance["calories_burned"].fillna(median_calories_burned)
print("The new column calories burned with the filled spaces with the mean\n", refill_mean_spaces)


#Creating new columns with new values
print(df_gym_attendance.info())

df_gym_attendance['visit_date'] = pd.to_datetime(df_gym_attendance['visit_date'])
print(df_gym_attendance.info())

df_gym_attendance['calories_per_min'] = df_gym_attendance['calories_burned'] / df_gym_attendance['workout_duration_minutes']
print(df_gym_attendance)

df_gym_attendance['intensity'] = df_gym_attendance['calories_burned'].apply(lambda x: 'Low' if x < 200 else 'Medium' if x < 400 else 'High')
print(df_gym_attendance)

max_cal = df_gym_attendance['calories_burned'].max()
df_gym_attendance['performance_pct'] = (df_gym_attendance['calories_burned'] / max_cal) * 100
print(df_gym_attendance)