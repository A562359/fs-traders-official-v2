import os
import pandas as pd

# Check if data files exist, else create dummy data
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
    dummy_bank.to_csv("banknifty_pcr.csv", index=False)from datetime import datetime
import random

# Simulated Angel One data fetch (replace with actual API later)
def fetch_live_pcr(symbol):
    # Simulate live call/put OI data for now
    call_oi = random.randint(1000000, 3000000)
    put_oi = random.randint(1000000, 3000000)
    time_now = datetime.now().strftime("%H:%M")
    pcr = round(put_oi / call_oi, 2)
    signal = "BUY" if pcr > 1 else "SELL"

    return {
        "Time": time_now,
        "Call OI": call_oi,
        "Put OI": put_oi,
        "Diff": put_oi - call_oi,
        "PCR": pcr,
        "Signal": signal
    }

# Append new row to CSV every 3 mins (simulated for now)
def update_csv(file_name, symbol):
    df = pd.read_csv(file_name)
    new_row = fetch_live_pcr(symbol)
    if df.empty or df["Time"].iloc[-1] != new_row["Time"]:  # avoid duplicates
        df = pd.concat([df, pd.DataFrame([new_row])])
        df.to_csv(file_name, index=False)

update_csv("nifty_pcr.csv", "NIFTY")
update_csv("banknifty_pcr.csv", "BANKNIFTY")

