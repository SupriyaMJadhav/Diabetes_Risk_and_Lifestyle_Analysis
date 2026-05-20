import pandas as pd
import numpy as np

df = pd.read_csv('diabetes_dataset.csv')

# Step 2: Handle Missing Values
# We fill empty alcohol consumption with 'None' as it's a categorical field
df['alcohol_consumption'] = df['alcohol_consumption'].fillna('None')

# Step 3: Feature Engineering - Creating 'BMI Category'
def categorize_bmi(bmi):
    if bmi < 18.5: return 'Underweight'
    elif 18.5 <= bmi < 25: return 'Normal'
    elif 25 <= bmi < 30: return 'Overweight'
    else: return 'Obese'

df['bmi_category'] = df['bmi'].apply(categorize_bmi)

# Step 4: Creating Age Groups
bins = [0, 30, 45, 60, 100]
labels = ['Young', 'Middle-Aged', 'Senior', 'Elderly']
df['age_group'] = pd.cut(df['age'], bins=bins, labels=labels)

# Step 5: Lifestyle Scoring (Combining habits into one score)
# Mapping text to numbers
activity_map = {'Sedentary': 0, 'Light': 1, 'Moderate': 2, 'Active': 3}
diet_map = {'Poor': 0, 'Fair': 1, 'Good': 2, 'Excellent': 3}

df['lifestyle_points'] = df['physical_activity'].map(activity_map) + df['diet_quality'].map(diet_map)

df['Visit_Date'] = pd.to_datetime(np.random.choice(
    pd.date_range('2024-01-01', '2026-05-14'), 
    len(df)
))

# 4. Save the final "Golden" dataset
#df.to_csv('diabetes_cleaned_final.csv', index=False)
#print("✅ Cleaning complete and Visit_Date column added!")

# Save the cleaned file for SQL and Power BI
df.to_csv('diabetes_cleaned_final.csv', index=False)