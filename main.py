import streamlit as st
import pandas as pd
import joblib

# Load trained model and encoder
model = joblib.load('house_model.pkl')
encoder = joblib.load('encoder.pkl')

# Streamlit UI
st.title("🏡 House Price Prediction")

# User Inputs
area = st.slider("House Area (sq ft)", min_value=500, max_value=5000, step=100)
bedrooms = st.selectbox("Number of Bedrooms", [1, 2, 3, 4, 5])
bathrooms = st.selectbox("Number of Bathrooms", [1, 2, 3, 4])
location = st.selectbox("Location", ['A', 'B', 'C'])

# Convert categorical input
location_encoded = encoder.transform([location])[0]

# Prediction
if st.button("Predict Price"):
    input_data = pd.DataFrame([[area, bedrooms, bathrooms, location_encoded]], 
                              columns=['area', 'bedrooms', 'bathrooms', 'location'])
    predicted_price = model.predict(input_data)[0]
    st.success(f"🏠 Estimated Price: ${predicted_price:,.2f}")
