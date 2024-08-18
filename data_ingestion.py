import polars as pl
import pandas as pd
from openbb import obb

# # Get symbol list
# mx_tickers_df = obb.equity.screener(country="MX",provider="fmp").to_df()
# print(mx_tickers_df)

def connect_to_obb(my_pat="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdXRoX3Rva2VuIjoiRmJ2b0VjZ2Q2bW51RVZ0WFQ1enlDRHY0dWFwdWp3RUlhdjZDcUc5MyIsImV4cCI6MTc1NTQ3MDQyM30.z0T30AQXH_M4qQ54j1qnwaLcxvFT7ZObnu4JRSaP1NQ"):

    # Login with your API token
    try:
        obb.account.login(pat=my_pat, remember_me=True)
        print("Login successful!")
    except Exception as e:
        print(f"Login failed: {e}")

def query_stock_data(symbols):
    
    connect_to_obb()

    # Query data
    data_df = obb.equity.price.historical(symbol=symbols, #mx_tickers_df.iloc[:,0], 
                                          start_date="2023-01-01",
                                          end_date="2023-12-31",
                                          provider="polygon").to_df()
    # Logout OBB
    obb.account.logout()
    
    return data_df

# Use polars rather than pandas
#df_polars = pl.from_pandas(data)
