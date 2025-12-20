# train_1feature_model.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load your dataset
df = pd.read_csv("creditCard.csv")  # replace with your dataset file

# Use only 1 feature: 'Amount'
X = df[['Amount']]
y = df['Class']

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save 1-feature model
joblib.dump(model, "fraud_model_1feature.pkl")

print("1-feature model trained and saved successfully")
