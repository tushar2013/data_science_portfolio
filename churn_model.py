# churn_model.py

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from catboost import CatBoostClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Load Data
data = pd.read_csv('Telco-Customer-Churn.csv')

# EDA
data.dropna(inplace=True)
data = pd.get_dummies(data, drop_first=True)

# Splitting the Data
X = data.drop('Churn_Yes', axis=1)
y = data['Churn_Yes']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# RandomForest Model with GridSearchCV
param_grid = {
    'n_estimators': [100, 200, 300],
    'max_depth': [10, 15, 20],
    'min_samples_split': [2, 5, 10]
}

rf = RandomForestClassifier(random_state=42)
grid_search = GridSearchCV(rf, param_grid, cv=5, scoring='accuracy')
grid_search.fit(X_train, y_train)

# XGBoost Model
#xgb_model = XGBClassifier(n_estimators=200, learning_rate=0.1)
#xgb_model.fit(X_train, y_train)

# CatBoost Model
#cat_model = CatBoostClassifier(iterations=300, depth=6, learning_rate=0.1, verbose=0)
#cat_model.fit(X_train, y_train)

# Model Evaluation
def evaluate_model(model, name):
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    print(f"{name} Accuracy: {acc:.4f}")
    print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
    print("Classification Report:\n", classification_report(y_test, y_pred))
    return acc

rf_acc = evaluate_model(grid_search.best_estimator_, "RandomForest with GridSearchCV")
#xgb_acc = evaluate_model(xgb_model, "XGBoost")
#cat_acc = evaluate_model(cat_model, "CatBoost")

# Export Models
import joblib
joblib.dump(grid_search.best_estimator_, "rf_model.pkl")
#joblib.dump(xgb_model, "xgb_model.pkl")
#joblib.dump(cat_model, "cat_model.pkl")
