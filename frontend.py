# streamlit_frontend.py
import streamlit as st
import requests

# FastAPI URL
API_URL = "http://127.0.0.1:8000/predict/forest"

# Page title
st.title("Churn Classification")

# Input fields for CustomData
credit_score = st.number_input("Credit Score", min_value=300, max_value=850, step=1)
geography = st.selectbox("Geography", ["France", "Spain", "Germany"])
gender = st.selectbox("Gender", ["Male", "Female"])
age = st.number_input("Age", min_value=18, max_value=100, step=1)
tenure = st.number_input("Tenure (years as a customer)", min_value=0, max_value=10, step=1)
balance = st.number_input("Balance", min_value=0.0, step=100.0)
num_of_products = st.number_input("Number of Products", min_value=0, max_value=4, step=1)
has_cr_card = st.selectbox("Has Credit Card?", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
is_active_member = st.selectbox("Is Active Member?", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
estimated_salary = st.number_input("Estimated Salary", min_value=0.0, step=1000.0)

# Add a button to submit the form
if st.button("Predict"):
    # Prepare the data in the format expected by FastAPI
    input_data = {
        "CreditScore": credit_score,
        "Geography": geography,
        "Gender": gender,
        "Age": age,
        "Tenure": tenure,
        "Balance": balance,
        "NumOfProducts": num_of_products,
        "HasCrCard": has_cr_card,
        "IsActiveMember": is_active_member,
        "EstimatedSalary": estimated_salary
    }

    # Make a POST request to FastAPI
    try:
        response = requests.post(API_URL, json=input_data)

        if response.status_code == 200:
            result = response.json()
            st.success(f"Prediction Result: {result}")
        else:
            st.error(f"Error {response.status_code}: {response.json()['detail']}")
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
