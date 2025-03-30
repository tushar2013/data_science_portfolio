# Importing necessary libraries
import pandas as pd
import numpy as np
import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Load the data
file_path = 'Telco-Customer-Churn.csv'
data = pd.read_csv(file_path)

# Data
st.write("### Data")
st.write(data.head())

# --------------------------
# ✅ Data Cleaning & Preprocessing
# --------------------------

# Convert TotalCharges to numeric and handle errors
data['TotalCharges'] = pd.to_numeric(data['TotalCharges'], errors='coerce')

# Handle missing values
data.fillna(data.mean(numeric_only=True), inplace=True)

# Encode categorical variables
label_enc = LabelEncoder()
for col in data.select_dtypes(include='object').columns:
    if col != 'customerID':
        data[col] = label_enc.fit_transform(data[col])

st.write("### Encoded Data")
st.write(data.head())

# Splitting features and target
X = data.drop(['customerID', 'Churn'], axis=1)
y = data['Churn']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Standardizing the data
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# --------------------------
# ✅ Model Training
# --------------------------
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# --------------------------
# ✅ Model Evaluation
# --------------------------
y_pred = model.predict(X_test)

# Metrics
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
report = classification_report(y_test, y_pred)

# --------------------------
# ✅ Streamlit Visualization
# --------------------------

st.title("📊 Telco Customer Churn Prediction")

# Display Model Metrics
st.write("### Model Performance:")
st.write(f"**Accuracy:** {accuracy:.4f}")
st.write("### Confusion Matrix:")
st.write(conf_matrix)
st.write("### Classification Report:")
st.code(report)

# User Prediction
st.write("### 📈 Make a New Prediction")
customer_data = {}
for col in X.columns:
    if data[col].dtype == 'float64' or data[col].dtype == 'int64':
        customer_data[col] = st.number_input(f"{col}", float(data[col].min()), float(data[col].max()), float(data[col].mean()))

# Convert to DataFrame
customer_df = pd.DataFrame([customer_data])
customer_df = scaler.transform(customer_df)

if st.button("Predict Churn"):
    churn_pred = model.predict(customer_df)
    churn_prob = model.predict_proba(customer_df)[0][1]
    
    if churn_pred[0] == 1:
        st.write(f"🔴 **Churn Risk: {churn_prob:.2%}**")
    else:
        st.write(f"🟢 **No Churn Risk: {churn_prob:.2%}**")

