import yfinance as yf
import pandas as pd
import streamlit as st

dat = yf.Ticker("TCS.NS")

def fetch_data():
    df = dat.history(period='1d', interval='1m')
    df.reset_index(inplace=True)
    st.line_chart(df.set_index('Datetime')['High'])
    return df 

if st.button('Fetch Data'):
    st.write(fetch_data())
