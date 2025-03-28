import yfinance as yf
import pandas as pd
import streamlit as st

ticker = st.text_input('Enter Stock', '')
period = st.selectbox('Select period', ('1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max',))
interval = st.selectbox('Select interval', ('1m', '5m'))

dat = yf.Ticker(f'{ticker.upper()}.NS')

def fetch_data():
    df = dat.history(period=period, interval=interval)
    df.reset_index(inplace=True)
    st.line_chart(df.set_index('Datetime')['High'])
    return df.tail()

if st.button('Fetch Data'):
    st.write(fetch_data())


