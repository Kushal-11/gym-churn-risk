import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load('../models/churn_model.pkl')

# Load user data
user_data = pd.read_csv('../data/USERS_DATA.CSV')

# Function to predict churn risk
def predict_churn(user_info):
    # Assuming the model expects a DataFrame with the same structure as the training data
    prediction = model.predict(user_info)
    return prediction

# Streamlit dashboard
st.title("Gym Member Churn Risk Prediction")

# User input for prediction
user_id = st.selectbox("Select User ID", user_data['user_id'].unique())
user_info = user_data[user_data['user_id'] == user_id]

if st.button("Predict Churn Risk"):
    if not user_info.empty:
        churn_risk = predict_churn(user_info.drop(columns=['user_id', 'first_name', 'last_name', 'birthdate', 'sign_up_date', 'user_location', 'subscription_plan']))
        st.write(f"Churn Risk for {user_info['first_name'].values[0]} {user_info['last_name'].values[0]}: {'High' if churn_risk[0] == 1 else 'Low'}")
    else:
        st.write("User not found.")