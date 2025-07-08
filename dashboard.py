import pandas as pd
import streamlit as st
from streamlit_autorefresh import st_autorefresh

st.set_page_config(layout="centered", page_title="FS Traders Official PCR", page_icon="📊")
st_autorefresh(interval=3 * 60 * 1000, key="refresh")

st.markdown("# 📊 FS Traders Official")
st.markdown("### NIFTY & BANKNIFTY PCR Live Dashboard (Auto-refresh every 3 mins)")

# Load CSVs
df_nifty = pd.read_csv("nifty_pcr.csv")
df_banknifty = pd.read_csv("banknifty_pcr.csv")

# Display tables
st.markdown("### 🔵 NIFTY PCR Overview")
st.table(df_nifty.tail(10))

st.markdown("### 🟢 BANKNIFTY PCR Overview")
st.table(df_banknifty.tail(10))
