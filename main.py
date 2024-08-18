import streamlit as st
import pandas as pd
import base64
import os

from data_ingestion import query_stock_data

# Mock portfolio
sample_symbols = [
    "AAPL","MSFT","GOOGL","AMZN","META","TSLA","BRK-B","V","JNJ","WMT","JPM","MA","PG",
    "UNH","DIS", "NVDA","HD","PYPL","BAC", "VZ","ADBE","CMCSA","NFLX", "KO","NKE","MRK",
    "PEP","T","PFE","INTC",
]

st.set_page_config(layout="wide")  # this needs to be the first Streamlit command

st.title('Financial Espresso')

st.markdown("""
#### **Caffeine for Financial Data & Analysis**
""")

def get_root_dir():
    script_path = os.path.dirname(os.path.realpath(__file__))
    root_dir = os.path.dirname(script_path)
    return root_dir
root_dir_path = get_root_dir()

# Load data
@st.cache
def query_financial_data():
    data = query_stock_data(symbols=sample_symbols)
    return data

source_df = query_financial_data()
print(source_df)

# Sidebar
st.sidebar.header('Stock Selection')

# Sidebar - State selection
sorted_unique_symbol = sorted(source_df.symbol.unique())
selected_symbol = st.sidebar.multiselect('symbol', sorted_unique_symbol, sorted_unique_symbol)

# # Sidebar - Supplier selection
# sorted_unique_supplier = sorted(source_df.Proveedor.unique())
# selected_supplier = st.sidebar.multiselect('Proveedor', sorted_unique_supplier, sorted_unique_supplier)

# # Sidebar - Category selection
# unique_category = ['Acero y Metal','Cementos y Pegazulejo','Block y Ladrillo','Maquinaria y Equipo']
# selected_category = st.sidebar.multiselect('Materiales', unique_category, unique_category)

# Filtering data
df_selected = source_df[
    (source_df.symbol.isin(selected_symbol))
    # (source_df.Proveedor.isin(selected_supplier)) &
    # (source_df.Categoria.isin(selected_category))
    ]

st.header('US equities - Historical prices')
# st.write('Productos seleccionados: ' + str(df_selected.shape[0]))
st.dataframe(df_selected)

# # Download selected data
# # https://discuss.streamlit.io/t/how-to-download-file-in-streamlit/1806
# def filedownload(df):
#     csv = df.to_csv(index=False)
#     b64 = base64.b64encode(csv.encode()).decode()  # strings <-> bytes conversions
#     href = f'<a href="data:file/csv;base64,{b64}" download="unit_prices_download.csv">Descargar datos</a>'
#     return href

# st.markdown(filedownload(df_selected), unsafe_allow_html=True)