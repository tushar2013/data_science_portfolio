# Telco Customer Churn Prediction Project

## 📌 **Project Overview**
This project aims to predict **customer churn** (whether a customer will leave or stay) using the **Telco Customer Churn dataset**. The solution involves:
- Data preprocessing (handling missing values, encoding categorical variables)
- Model training using **Logistic Regression**
- Model evaluation using accuracy, confusion matrix, and classification report
- Visualization of model performance and metrics using Streamlit

---

## 📊 **Dataset Information**
The dataset used for this project is `Telco-Customer-Churn.csv`, containing customer data with the following columns:

- `customerID`: Unique ID for each customer
- `gender`: Gender of the customer (Male/Female)
- `SeniorCitizen`: Whether the customer is a senior citizen (1: Yes, 0: No)
- `Partner`: Whether the customer has a partner (Yes/No)
- `Dependents`: Whether the customer has dependents (Yes/No)
- `tenure`: Number of months the customer has stayed with the company
- `PhoneService`: Whether the customer has phone service (Yes/No)
- `MultipleLines`: Whether the customer has multiple lines (Yes/No/No phone service)
- `InternetService`: Type of internet service (DSL, Fiber optic, None)
- `OnlineSecurity`: Whether the customer has online security (Yes/No/No internet service)
- `OnlineBackup`: Whether the customer has online backup (Yes/No/No internet service)
- `DeviceProtection`: Whether the customer has device protection (Yes/No/No internet service)
- `TechSupport`: Whether the customer has tech support (Yes/No/No internet service)
- `StreamingTV`: Whether the customer has streaming TV service (Yes/No/No internet service)
- `StreamingMovies`: Whether the customer has streaming movies service (Yes/No/No internet service)
- `Contract`: The contract term (Month-to-month, One year, Two years)
- `PaperlessBilling`: Whether the customer uses paperless billing (Yes/No)
- `PaymentMethod`: Payment method (Electronic check, Mailed check, Bank transfer, Credit card)
- `MonthlyCharges`: The monthly charges for the customer
- `TotalCharges`: The total charges incurred by the customer
- `Churn`: The target variable (Yes/No)

---

## ⚙️ **Project Workflow**

### 1️⃣ **Data Preprocessing**
Before training the model, the data undergoes cleaning and preprocessing:
- **Missing values:** The `TotalCharges` column contains some missing or empty values, which are converted to `NaN` and filled with the median.
- **Encoding categorical variables:** Categorical columns are converted to numerical using **Label Encoding**.
- **Feature and target separation:** 
  - `X`: Contains the customer attributes (features)
  - `y`: Contains the target variable (`Churn`)
- **Train-test split:** The dataset is split into **80% training** and **20% testing** sets.

---

### 2️⃣ **Model Training**
The model used for this project is:
- **Logistic Regression**: A simple, effective model for binary classification problems.

---

### 3️⃣ **Model Evaluation**
The model's performance is assessed using:
- **Accuracy**: Measures the proportion of correctly predicted labels.
- **Confusion Matrix**: Shows the distribution of true positives, true negatives, false positives, and false negatives.
- **Classification Report**: Includes:
    - **Precision:** Proportion of positive predictions that were actually correct.
    - **Recall:** Proportion of actual positives correctly identified.
    - **F1-Score:** The harmonic mean of precision and recall.
    - **Support:** The number of occurrences of each label in the dataset.

---

## 🔥 **Streamlit App Functionalities**

The project is wrapped in a **Streamlit web app** with the following features:
- **Sidebar controls**:
    - Upload CSV file
    - View raw data
- **Training and evaluation**:
    - Train the Logistic Regression model
    - Display accuracy, confusion matrix, and classification report
- **Model testing with custom input**:
    - Allows the user to input customer details and predict churn status in real time
- **Visualization**:
    - Confusion matrix plotted using `seaborn`

---

## 📈 **Results and Insights**

### ✅ **Model Performance**
The model's accuracy and classification report are displayed in the app, providing insights into the model's effectiveness:
- **Accuracy**: The proportion of correctly classified samples
- **Precision & Recall**: Indicators of model quality
- **F1-Score**: Balances precision and recall

### 📉 **Confusion Matrix Visualization**
A confusion matrix visualizes the performance by displaying:
- **True Positives (TP)**: Correctly predicted churn cases
- **True Negatives (TN)**: Correctly predicted non-churn cases
- **False Positives (FP)**: Incorrectly predicted churn cases
- **False Negatives (FN)**: Incorrectly predicted non-churn cases

---

## 🛠️ **Technologies Used**
- **Python**: Core programming language
- **Pandas**: Data manipulation and preprocessing
- **NumPy**: Numerical operations
- **Scikit-Learn**: Model building and evaluation
- **Seaborn & Matplotlib**: Data visualization
- **Streamlit**: Interactive web app framework

---

## 📚 **Code Execution Instructions**

1. Install the required libraries:
```bash
pip install pandas numpy scikit-learn streamlit matplotlib seaborn

