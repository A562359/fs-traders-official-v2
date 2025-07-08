import os
import pandas as pd
import streamlit as st
from streamlit_autorefresh import st_autorefresh

# 🔁 Auto-refresh every 3 minutes
st_autorefresh(interval=3 * 60 * 1000, key="refresh")

# 🎯 Dashboard Title
st.markdown("<h1 style='text-align: center;'>📊 FS Traders Official</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>NIFTY & BANKNIFTY PCR Live Dashboard (Auto-refresh every 3 mins)</h4>", unsafe_allow_html=True)
st.markdown("---")

# 🧪 Dummy data if CSV not found
if not os.path.exists("nifty_pcr.csv"):
    dummy_nifty = pd.DataFrame([{
        "Time": "09:30",
        "Call OI": 0,
        "Put OI": 0,
        "Diff": 0,
        "PCR": 0,
        "Signal": "N/A"
    }])
    dummy_nifty.to_csv("nifty_pcr.csv", index=False)

if not os.path.exists("banknifty_pcr.csv"):
    dummy_bank = pd.DataFrame([{
        "Time": "09:30",
        "Call OI": 0,
        "Put OI": 0,
        "Diff": 0,
        "PCR": 0,
        "Signal": "N/A"
    }])
    dummy_bank.to_csv("banknifty_pcr.csv", index=False)

# 📂 Load CSVs
try:
    df_nifty = pd.read_csv("nifty_pcr.csv")
except Exception as e:
    st.error("❌ NIFTY file not found ya corrupt hai.")
    df_nifty = pd.DataFrame()

try:
    df_banknifty = pd.read_csv("banknifty_pcr.csv")
except Exception as e:
    st.error("❌ BANKNIFTY file not found ya corrupt hai.")
    df_banknifty = pd.DataFrame()

# 🔵 NIFTY PCR Table
st.markdown("### 🔵 NIFTY PCR Overview")
if not df_nifty.empty:
    st.table(df_nifty.tail(10))  # Show last 10 entries
else:
    st.warning("No NIFTY data available.")

# 🟢 BANKNIFTY PCR Table
st.markdown("### 🟢 BANKNIFTY PCR Overview")
if not df_banknifty.empty:
    st.table(df_banknifty.tail(10))
else:
    st.warning("No BANKNIFTY data available.")
