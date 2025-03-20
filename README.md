# 🏡 House Price Prediction  

A **machine learning project** to predict house prices using **Streamlit, Docker, and joblib**.  

## 📂 Project Directory Structure  

```
House-Price-Prediction/
│── assets/
│   ├── images/
│   │   ├── logo.png
│   ├── styles/
│   │   ├── styles.css
│── house_model.pkl
│── encoder.pkl
│── main.py
│── Dockerfile
│── requirements.txt
│── .gitignore
```

---

## 🚀 Setup Guide  

### 1️⃣ **Clone the Repository**  
```bash
git clone https://github.com/Rahul5116/House-Price-Prediction.git
cd House-Price-Prediction
```

### 2️⃣ **Install Dependencies**  
```bash
pip install -r requirements.txt
```

### 3️⃣ **Run the App**  
```bash
streamlit run main.py
```

---

## 🖥️ **Code Files**  

### 🔹 `main.py`  
```python
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

```

---

### 🔹 `Dockerfile`
```dockerfile
# Use official Python image
FROM python:3.12

# Set working directory
WORKDIR /app

# Copy project files
COPY . /app

# Install dependencies
RUN pip install -r requirements.txt

# Expose port for Streamlit
EXPOSE 8501

# Run Streamlit
CMD ["streamlit", "run", "main.py", "--server.port=8501", "--server.enableCORS=false"]
```

---

### 🔹 `requirements.txt`
```
streamlit
pandas
joblib
scikit-learn
```

---

## 📸 **Adding Assets (Images & CSS)**  

### 1️⃣ **Create Required Folders**  
```bash
mkdir -p assets/images
mkdir -p assets/styles
```

### 2️⃣ **Move Files into Folders**  
```bash
mv logo.png assets/images/
mv styles.css assets/styles/
```

---

## 🔥 Git Commands (Save & Push Updates)  

### 1️⃣ **Stage & Commit Changes**  
```bash
git add .
git commit -m "Added logo, CSS, and updated main.py"
```

### 2️⃣ **Push to GitHub**  
```bash
git push origin main
```

---

## 🐳 Docker Commands  

### 1️⃣ **Build Docker Image**  
```bash
docker build -t house-price-prediction .
```

### 2️⃣ **Run Docker Container**  
```bash
docker run -p 8501:8501 house-price-prediction
```
