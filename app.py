import streamlit as st
import pandas as pd
import joblib

print("NEW STREAMLIT APP RUNNING")

# Load model
model = joblib.load("Extra_Trees_Credit_model.pkl")

# Load encoders
encoders = {
    col: joblib.load(f"{col}_encoder.pkl")
    for col in ["Sex", "Housing", "Saving accounts", "Checking account", "Purpose"]
}

st.title("Credit Risk Prediction App")
st.write("Enter applicant information to predict if the credit risk is good or bad")

age = st.number_input("Age", 18, 80, 30)
sex = st.selectbox("Sex", ["male", "female"])
job = st.number_input("Job (0 - 3)", 0, 3, 1)
housing = st.selectbox("Housing", ["own", "rent", "free"])
saving_accounts = st.selectbox("Saving accounts", ["little", "moderate", "rich", "quite rich"])
checking_account = st.selectbox("Checking account", ["little", "moderate", "rich", "quite rich"])

# 👉 ADD PURPOSE INPUT
purpose = st.selectbox(
    "Purpose",
    ["car", "furniture", "radio/TV", "education", "business"]
)

credit_amount = st.number_input("Credit amount", 0, 10000)
duration = st.number_input("Duration (months)", 1, 100)

# Create dataframe
input_df = pd.DataFrame({
    "Age": [age],
    "Sex": [encoders["Sex"].transform([sex])[0]],
    "Job": [job],
    "Housing": [encoders["Housing"].transform([housing])[0]],
    "Saving accounts": [encoders["Saving accounts"].transform([saving_accounts])[0]],
    "Checking account": [encoders["Checking account"].transform([checking_account])[0]],
    "Purpose": [encoders["Purpose"].transform([purpose])[0]],
    "Credit amount": [credit_amount],
    "Duration": [duration]
})

# Match model column order
input_df = input_df[model.feature_names_in_]

# Predict
if st.button("Predict Risk"):
    pred = model.predict(input_df)[0]

    if pred == 1:
        st.success("The predicted credit risk is: Good")
    else:
        st.error("The predicted credit risk is: Bad")
