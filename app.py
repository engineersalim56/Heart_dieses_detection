import pickle
import streamlit as st
import numpy as np
# Load the trained machine learning model
model = pickle.load(open('train_model.pkl', 'rb'))

# Function to predict heart disease
def predict_heart_disease(age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal):
    # Map chest pain type string to numerical value
    cp_mapping = {"Typical Angina": 0, "Atypical Angina": 1, "Non-anginal Pain": 2, "Asymptomatic": 3}
    cp = cp_mapping.get(cp, 0)  # Default to 0 if the value is not found in the mapping

    input_data = np.array([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
    prediction = model.predict(input_data)[0]
    return prediction

# Streamlit app
st.title("Heart Disease Prediction App")
st.write("Welcome to the Heart Disease Prediction App!")

# User input fields
age = st.number_input("Age", min_value=1, max_value=100, value=30, step=1)
sex = st.radio("Gender", ["Male", "Female"])
cp = st.selectbox("Chest Pain Type", ["Typical Angina", "Atypical Angina", "Non-anginal Pain", "Asymptomatic"])
trestbps = st.number_input("Resting Blood Pressure", min_value=90, max_value=200, value=120, step=1)
chol = st.number_input("Serum Cholestoral (mg/dl)", min_value=100, max_value=400, value=200, step=1)
fbs = st.radio("Fasting Blood Sugar > 120 mg/dl", ["Yes", "No"])
restecg = st.selectbox("Resting Electrocardiographic Results", [0, 1, 2])
thalach = st.number_input("Maximum Heart Rate Achieved", min_value=50, max_value=200, value=150, step=1)
exang = st.radio("Exercise Induced Angina", ["Yes", "No"])
oldpeak = st.number_input("ST Depression Induced by Exercise Relative to Rest", min_value=0.0, max_value=6.0, value=0.0, step=0.1)
slope = st.selectbox("Slope of the Peak Exercise ST Segment", [0, 1, 2])
ca = st.number_input("Number of Major Vessels Colored by Flourosopy (0-3)", min_value=0, max_value=3, value=0, step=1)
thal = st.selectbox("Thal", [0, 1, 2])

# Predict button
if st.button("Predict Heart Disease"):
    sex = 1 if sex == "Male" else 0
    fbs = 1 if fbs == "Yes" else 0
    exang = 1 if exang == "Yes" else 0
    prediction = predict_heart_disease(age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal)
    
    # Display prediction result
    result_mapping = {0: "The patient has No Heart Disease", 1: "The patient has Heart Disease"}
    st.write(f"Prediction Result: {result_mapping[prediction]}")
