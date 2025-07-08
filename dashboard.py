import streamlit as st
import pandas as pd
import random
from datetime import datetime, timedelta
from streamlit_autorefresh import st_autorefresh

# Auto-refresh every 3 minutes
st_autorefresh(interval=180000, key="refresh")

# Title
st.set_page_config(page_title="FS Traders Official", layout="wide")
st.title("📊 FS Traders Official")
st.markdown("### NIFTY & BANKNIFTY PCR Live Dashboard (Auto-refresh every 3 mins)")

# Generate time slots from 9:30 to 15:30 at 3-minute intervals
start_time = datetime.strptime("09:30", "%H:%M")
end_time = datetime.strptime("15:30", "%H:%M")
time_slots = []

while start_time <= end_time:
    time_slots.append(start_time.strftime("%H:%M"))
    start_time += timedelta(minutes=3)

# Generate dummy data
def generate_dummy_data():
    call_oi = random.randint(10_00_000, 25_00_000)
    put_oi = random.randint(10_00_000, 25_00_000)
    diff = put_oi - call_oi
    pcr = round(put_oi / call_oi, 2)
    signal = "BUY" if pcr >= 1 else "SELL"
    return call_oi, put_oi, diff, pcr, signal

# Create DataFrames
nifty_data = []
banknifty_data = []

for t in time_slots:
    nifty_row = [t] + list(generate_dummy_data())
    banknifty_row = [t] + list(generate_dummy_data())
    nifty_data.append(nifty_row)
    banknifty_data.append(banknifty_row)

nifty_df = pd.DataFrame(nifty_data, columns=["Time", "Call OI", "Put OI", "Diff", "PCR", "Signal"])
banknifty_df = pd.DataFrame(banknifty_data, columns=["Time", "Call OI", "Put OI", "Diff", "PCR", "Signal"])

# Layout
col1, col2 = st.columns(2)

with col1:
    st.subheader("🟦 NIFTY PCR Overview")
    st.dataframe(nifty_df, use_container_width=True)

with col2:
    st.subheader("🟩 BANKNIFTY PCR Overview")
    st.dataframe(banknifty_df, use_container_width=True)

# Footer
st.markdown("---")
st.markdown(f"<center><small>Updated at: {datetime.now().strftime('%H:%M:%S')}</small></center>", unsafe_allow_html=True)
