import pandas as pd
import numpy as np
import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error

print("Starting Incident Risk Prediction Model Training...")

# Setting seed for reproducibility
np.random.seed(42)

# Creating a dataset that looks like a ServiceNow Export
data = {
    'incident_id': [f'INC00{i}' for i in range(100)],
    'priority': np.random.randint(1, 5, 100),           # 1 (High) to 4 (Low)
    'reassignment_count': np.random.randint(0, 10, 100),# How many times it "bounced"
    'age_days': np.random.randint(1, 30, 100),          # Days open
    'sentiment_score': np.random.uniform(0, 1, 100),    # 0 (Angry) to 1 (Happy)
    'escalation_score': []                              # The Target (Y) we will "simulate"
}

for i in range(100):
    score = (data['age_days'][i] * 2) + (data['reassignment_count'][i] * 5) + ((1 - data['sentiment_score'][i]) * 20)
    data['escalation_score'].append(min(score, 100)) 

df = pd.DataFrame(data)
df.loc[df.sample(frac=0.1).index, 'reassignment_count'] = np.nan
df['reassignment_count'] = df['reassignment_count'].fillna(0)

features = df[['priority', 'reassignment_count', 'age_days', 'sentiment_score']]
target = df['escalation_score']

X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

print("Model Training Complete.")
model_filename = 'incident_risk_model.joblib'
joblib.dump(model, model_filename)
print(f"Model saved as {model_filename}")
