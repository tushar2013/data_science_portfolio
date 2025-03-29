# app.py

import streamlit as st
import pandas as pd
import joblib

# Load Models
rf_model = joblib.load("rf_model.pkl")
#xgb_model = joblib.load("xgb_model.pkl")
#cat_model = joblib.load("cat_model.pkl")

# Load Data
data = pd.read_csv("Telco-Customer-Churn.csv")

# Sidebar
st.sidebar.title("Model Selection")
model_choice = st.sidebar.selectbox("Choose a Model", ["RandomForest", "XGBoost", "CatBoost"])

# Display Data
st.write("### Customer Churn Data Sample")
st.write(data.head())

# User Input
st.write("### Input Customer Data")
customer_data = {}

for col in data.columns:
    try:
        # Try to convert to float if numeric
        customer_data[col] = st.number_input(
            f"{col}", 
            float(data[col].min()), 
            float(data[col].max()), 
            float(data[col].mean())
        )
    except ValueError:
        # Use selectbox for non-numeric columns
        customer_data[col] = st.selectbox(
            f"{col}", 
            data[col].unique()
        )

# Display the final customer input data
st.write("### Customer Input Data")
st.write(customer_data)

#for col in data.columns[:-1]:
#    customer_data[col] = st.number_input(f"{col}", float(data[col].min()), float(data[col].max()), float(data[col].mean()))
#
customer_df = pd.DataFrame([customer_data])

# Prediction
model = {"RandomForest": rf_model}[model_choice] # "XGBoost": xgb_model, "CatBoost": cat_model}[model_choice]
prediction = model.predict(customer_df)[0]

# Display Prediction
st.write("### Prediction:")
st.success("Churn" if prediction == 1 else "No Churn")

# Visualize Feature Importance
import matplotlib.pyplot as plt

st.write("### Feature Importance")
importance = pd.Series(model.feature_importances_, index=customer_df.columns)
importance.sort_values(ascending=False).plot(kind='barh')
st.pyplot(plt)
