import streamlit as st
import pandas as pd
from streamlit_autorefresh import st_autorefresh
from datetime import datetime

# 🔁 Auto-refresh every 3 mins (180000 ms)
st_autorefresh(interval=180000, limit=None, key="pcr_dashboard_refresh")

# 🌐 Page settings
st.set_page_config(page_title="FS Traders Official", layout="wide")

# 🧠 Title
st.markdown("<h1 style='text-align: center;'>📊 FS Traders Official</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>NIFTY & BANKNIFTY PCR Live Dashboard (Auto-refresh every 3 mins)</h4>", unsafe_allow_html=True)
st.markdown("---")

# 📥 Dummy data (replace this with your real-time data source)
nifty_data = {
    "Time": ["09:30", "09:45", "10:00"],
    "Call OI": [15049875, 21340725, 24376125],
    "Put OI": [16087000, 21926700, 22910175],
    "Diff": [-1037925, -586975, -1465950],
    "PCR": [1.07, 1.03, 0.94],
    "Signal": ["BUY", "BUY", "SELL"]
}

banknifty_data = {
    "Time": ["09:30", "09:45", "10:00"],
    "Call OI": [182420, 258285, 451885],
    "Put OI": [412400, 602575, 763875],
    "Diff": [229980, 344290, 311990],
    "PCR": [2.26, 2.34, 1.69],
    "Signal": ["BUY", "BUY", "BUY"]
}

nifty_df = pd.DataFrame(nifty_data)
banknifty_df = pd.DataFrame(banknifty_data)

# 🎨 Layout with columns
col1, col2 = st.columns(2)

# 🔷 NIFTY PCR
with col1:
    st.markdown("### 🟦 NIFTY PCR Overview")
    st.dataframe(nifty_df, use_container_width=True)

# 🟩 BANKNIFTY PCR
with col2:
    st.markdown("### 🟩 BANKNIFTY PCR Overview")
    st.dataframe(banknifty_df, use_container_width=True)

# 📅 Footer
st.markdown("---")
st.markdown(f"<center><small>Updated at: {datetime.now().strftime('%H:%M:%S')} | Auto-refreshes every 3 minutes</small></center>", unsafe_allow_html=True)
