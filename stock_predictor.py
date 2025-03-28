import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.express as px
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import datetime

# --- Streamlit App ---
st.title("📈 Stock Price Predictor")
st.sidebar.header("Select Stock and Parameters")

# --- User Inputs ---
_ticker = st.sidebar.text_input('Enter Stock Ticker (NSE)', '')
ticker = f'{_ticker.upper()}.NS'
period = st.sidebar.selectbox('Select Period', ['1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max'])
interval = st.sidebar.selectbox('Select Interval', ['1m', '5m', '15m', '30m', '1h', '1d', '1wk'])

# --- Fetch Stock Data ---
@st.cache_data
def fetch_data(ticker, period, interval):
    stock = yf.Ticker(ticker)
    df = stock.history(period=period, interval=interval)
    
    if df.empty:
        st.error("⚠️ No data found for the given ticker and period.")
        return None

    df.reset_index(inplace=True)
    df['Date'] = pd.to_datetime(df['Datetime'] if 'Datetime' in df.columns else df['Date'])
    return df

# --- Visualize Data ---
def plot_stock_data(df):
    fig = px.line(df, x='Date', y=['Open', 'High', 'Low', 'Close'],
                  labels={'value': 'Price', 'Date': 'Time'},
                  title=f'{ticker} Stock Prices Over Time')
    fig.update_traces(mode='lines+markers')
    st.plotly_chart(fig)

# --- Model Training & Prediction ---
def predict_stock(df, future_days=10):
    if len(df) < 2:
        st.warning("⚠️ Not enough data to train the model.")
        return None, None

    df['Days'] = (df['Date'] - df['Date'].min()).dt.days
    X = df[['Days']]
    y = df['Close']

    # Splitting into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Linear Regression Model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Predictions
    y_pred = model.predict(X_test)

    # Model Metrics
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    # Future Predictions
    future_dates = [(df['Date'].max() + datetime.timedelta(days=i)) for i in range(1, future_days + 1)]
    future_df = pd.DataFrame({'Date': future_dates})
    future_df['Days'] = (future_df['Date'] - df['Date'].min()).dt.days
    future_df['Predicted'] = model.predict(future_df[['Days']])

    return mse, r2, future_df

# --- Main Execution ---
df = fetch_data(ticker, period, interval)

if df is not None:
    st.subheader("📊 Stock Data")
    st.dataframe(df.tail())

    # Visualize Historical Data
    plot_stock_data(df)

    # Predict Future Prices
    mse, r2, future_df = predict_stock(df)

    if future_df is not None:
        st.subheader("🔮 Stock Price Prediction")
        
        # Display future predictions
        fig = px.line(future_df, x='Date', y='Predicted', title='Predicted Future Prices')
        fig.add_scatter(x=df['Date'], y=df['Close'], mode='lines', name='Actual', line=dict(color='blue'))
        fig.update_traces(mode='lines+markers')
        st.plotly_chart(fig)

        # Display Model Metrics
        st.write(f"📉 **Mean Squared Error:** {mse:.2f}")
        st.write(f"📈 **R² Score:** {r2:.2f}")

    # Show combined actual and predicted data
    combined_df = pd.concat([df[['Date', 'Close']], future_df[['Date', 'Predicted']].rename(columns={'Predicted': 'Close'})])
    combined_df.sort_values(by='Date', inplace=True)

    st.subheader("📊 Combined Actual and Predicted Prices")
    st.line_chart(combined_df.set_index('Date'))


