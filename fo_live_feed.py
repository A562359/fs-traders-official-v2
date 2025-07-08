from smartapi import SmartConnect
from datetime import datetime
import pandas as pd
import time
import os

# 🔐 Replace with your real credentials
API_KEY = "your_api_key"
CLIENT_ID = "your_client_id"
PWD = "your_password"
TOTP = "your_totp"

obj = SmartConnect(api_key=API_KEY)
data = obj.generateSession(CLIENT_ID, PWD, TOTP)

# 🔍 Function to fetch Option Chain OI
def get_oi_data(symbol):
    # Replace this with real F&O instrument token from Angel One
    # Sample data structure (replace it with real token + logic)
    call_oi = 2500000  # Replace this
    put_oi = 1900000   # Replace this
    pcr = round(put_oi / call_oi, 2)
    signal = "BUY" if pcr > 1 else "SELL"
    return {
        "Time": datetime.now().strftime("%H:%M"),
        "Call OI": call_oi,
        "Put OI": put_oi,
        "Diff": put_oi - call_oi,
        "PCR": pcr,
        "Signal": signal
    }

# 🔁 Update CSV every 3 mins
def update_csv(file, symbol):
    row = get_oi_data(symbol)
    if os.path.exists(file):
        df = pd.read_csv(file)
        if df.empty or df["Time"].iloc[-1] != row["Time"]:
            df = pd.concat([df, pd.DataFrame([row])])
            df.to_csv(file, index=False)
    else:
        df = pd.DataFrame([row])
        df.to_csv(file, index=False)

# Call the function
update_csv("nifty_pcr.csv", "NIFTY")
update_csv("banknifty_pcr.csv", "BANKNIFTY")
