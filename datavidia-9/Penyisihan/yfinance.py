import pandas as pd
import pandas_ta as ta
import yfinance as yf

# Download USD/IDR data from Yahoo Finance
df = yf.download('USDIDR=X', start='2022-01-01', end='2024-12-31', interval='1d')

# Rename columns for consistency
df.columns = df.columns.map(lambda x: x[0])

# Calculate technical indicators
df['VWAP'] = ta.vwap(df['High'], df['Low'], df['Close'], df['Volume'])
df['RSI'] = ta.rsi(df['Close'], length=14)
df['Stoch'] = ta.stoch(df['High'], df['Low'], df['Close'], length=14)

df['Log_Return'] = ta.log_return(df['Close'], cumulative=True)
df['Percent_Return'] = ta.percent_return(df['Close'], cumulative=True)

print(df)
