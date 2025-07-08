
import streamlit as st
from fo_live_feed import get_live_fno_data
from streamlit_autorefresh import st_autorefresh
from datetime import datetime

st.set_page_config(page_title="FS Traders - Live F&O Dashboard", layout="wide")
st_autorefresh(interval=3 * 60 * 1000, key="fno_refresh")
st.title("📊 FS Traders Official - Live Futures & Options Prices")
st.caption(f"Updated: {datetime.now().strftime('%H:%M:%S')} (Auto-refresh every 3 mins)")

try:
    fut_df, opt_df = get_live_fno_data()
    st.subheader("📈 Futures Live Prices")
    st.dataframe(fut_df, use_container_width=True)

    st.subheader("📉 Options Chain (CE/PE)")
    st.dataframe(opt_df, use_container_width=True)

except Exception as e:
    st.error(f"Error fetching data: {e}")
