import streamlit as st
import yfinance as yf
import pandas as pd

ticker = 'M&M.NS'
today = pd.Timestamp.now(tz='Asia/Kolkata').normalize()

data = yf.Ticker(ticker)
df = data.history(period='1mo').loc[today:today + pd.Timedelta(days=1)]

df
