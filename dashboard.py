# dashboard.py

import streamlit as st
import pandas as pd
from streamlit_autorefresh import st_autorefresh

st.set_page_config(page_title="FS Traders Official", layout="wide")
st_autorefresh(interval=3 * 60 * 1000)  # Refresh every 3 mins

st.title("📊 FS Traders Official")
st.markdown("**NIFTY & BANKNIFTY PCR Live Dashboard (Auto-refresh every 3 mins)**")

col1, col2 = st.columns(2)

with col1:
    st.subheader("🔵 NIFTY PCR Overview")
    df_nifty = pd.read_csv("nifty_pcr.csv")
    st.dataframe(df_nifty)

with col2:
    st.subheader("🟢 BANKNIFTY PCR Overview")
    df_bank = pd.read_csv("banknifty_pcr.csv")
    st.dataframe(df_bank)
