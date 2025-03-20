import streamlit as st
import pandas as pd
import joblib
import os

# Function to load CSS
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Set paths for assets
css_file = os.path.join('assets', 'styles', 'styles.css')
logo_path = os.path.join('assets', 'images', 'logo.png')

# Load CSS
load_css(css_file)

# Display logo
st.image(logo_path, width=150)

# Title and description
st.title("🏡 House Price Prediction")
st.markdown("💰 **Predict the price of your dream home!** 🏠")

# Load trained model and encoder
model = joblib.load('house_model.pkl')
encoder = joblib.load('encoder.pkl')

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
