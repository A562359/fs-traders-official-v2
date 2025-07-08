import streamlit as st
import pandas as pd
import time
from fo_live_feed import fetch_live_fo_data

st.set_page_config(layout="wide", page_title="📊 FS Traders Official - PCR Dashboard")

st.title("📊 FS Traders Official")
st.markdown("### NIFTY & BANKNIFTY PCR Live Dashboard (Auto-refresh every 3 mins)")

placeholder = st.empty()

def display_dashboard():
    while True:
        with placeholder.container():
            nifty_df, banknifty_df = fetch_live_fo_data()

            col1, col2 = st.columns(2)

            with col1:
                st.subheader("📘 NIFTY PCR Overview")
                st.dataframe(nifty_df, use_container_width=True)

            with col2:
                st.subheader("📗 BANKNIFTY PCR Overview")
                st.dataframe(banknifty_df, use_container_width=True)

        time.sleep(180)

display_dashboard()
