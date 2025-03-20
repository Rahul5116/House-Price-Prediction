import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder

# Sample dataset (Replace this with a real dataset)
data = {
    'area': [1200, 1500, 1800, 2000, 2500],
    'bedrooms': [2, 3, 3, 4, 4],
    'bathrooms': [1, 2, 2, 3, 3],
    'location': ['A', 'B', 'A', 'B', 'C'],
    'price': [200000, 250000, 280000, 320000, 400000]
}

df = pd.DataFrame(data)

# Encode categorical features
encoder = LabelEncoder()
df['location'] = encoder.fit_transform(df['location'])

# Split data into training & testing
X = df.drop(columns=['price'])
y = df['price']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save model
joblib.dump(model, 'house_model.pkl')
joblib.dump(encoder, 'encoder.pkl')
print("Model and encoder saved successfully!")
