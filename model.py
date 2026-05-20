import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# 1. Load data
df = pd.read_csv('diabetes_cleaned_final.csv')

# 2. Select only NUMERIC columns for the model
# AI models cannot read text like "Female" or "Active" without extra steps
features = ['age', 'bmi', 'glucose_level', 'hba1c', 'blood_pressure', 'insulin']
X = df[features]
y = df['diabetes_outcome']

# 3. Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Initialize and Train
model = RandomForestClassifier()
model.fit(X_train, y_train)

# 5. Check if it worked
predictions = model.predict(X_test)
print(f"Model Training Complete. Accuracy: {accuracy_score(y_test, predictions)*100:.2f}%")