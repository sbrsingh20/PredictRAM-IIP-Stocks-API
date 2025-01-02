import streamlit as st
import pandas as pd
import requests
import matplotlib.pyplot as plt

# Helper function to fetch economic data from your API
def get_economic_data(date=None):
    url = "https://your-api-url.com/economic-data"  # Replace with your API URL
    if date:
        url += f"?date={date}"
    response = requests.get(url)
    return pd.DataFrame(response.json())

# Helper function to fetch stock data from your API
def get_stock_data(symbol, start_date=None, end_date=None):
    url = f"https://your-api-url.com/stock-data?symbol={symbol}"  # Replace with your API URL
    if start_date:
        url += f"&start_date={start_date}"
    if end_date:
        url += f"&end_date={end_date}"
    response = requests.get(url)
    return pd.DataFrame(response.json())

# Streamlit interface to allow users to interact with the data
st.title("Economic and Stock Data API")

# Sidebar for input options
st.sidebar.header("Input Options")

# Economic Data Section
st.sidebar.subheader("Economic Data")
date_input = st.sidebar.date_input("Select Date", pd.to_datetime("2024-11-01"))

if st.sidebar.button("Get Economic Data"):
    economic_data = get_economic_data(date_input.strftime('%Y-%m-%d'))
    st.subheader(f"Economic Data for {date_input.strftime('%Y-%m-%d')}")
    st.write(economic_data)

# Stock Data Section
st.sidebar.subheader("Stock Data")
stock_symbol = st.sidebar.text_input("Enter Stock Symbol", "AAPL")
start_date = st.sidebar.date_input("Start Date", pd.to_datetime("2024-01-01"))
end_date = st.sidebar.date_input("End Date", pd.to_datetime("2024-12-31"))

if st.sidebar.button("Get Stock Data"):
    stock_data = get_stock_data(stock_symbol, start_date.strftime('%Y-%m-%d'), end_date.strftime('%Y-%m-%d'))
    st.subheader(f"Stock Data for {stock_symbol}")
    st.write(stock_data)

    # Plot the stock data (Optional)
    fig, ax = plt.subplots()
    ax.plot(stock_data['Date'], stock_data['Close'], label='Closing Price')
    ax.set_xlabel('Date')
    ax.set_ylabel('Price')
    ax.set_title(f'{stock_symbol} Stock Price')
    plt.xticks(rotation=45)
    st.pyplot(fig)
