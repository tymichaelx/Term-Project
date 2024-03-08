
import pandas as pd

pd.set_option('display.max_columns', 10000)
pd.set_option('display.max_rows', 10000)

csv = pd.read_csv('Projectdata.csv')
courses_csv = pd.read_csv('ProjectData Courses.txt', sep='\t')

print(csv.head())
print(csv.info())

# Remove duplicates and remove missing/null values
duplicates = csv[csv.duplicated()]
null_rows = csv[csv.isnull().any(axis=1)]

print(duplicates)
print(null_rows)

csv = csv.dropna()
csv = csv.drop_duplicates()

# Export clean data to csv
csv.to_csv('cleaned_Projectdata.csv', index=False)

df = pd.read_csv('cleaned_Projectdata.csv')
print(df.info())

csv_file = 'cleaned_Projectdata.csv'
df = pd.read_csv(csv_file)

# Print all unique student names, for manual scanning of possible typos, and abbreviations
print("Unique student names:")
print(df['Student name'].unique())

print(df['coursename'].unique())

course_names = []

for c in df['coursename']:
    if c not in df['coursename']:
        course_names.append(c)

print(course_names)