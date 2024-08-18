import polars as pl
import pandas as pd
from openbb import obb

my_pat = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdXRoX3Rva2VuIjoiRmJ2b0VjZ2Q2bW51RVZ0WFQ1enlDRHY0dWFwdWp3RUlhdjZDcUc5MyIsImV4cCI6MTc1NTQ3MDQyM30.z0T30AQXH_M4qQ54j1qnwaLcxvFT7ZObnu4JRSaP1NQ"

# Login with your API token
try:
    obb.account.login(pat=my_pat, remember_me=True)
    print("Login successful!")
except Exception as e:
    print(f"Login failed: {e}")

# # Get symbol list
# mx_tickers_df = obb.equity.screener(country="MX",provider="fmp").to_df()
# print(mx_tickers_df)
# print(mx_tickers_df.iloc[:,0])

# Mock portfolio
symbols = [
    "AAPL","MSFT","GOOGL","AMZN","META",
    "TSLA","BRK-B","V","JNJ","WMT","JPM",
    "MA","PG","UNH","DIS", "NVDA","HD", 
    "PYPL","BAC", "VZ","ADBE","CMCSA","NFLX",
    "KO","NKE","MRK","PEP","T","PFE","INTC",
]

# Query data
data = obb.equity.price.historical(symbol=symbols, #mx_tickers_df.iloc[:,0], 
                                   start_date="2020-01-01",
                                   end_date="2023-12-31",
                                   provider="polygon").to_df()
#data = data["Adj Close"]
# Logout OBB
obb.account.logout()

df_polars = pl.from_pandas(data)
print(df_polars)