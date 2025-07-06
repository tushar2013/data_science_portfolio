import pickle
import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

with open('dtree_pickle.pkl', 'rb') as pkl:
    model = pickle.load(pkl)

st.title('House Price Prediction App')

house_price_df = pd.read_csv('/home/neo/coding_playground/datasets/kc_house_data.csv')

column_values = []
for column in house_price_df.columns:
    if not column in ['date', 'price']:
        column_values.append(st.number_input(column.upper()))
        #column_values.append(
        #    st.number_input(column.upper(), 
        #    value=house_price_df[column].mean(), 
        #    min_value=0, 
        #    max_value=1212.1212, 
        #    step=12312)
        #)

if st.button('Make Prediction'):
    st.write(model.predict([column_values]))
